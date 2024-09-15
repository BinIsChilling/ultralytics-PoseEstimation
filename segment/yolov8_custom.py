from ultralytics import YOLO

model = YOLO('yolov8m-pose.pt')

results = model(source="", show=True, conf=0.3, save=True)