import cv2
import os, shutil, sys
from fastai.text import Path

root_dir = Path(f'/home/gaurav/Downloads/ISL')

for cls in (root_dir/'hackathon_data').ls():
    for vid_path in cls.ls():
        file_name = str(vid_path).replace(f'{root_dir}/hackathon_data/', '')
        print(file_name)

        output_path = f'{root_dir}/video_frames/{file_name}'

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # delete all files in output path
        for the_file in os.listdir(output_path):
            file_path = os.path.join(output_path, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)

        vidcap = cv2.VideoCapture(str(vid_path))

        def getFrame(sec):
            vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
            hasFrames,image = vidcap.read()
            if hasFrames:
                cv2.imwrite(f"{output_path}/image"+str(count)+".jpg", image)     # save frame as JPG file
            return hasFrames
        sec = 0
        frameRate = 0.1  # it will capture image in each 0.1 second
        count=1
        success = getFrame(sec)
        while success:
            count = count + 1
            sec = sec + frameRate
            sec = round(sec, 2)
            success = getFrame(sec)

        os.system(f'python pytorch-openpose/demo.py {file_name}')
