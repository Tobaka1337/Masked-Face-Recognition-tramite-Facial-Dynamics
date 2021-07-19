import os

dirs = os.listdir()
for d in dirs:
    os.chdir(d)
    videos = os.listdir()
    for v in videos:
        os.chdir(v)
        frames = os.listdir()
        for frame in frames:
            tail = frame[-8:]
            if tail[0] == '_':
                head = frame[:-7]
                tail = frame[-7:]
                new_name = head+"0"+tail
                os.rename(frame, new_name)
        os.chdir("..")
    os.chdir("..")
