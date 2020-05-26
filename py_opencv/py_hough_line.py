"""
@file hough_lines.py
@brief This program demonstrates line finding with the Hough transform
"""

# Source url: https://docs.opencv.org/4.2.0/d9/db0/tutorial_hough_lines.html

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

import sys
import math
import cv2 as cv
import numpy as np

def main():
    filename = 'sudoku.png'
    src = cv.imread(filename, cv.IMREAD_GRAYSCALE)
    if src is None:
        raise Exception("Failed to load source file")

    dst = cv.Canny(src, 50, 200, None, 3)
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)

    cv.imshow("Origin image", src)
    cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    cv.waitKey()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log.exception(e)