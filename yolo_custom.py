from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training) before implementing this project

# Train the model with 2 GPUs
results = model.train(data='C:/Users/chara/OneDrive/Desktop/PROGRAMS/yolo/data.yaml', epochs=50, augment=True)