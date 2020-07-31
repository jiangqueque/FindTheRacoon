#!/usr/bin/env python
# coding: utf-8

import csv
import os

if __name__ == "__main__":
    data_path = os.getcwd() + '/data/'
    for subdir, dir, files in os.walk(data_path):
        if subdir != data_path + 'Video' :
            continue
        output = subdir + '_label.csv'
        with open(output, 'w') as output_f:
            csv_writer = csv.writer(output_f)
            for filename in files:
                if filename.endswith(".jpg") or filename.endswith(".JPG"):
                    data = []
                    items = filename.split('_')
                    i = 0
                    for item in items:
                        i += 1
                        if item == 'frame':
                            break
                    frame_index = int(items[i].split('.')[0])
                    if frame_index == 530 or frame_index == 540 or frame_index == 550:
                        data.append(filename)
                        data.append(0)
                        csv_writer.writerow(data)
                        data.clear()
                    elif frame_index < 90 or frame_index >= 790:
                        data.append(filename)
                        data.append(0)
                        csv_writer.writerow(data)
                        data.clear()
                    else:
                        data.append(filename)
                        data.append(1)
                        csv_writer.writerow(data)
                        data.clear()