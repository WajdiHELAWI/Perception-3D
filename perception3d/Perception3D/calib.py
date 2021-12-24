import cv2
import numpy as np
import matplotlib as plt
import Calibration as ca

monocalib = ca.MonoCalibration(cols=8, rows=5, patternSize_m=1.0, patternType='chessboard')
#monocalib.acquire(cameraId=0, startIndex=1)
monocalib.calibrate(framesPath = 'results/acquired')
monocalib.plotRMS()