#! /usr/bin/python3

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

import sys
import cv2 as cv
import numpy as np

def main():
    filename = 'smarties.png'
    src = cv.imread(filename, cv.IMREAD_COLOR)
    cv.imshow('origin image', src)
    if src is None:
        raise Exception("Failed to open source file")

    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=30)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            cv.circle(src, center, 1, (0, 100, 100), 3)
            radius = i[2]
            cv.circle(src, center, radius, (255, 0, 255), 3)

    cv.imshow("Detected circles", src)
    cv.waitKey(0)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log.exception(e)