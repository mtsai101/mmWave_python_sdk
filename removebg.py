import csv 
import numpy as np
import logging
import sys
logging.basicConfig(level=logging.DEBUG)
prev_frame = set(np.array([]))
with open("detected.csv",'r', ) as csvfile:
    rows = csv.reader(csvfile)
    headers = next(rows, None)
    for row in rows:
        cur_point_frame = np.vstack([
            np.array(row[1][1:-1].split(),dtype=float),
            np.array(row[2][1:-1].split(),dtype=float),
            np.array(row[3][1:-1].split(),dtype=float)
        ]).T
        cur_point_frame = cur_point_frame.round(decimals=2)
        cur_point_frame = set(map(tuple, cur_point_frame))
        bg = cur_point_frame.intersection(prev_frame)
        moving_obj = cur_point_frame - bg
        prev_frame = cur_point_frame
        


        
        
        
        

