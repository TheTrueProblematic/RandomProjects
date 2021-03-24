import ffmpy
ff = ffmpy.FFmpeg(
inputs={'In/Test1.avi': None}, outputs={'Out/Test1.mp4': None}
)
ff.run()
