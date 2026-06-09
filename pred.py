import cv2
from ultralytics import YOLO
path=cv2.imread('/Users/amritanshushiwanshi/Downloads/Pothole_detection-main/data/train/images/224.jpg')
model=YOLO('/Users/amritanshushiwanshi/Downloads/Pothole_detection-main/runs/detect/train10/weights/last.pt')
load=model(path)
result=load[0].plot()
cv2.imshow('frame',result)
cv2.waitKey(0)


