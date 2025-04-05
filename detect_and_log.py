import torch
import cv2
from dronekit import connect
from datetime import datetime
import csv
import os

vehicle = connect('/dev/ttyAMA0', baud=57600, wait_ready=True)

model = torch.hub.load('yolov5', 'yolov5s', source='local')
target_classes = ['person', 'dog', 'cat', 'bird', 'horse', 'elephant', 'zebra']
model.conf = 0.5

cap = cv2.VideoCapture(0)

os.makedirs("runs", exist_ok=True)
if not os.path.exists("sightings_log.csv"):
    with open("sightings_log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "Latitude", "Longitude", "Detection", "Confidence"])

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        results = model(frame)

        for *box, conf, cls in results.xyxy[0]:
            label = model.names[int(cls)]
            if label in target_classes:
                timestamp = datetime.now().isoformat()
                lat = vehicle.location.global_frame.lat
                lon = vehicle.location.global_frame.lon

                filename = f"runs/{timestamp}_{label}.jpg"
                cv2.imwrite(filename, frame)

                with open("sightings_log.csv", "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([timestamp, lat, lon, label, float(conf)])
except KeyboardInterrupt:
    print("Interrupted by user")

cap.release()
vehicle.close()
