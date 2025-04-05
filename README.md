# wildlife-Surveillance
AI Powered classification and detection drone

**Project Title: AI-Powered Wildlife Surveillance Drone**

---

**Objective:**
To build an autonomous drone system using a Raspberry Pi, AI-based animal detection, and GPS logging to monitor and document wildlife activity in forests or conservation zones.

---

**Key Features:**
- Animal detection using YOLOv5 on Raspberry Pi camera feed
- Real-time GPS logging using Pixhawk flight controller
- Autonomous waypoint-based missions
- Logging of sightings with location, timestamp, and confidence
- Optional cloud sync and alert system

---

**Hardware Required:**
- Raspberry Pi 4 (4GB or 8GB)
- Pi Camera V2 or USB webcam
- Pixhawk Flight Controller
- GPS Module (e.g., u-blox NEO-M8N)
- ESCs + Brushless Motors + Drone Frame + LiPo Battery
- SD Card (32GB+)
- Wi-Fi dongle or 4G USB modem (for remote access or cloud sync)

---

**Software Stack:**
- OS: Raspberry Pi OS (Lite or Full)
- Programming Language: Python
- AI Model: YOLOv5 (custom or pretrained)
- Libraries: OpenCV, DroneKit, Torch, NumPy, CSV
- Ground Control: QGroundControl

---

**System Architecture:**
1. Raspberry Pi captures video feed and performs animal detection.
2. When detection occurs, logs GPS (from Pixhawk), timestamp, label, and confidence.
3. Image snapshots are saved locally.
4. Pixhawk executes autonomous flight missions.

---

**Steps to Build:**

1. **Hardware Integration:**
   - Mount Raspberry Pi and camera on drone.
   - Connect Pi to Pixhawk via UART (/dev/ttyAMA0).
   - Calibrate ESCs, GPS, accelerometer via QGroundControl.

2. **Install Software:**
   ```bash
   sudo apt update && sudo apt install python3-pip git
   git clone https://github.com/ultralytics/yolov5
   cd yolov5 && pip install -r requirements.txt
   pip install dronekit opencv-python
   ```



*Maintained by: Saurabh J*

