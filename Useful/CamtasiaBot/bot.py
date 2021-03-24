from converter import Converter
conv = Converter()

info = conv.probe('In/Test1.avi')

convert = conv.convert('In/Test1.avi', 'Out/Test1.mp4', {
    'format': 'mp4',
    'audio': {
        'codec': 'aac',
        'samplerate': 11025,
        'channels': 2
    },
    'video': {
        'codec': 'hevc',
        'width': 720,
        'height': 400,
        'fps': 25
    }})

for timecode in convert:
    print(f'\rConverting ({timecode:.2f}) ...')