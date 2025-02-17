import cv2
import numpy as np
import face_recognition
import os
import logging
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer, QThread, Signal
from typing import Optional, List, Tuple
from captured_images import CapturedImages

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FaceRecognition(QThread):
    update_frame_signal = Signal(QImage)  # Signal to emit the processed frame

    def __init__(self, camera_index: int = 0, label=None, scale_factor: float = 0.25, fps: int = 50):
        super().__init__()
        self.camera_index = camera_index
        self.scale_factor = scale_factor
        self.fps = fps
        self.label = label
        self.recognized = False
        self.running = False

        # Initialize camera
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise ValueError("Error: Could not open camera.")

        # Initialize font attributes for drawing on the frame
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_scale = 1
        self.font_thickness = 2

        # Initialize captured images
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_file_path = os.path.join(script_dir, "captured_images_data.py")
        self.captured_images = CapturedImages(data_file_path)

    def _draw_face_info(self, img: np.ndarray, face_loc: Tuple[int, int, int, int], name: str, color: Tuple[int, int, int]):
        """
        Draws a rectangle around the face and displays the name.
        """
        y1, x2, y2, x1 = [i * 4 for i in face_loc]  # Scale up the face location
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), color, cv2.FILLED)
        cv2.putText(img, name, (x1 + 6, y2 - 6), self.font, self.font_scale, (255, 255, 255), self.font_thickness)

    def _process_frame(self, img: np.ndarray) -> np.ndarray:
        """
        Processes the frame for face recognition.
        """
        try:
            # Resize and convert the image for face recognition
            img_small = cv2.resize(img, (0, 0), None, self.scale_factor, self.scale_factor)
            img_small_rgb = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)

            # Detect face locations and encodings
            face_locations = face_recognition.face_locations(img_small_rgb)
            face_encodings = face_recognition.face_encodings(img_small_rgb, face_locations)

            # Get known face data
            class_names, encode_list_known = self.captured_images.get_loaded_data()

            # Process each detected face
            for encode_face, face_loc in zip(face_encodings, face_locations):
                matches = face_recognition.compare_faces(encode_list_known, encode_face)
                face_distance = face_recognition.face_distance(encode_list_known, encode_face)
                match_index = np.argmin(face_distance) if len(face_distance) > 0 else -1

                # Determine the name and color for the face
                if match_index != -1 and matches[match_index]:
                    name, color = class_names[match_index], (0, 255, 0)  # Green for recognized faces
                    self.recognized = True
                else:
                    name, color = "Unknown", (0, 0, 255)  # Red for unknown faces

                # Draw face info on the image
                self._draw_face_info(img, face_loc, name, color)

            return img

        except Exception as e:
            logger.error(f"Error during face recognition: {e}")
            return img

    def run(self):
        """
        Main loop for capturing and processing frames.
        """
        self.running = True
        while self.running:
            ret, img = self.cap.read()
            if not ret:
                logger.error("Error: Failed to capture image from camera.")
                break

            # Process the frame
            processed_img = self._process_frame(img)

            # Convert the image to QImage for display
            h, w, ch = processed_img.shape
            bytes_per_line = ch * w
            q_img = QImage(processed_img.data, w, h, bytes_per_line, QImage.Format.Format_BGR888)

            # Emit the processed frame
            self.update_frame_signal.emit(q_img)

            # Sleep to maintain the desired FPS
            self.msleep(1000 // self.fps)

    def stop(self):
        """
        Stops the camera feed and releases the camera.
        """
        self.running = False
        self.wait()  # Wait for the thread to finish
        self.cap.release()
        logger.info("Camera released and thread stopped.")

    def return_recognition_status(self) -> bool:
        """
        Returns the current recognition status.
        """
        return self.recognized