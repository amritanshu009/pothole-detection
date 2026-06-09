# Pothole Detection using YOLOv8

## Project Overview

This project is a pothole detection system built using YOLOv8, a deep learning-based object detection model. The main goal of this project is to detect potholes from road images and videos automatically.

Pothole detection is useful for road safety, smart city monitoring, traffic management, and road maintenance systems. Instead of manually checking road conditions manually, this system can help identify pothole-affected areas using computer vision.

## Features

* Detects potholes from road images
* Supports pothole detection in videos
* Uses YOLOv8 for object detection
* Includes trained model weights
* Contains training results and evaluation graphs
* Provides separate Python scripts for image and video prediction

## Project Structure

```text
pothole-detection/
│
├── data/
│   ├── normal/
│   ├── potholes/
│   ├── train/
│   │   ├── images/
│   │   └── labels/
│   └── vid_test/
│
├── runs/
│   └── detect/
│       └── train10/
│           ├── weights/
│           │   ├── best.pt
│           │   └── last.pt
│           ├── confusion_matrix.png
│           ├── confusion_matrix_normalized.png
│           ├── F1_curve.png
│           ├── PR_curve.png
│           ├── P_curve.png
│           ├── R_curve.png
│           ├── results.csv
│           └── results.png
│
├── data.yaml
├── pred.py
├── pred_vid.py
├── yolo_custom.py
├── yolov8n.pt
├── README.md
└── .gitignore
```

## Technologies Used

* Python
* YOLOv8
* Ultralytics
* OpenCV
* PyTorch
* YAML

## Dataset

The dataset contains road images used for pothole detection. It includes normal road images, pothole images, training images, annotation labels, and test videos.

The annotations are stored in YOLO format, where each label file contains bounding box details for pothole detection.

## Model

This project uses YOLOv8 for object detection. YOLOv8 is suitable for real-time detection tasks because it provides good speed and accuracy.

The trained model weights are stored in:

```text
runs/detect/train10/weights/
```

The important trained weight files are:

```text
best.pt
last.pt
```

## Training Results

The training results are available inside:

```text
runs/detect/train10/
```

This folder includes:

* Confusion matrix
* Normalized confusion matrix
* Precision curve
* Recall curve
* F1 score curve
* Precision-Recall curve
* Training result graph
* Validation prediction images
* Trained model weights

## Installation

Clone the repository:

```bash
git clone https://github.com/amritanshu009/pothole-detection.git
cd pothole-detection
```

Install the required libraries:

```bash
pip install ultralytics opencv-python
```

## How to Run

### Run Image Detection

```bash
python pred.py
```

### Run Video Detection

```bash
python pred_vid.py
```

### Train the Custom YOLO Model

```bash
python yolo_custom.py
```

## Expected Output

The model detects potholes in images or videos and marks them using bounding boxes. The output helps visually identify potholes on road surfaces.

## Applications

* Road damage detection
* Smart city road monitoring
* Automated road inspection
* Vehicle safety systems
* Public infrastructure maintenance
* Traffic and transportation analysis

## Future Improvements

* Add real-time webcam pothole detection
* Improve the dataset with more road conditions
* Deploy the model using Flask or FastAPI
* Build a simple web interface for image and video upload
* Add GPS location tracking for detected potholes
* Train with larger YOLO models for better accuracy

## Author

**Amritanshu Shiwanshi**

GitHub: [amritanshu009](https://github.com/amritanshu009)
