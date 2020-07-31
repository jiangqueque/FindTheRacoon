#!/usr/bin/env python
# coding: utf-8

import argparse
import cv2
import datetime
import os
import shutil
import sys

# Open and parse the video file
def parse(path):
    step = 10
    for filename in os.listdir(path):
        if filename.endswith(".mov") or filename.endswith(".MOV"):
            sub_path = path + os.path.splitext(filename)[0]
            if os.path.exists(sub_path) and os.path.isdir(sub_path):
                shutil.rmtree(sub_path)
            os.mkdir(sub_path)
            print(os.path.join(path, filename))
            video = cv2.VideoCapture(path + filename)
            fps = video.get(cv2.CAP_PROP_FPS)
            i = 0
            while(video.isOpened()):
                ret, frame = video.read()
                if ret == False:
                    break
                if i % step == 0:
                    image = cv2.rotate(frame, cv2.ROTATE_180)
                    os.chdir(sub_path)
                    t_sec = int(i / fps)
                    t_conversion = datetime.timedelta(seconds=t_sec)
                    cv2.imwrite(os.path.splitext(filename)[0] + '_time_' + str(t_conversion)
                        + '_frame_' + str(i) + '.jpg', image)
                i += 1            
            video.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, default=os.getcwd() + '/data/',
        help='The path of input data')

    args = parser.parse_args()
    path = str(args.input)
    print("Data path is: " + path)
    parse(path)
