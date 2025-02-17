import cv2
import torch
from ultralytics import YOLO
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap
import os

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Use a larger model (e.g., yolov8m.pt)
model_name = "yolov8m.pt"
model_path = os.path.join(current_directory, model_name)

class CarAlarmSystem:
    def __init__(self, camera_index=0, label=None, model_path=model_path):
        """
        Initialize the CarAlarmSystem.
        
        :param camera_index: Index of the camera (default is 0 for the default camera).
        :param label: QLabel to display the camera feed.
        :param model_path: Path to the YOLO model file.
        """
        self.camera_index = camera_index
        self.label = label
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = YOLO(model_path).to(self.device)
        self.alarm_status = False
        self.relevant_signs = {
            'stop sign', 'speed limit', 'traffic light', 'street sign', 'flag', 
            'pedestrian crossing', 'no-parking', 'turn left', 'turn right', 'uturn'
        }
        self.detected_objects = []
        self.frame_counter = 0

        # Initialize the camera
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise ValueError("Error: Could not open camera.")

        # Set up a timer to update the camera feed
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    def update_frame(self):
        """Update the camera feed and perform object detection."""
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Could not read frame.")
            return

        # Skip frames for better performance
        if self.frame_counter % 3 == 0:  # Process every 3rd frame
            # Perform object detection
            detected_frame, detected_objects = self.detect_signs(frame)
            self.detected_objects = detected_objects  # Store detected objects

            # Display the frame in the QLabel
            if self.label:
                self.display_frame(detected_frame)

        self.frame_counter += 1

    def detect_signs(self, frame):
        """
        Detect relevant signs in the frame.
        
        :param frame: The frame to process.
        :return: The processed frame and a list of detected objects.
        """
        # Increase resolution (e.g., 1280x720)
        resized_frame = cv2.resize(frame, (1280, 720))  # Higher resolution

        # Adjust confidence and IoU thresholds
        results = self.model(resized_frame, device=self.device, verbose=False, conf=0.6, iou=0.5)

        scale_x = frame.shape[1] / resized_frame.shape[1]
        scale_y = frame.shape[0] / resized_frame.shape[0]

        detected_objects = []

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                x1 = int(x1 * scale_x)
                y1 = int(y1 * scale_y)
                x2 = int(x2 * scale_x)
                y2 = int(y2 * scale_y)

                label = self.model.names[int(box.cls)]
                confidence = float(box.conf)

                if label in self.relevant_signs and confidence > 0.5:
                    detected_objects.append(label)
                    self.alarm_status = True

                # Draw bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        return frame, detected_objects

    def display_frame(self, frame):
        """Display the frame in the QLabel."""
        # Convert the frame to QImage
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format.Format_BGR888)

        # Convert QImage to QPixmap and display it in the QLabel
        self.label.setPixmap(QPixmap.fromImage(q_img))

    def get_detected_objects(self):
        """Return the list of detected objects."""
        return self.detected_objects

    def start(self):
        """Start the camera feed and object detection."""
        self.timer.start(20)  # Update every 20 ms (~50 FPS)

    def stop(self):
        """Stop the camera feed and object detection."""
        self.timer.stop()
        self.cap.release()

    def trigger_alarm(self):
        """Trigger an alarm if a relevant sign is detected."""
        if self.alarm_status:
            print("ALARM: Relevant Traffic Sign Detected!")
            self.alarm_status = False