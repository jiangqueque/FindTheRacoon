#!/usr/bin/env python
# coding: utf-8

import csv

if __name__ == "__main__":
    output = "/Users/jianyigao/Documents/Raccoon/FindTheRacoon/label.csv"
    with open(output, 'w') as output_f:
        csv_writer = csv.writer(output_f)
        data = []
        for i in range(0, 1800, 10):
            if i < 90 or i >= 790:
                data.append("Video_Frame_" + str(i) + ".jpg")
                data.append(0)
                csv_writer.writerow(data)
                data.clear()
            else:
                data.append("Video_Frame_" + str(i) + ".jpg")
                data.append(1)
                csv_writer.writerow(data)
                data.clear()
    