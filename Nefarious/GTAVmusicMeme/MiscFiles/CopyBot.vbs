Set oShell = CreateObject("WScript.Shell")
strHomeFolder = oShell.ExpandEnvironmentStrings("%USERPROFILE%")
mainDirec = strHomeFolder&"\Documents\Rockstar Games\GTA V\"

Dim objFSO
Set objFSO = CreateObject("Scripting.FileSystemObject")
Dim CurrentDirectory
CurrentDirectory = objFSO.GetAbsolutePathName(".")

songFile = CurrentDirectory&"\MiscFiles\Song.mp3 "

randNum = Rnd

specificName = mainDirec&"song"&randNum&".mp3"

' MsgBox(songFile)

Dim FSO
Set FSO = CreateObject("Scripting.FileSystemObject")
FSO.CopyFile songFile, SpecificName
