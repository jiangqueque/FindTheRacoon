#!/usr/bin/env python
# coding: utf-8

import argparse
import cv2
import os
import sys

# Open and parse the video file
def parse(path):
    step = 10
    for filename in os.listdir(path):
        if filename.endswith(".mov") or filename.endswith(".MOV"):
            sub_path = path + os.path.splitext(filename)[0]
            os.mkdir(sub_path)
            print(os.path.join(path, filename))
            video = cv2.VideoCapture(path + filename)
            i = 0
            while(video.isOpened()):
                ret, frame = video.read()
                if ret == False:
                    break
                if i % step == 0:
                    image = cv2.rotate(frame, cv2.ROTATE_180)
                    os.chdir(sub_path)
                    cv2.imwrite(os.path.splitext(filename)[0] + '_Frame_' + str(i) + '.jpg', image)
                i += 1            
            video.release()
            cv2.destroyAllWindows()
        else:
            continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, default=os.getcwd() + '/data/',
        help='The path of input data')

    args = parser.parse_args()
    path = str(args.input)
    if (path == 'None'):
        print("[Error] Please set data path by -i or --input.")
        sys.exit(1)
    print("Data path is: " + path)
    parse(path)
