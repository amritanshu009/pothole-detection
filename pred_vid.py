from ultralytics import YOLO
import cv2
import time

# Load video
cap = cv2.VideoCapture('/Users/amritanshushiwanshi/Downloads/Pothole_detection-main/data/vid_test/istockphoto-875261436-640_adpp_is.mp4')
cap.set(3, 640)
cap.set(4, 480)

# Load model
model = YOLO('/Users/amritanshushiwanshi/Downloads/Pothole_detection-main/runs/detect/train10/weights/last.pt')

fps_list = []  # Store FPS values

while cap.isOpened():
    try:
        start_time = time.time()  # Start timing
        ret, frame = cap.read()
        if not ret:
            break
    except Exception as e:
        print(e)
        continue

    # Run YOLO detection
    results1 = model(frame)
    res_plotted1 = results1[0].plot()

    # Show video
    cv2.imshow("Detected Objects in Video", res_plotted1)

    # FPS calculation
    end_time = time.time()
    fps = 1 / (end_time - start_time)
    fps_list.append(fps)
    print(f"Current FPS: {fps:.2f}")

    if cv2.waitKey(1) == ord('q'):
        break

# Print average FPS
if fps_list:
    avg_fps = sum(fps_list) / len(fps_list)
    print(f"Average FPS: {avg_fps:.2f}")

cap.release()
cv2.destroyAllWindows()
