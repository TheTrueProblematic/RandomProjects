#!/usr/bin/env python3
"""
DVD sorter for MKV files on Windows.

Run this script inside the folder you want to clean up.
It will:
- Look only at MKV files in the current folder
- Detect video resolution using ffprobe or mediainfo
- Classify as HD if height > 768 or width >= 1080, otherwise move to a subfolder named DVD
  This explicitly treats 720x480 as DVD
- Create the DVD folder if it does not exist and reuse it if it does
- Never touch subfolders

Optional CLI flags:
  --dry-run            Show what would happen without moving files
  --path "C:\Movies"   Process a specific folder instead of the current one
"""

from __future__ import annotations

import argparse
import json
import logging
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional, Tuple

LOG = logging.getLogger("dvd_sorter")


def configure_logging(very_verbose: bool = True) -> None:
    level = logging.DEBUG if very_verbose else logging.INFO
    handler = logging.StreamHandler(stream=sys.stdout)
    fmt = "%(asctime)s | %(levelname)-8s | %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    handler.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))
    LOG.setLevel(level)
    LOG.addHandler(handler)


def which(cmd: str) -> Optional[str]:
    path = shutil.which(cmd)
    return path


def detect_tools() -> Tuple[Optional[str], Optional[str]]:
    ffprobe = which("ffprobe") or which("ffprobe.exe")
    mediainfo = which("mediainfo") or which("mediainfo.exe")
    if ffprobe:
        LOG.debug(f"Found ffprobe at {ffprobe}")
    else:
        LOG.debug("ffprobe not found in PATH")
    if mediainfo:
        LOG.debug(f"Found mediainfo at {mediainfo}")
    else:
        LOG.debug("mediainfo not found in PATH")
    return ffprobe, mediainfo


def get_resolution_with_ffprobe(ffprobe: str, file: Path) -> Optional[Tuple[int, int]]:
    cmd = [
        ffprobe,
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height",
        "-of", "json",
        str(file),
    ]
    LOG.debug(f"Running ffprobe: {' '.join(cmd)}")
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        data = json.loads(out.decode("utf-8", errors="replace"))
        streams = data.get("streams", [])
        if not streams:
            LOG.warning(f"No video streams found in {file.name}")
            return None
        s0 = streams[0]
        width = int(s0.get("width", 0))
        height = int(s0.get("height", 0))
        if width and height:
            LOG.debug(f"ffprobe says {file.name} is {width}x{height}")
            return width, height
        LOG.warning(f"Could not read width or height for {file.name} with ffprobe")
        return None
    except subprocess.CalledProcessError as e:
        LOG.error(f"ffprobe failed on {file.name}. Output: {e.output.decode('utf-8', errors='replace')}")
        return None
    except Exception as e:
        LOG.exception(f"Unexpected error probing {file.name} with ffprobe: {e}")
        return None


def get_resolution_with_mediainfo(mediainfo: str, file: Path) -> Optional[Tuple[int, int]]:
    cmd = [mediainfo, "--Output=JSON", str(file)]
    LOG.debug(f"Running mediainfo: {' '.join(cmd)}")
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        data = json.loads(out.decode("utf-8", errors="replace"))
        media = data.get("media", {})
        tracks = media.get("track", [])
        for t in tracks:
            if t.get("@type") == "Video":
                width = int(str(t.get("Width", "0")).split()[0]) if t.get("Width") else 0
                height = int(str(t.get("Height", "0")).split()[0]) if t.get("Height") else 0
                if width and height:
                    LOG.debug(f"mediainfo says {file.name} is {width}x{height}")
                    return width, height
        LOG.warning(f"mediainfo could not find video track for {file.name}")
        return None
    except subprocess.CalledProcessError as e:
        LOG.error(f"mediainfo failed on {file.name}. Output: {e.output.decode('utf-8', errors='replace')}")
        return None
    except Exception as e:
        LOG.exception(f"Unexpected error probing {file.name} with mediainfo: {e}")
        return None


def get_video_resolution(file: Path, ffprobe: Optional[str], mediainfo: Optional[str]) -> Optional[Tuple[int, int]]:
    if ffprobe:
        res = get_resolution_with_ffprobe(ffprobe, file)
        if res:
            return res
    if mediainfo:
        res = get_resolution_with_mediainfo(mediainfo, file)
        if res:
            return res
    return None


def is_hd(width: int, height: int) -> bool:
    """
    HD rule:
    - True if height > 768 or width >= 1080
    - False otherwise
    """
    result = (height > 768) or (width >= 1080)
    LOG.debug(
        f"HD check for {width}x{height}: "
        f"height>768={'yes' if height > 768 else 'no'} or width>=1080={'yes' if width >= 1080 else 'no'} "
        f"-> {'HD' if result else 'DVD'}"
    )
    return result


def ensure_dir(path: Path) -> None:
    if not path.exists():
        LOG.debug(f"Creating directory {path}")
        path.mkdir(parents=True, exist_ok=True)
    else:
        LOG.debug(f"Directory already exists: {path}")


def uniquify(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem = dest.stem
    suffix = dest.suffix
    parent = dest.parent
    i = 1
    while True:
        candidate = parent / f"{stem} ({i}){suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def move_file(src: Path, dst_dir: Path, dry_run: bool = False) -> Path:
    ensure_dir(dst_dir)
    target = dst_dir / src.name
    target = uniquify(target)
    if dry_run:
        LOG.info(f"[DRY RUN] Would move: {src.name} -> {target}")
        return target
    LOG.info(f"Moving: {src.name} -> {target}")
    shutil.move(str(src), str(target))
    return target


def scan_folder(folder: Path, dry_run: bool) -> None:
    LOG.info(f"Starting scan in folder: {folder}")
    ffprobe, mediainfo = detect_tools()
    if not ffprobe and not mediainfo:
        LOG.error("No probe tools found. Install one of these to read video resolution.")
        LOG.error("Option 1: Install FFmpeg and make sure ffprobe is in PATH.")
        LOG.error("Option 2: Install MediaInfo CLI and make sure mediainfo is in PATH.")
        LOG.error("Skipping all moves because resolution can not be determined safely.")
    dvd_dir = folder / "DVD"

    total = 0
    moved = 0
    skipped = 0
    failed = 0

    for entry in folder.iterdir():
        if entry.is_dir():
            LOG.debug(f"Skipping directory: {entry.name}")
            continue
        if entry.suffix.lower() != ".mkv":
            LOG.debug(f"Skipping non MKV file: {entry.name}")
            continue

        total += 1
        LOG.info(f"Processing file {total}: {entry.name}")

        res = get_video_resolution(entry, ffprobe, mediainfo)
        if not res:
            LOG.warning(f"Could not determine resolution for {entry.name}. Leaving it in place.")
            failed += 1
            continue

        width, height = res
        LOG.info(f"{entry.name} resolution detected as {width}x{height}")

        if is_hd(width, height):
            LOG.info(f"{entry.name} meets HD rule height>768 or width>=1080. Leaving it in place.")
            skipped += 1
            continue

        if (width == 720 and height == 480) or (width == 480 and height == 720):
            LOG.info(f"{entry.name} is exactly 720x480 which is explicitly treated as DVD.")

        try:
            move_file(entry, dvd_dir, dry_run=dry_run)
            moved += 1
        except Exception as e:
            LOG.exception(f"Failed to move {entry.name}: {e}")
            failed += 1

    LOG.info("Scan complete")
    LOG.info(f"Summary for folder: {folder}")
    LOG.info(f"  Total MKV files seen: {total}")
    LOG.info(f"  Moved to DVD:         {moved}")
    LOG.info(f"  Left in place:        {skipped}")
    LOG.info(f"  Failed or unknown:    {failed}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Move non HD MKV files to a DVD subfolder.")
    parser.add_argument("--path", type=str, default=".", help="Folder to process. Default is current folder.")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without moving files.")
    args = parser.parse_args()

    configure_logging(very_verbose=True)

    folder = Path(args.path).resolve()
    if not folder.exists() or not folder.is_dir():
        LOG.error(f"Path is not a folder or does not exist: {folder}")
        sys.exit(1)

    scan_folder(folder, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
