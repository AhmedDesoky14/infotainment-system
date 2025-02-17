import cv2
import numpy as np
import face_recognition
import os
import logging
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, Signal, QMutex
from typing import Optional, List, Tuple
from captured_images import CapturedImages
import time

class User_account(QThread):
    # Signal to update the GUI with the processed frame
    update_frame_signal = Signal(QPixmap)

    def __init__(self, camera_index: int = 0, scale_factor: float = 0.25, fps: int = 50):
        super().__init__()
        self.camera_index = camera_index
        self.scale_factor = scale_factor
        self.fps = fps
        self.cap = None
        self.mutex = QMutex()

        # Initialize captured images
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_file_path = os.path.join(script_dir, "captured_images_data.py")
        self.captured_images = CapturedImages(data_file_path)

        # Initialize logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def _draw_face_info(self, img: np.ndarray, face_loc: Tuple[int, int, int, int], name: str, color: Tuple[int, int, int]):
        """
        Draws a rectangle around the face and displays the name.
        """
        y1, x2, y2, x1 = [i * 4 for i in face_loc]  # Scale up the face location
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), color, cv2.FILLED)
        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    def _capture_and_process_frame(self) -> Optional[Tuple[np.ndarray, List[Tuple[int, int, int, int]], List[np.ndarray]]]:
        """
        Capture a frame from the camera and process it to detect faces.
        """
        success, img = self.cap.read()
        if not success:
            self.logger.error("Failed to capture image.")
            return None

        img_small = cv2.resize(img, (0, 0), None, self.scale_factor, self.scale_factor)
        img_small_rgb = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(img_small_rgb)
        face_encodings = face_recognition.face_encodings(img_small_rgb, face_locations)

        return img, face_locations, face_encodings

    def add_user_by_photo_name(self, user_name: str, timer_duration: int = 10) -> int:
        """
        Add a new user by capturing their photo and encoding their face.
        """
        self.mutex.lock()
        class_names, _ = self.captured_images.get_loaded_data()
        if user_name.lower() in [name.lower() for name in class_names]:
            self.logger.info(f"User '{user_name}' already exists.")
            self.mutex.unlock()
            return 0

        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            self.logger.error("Error: Could not open camera.")
            self.mutex.unlock()
            return 0

        start_time = time.time()

        try:
            while time.time() - start_time < timer_duration:
                result = self._capture_and_process_frame()
                if result is None:
                    continue
                elapsed_time = time.time() - start_time
                remaining_time = max(0, timer_duration - int(elapsed_time))
                img, face_locations, _ = result
                for face_loc in face_locations:
                    self._draw_face_info(img, face_loc, user_name, (0, 255, 0))

                cv2.putText(img, f"be ready at: {remaining_time}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.imshow('Add User', img)
                cv2.waitKey(1)

            result = self._capture_and_process_frame()
            if result is None:
                return 0

            img, face_locations, face_encodings = result


            if len(face_locations) != 1:
                self.logger.warning("Invalid number of faces detected. Please ensure only one face is visible.")
                return 0

            if face_encodings:
                self.captured_images.add_image(user_name.lower(), face_encodings[0].tolist())
                self.logger.info(f"User '{user_name}' added successfully.")
                return 1
            else:
                self.logger.warning("No face detected.")
                return 0

        finally:
            self.cap.release()
            cv2.destroyAllWindows()
            self.mutex.unlock()

    def remove_user(self, user_name: str) -> int:
        """
        Remove a user from the stored data.
        """
        self.mutex.lock()
        success = self.captured_images.remove_image(user_name)
        self.mutex.unlock()
        
        if success:
            self.logger.info(f"User '{user_name}' removed successfully.")
            return 1
        else:
            self.logger.warning(f"User '{user_name}' not found.")
            return 0

    # def _convert_cv_to_pixmap(self, img: np.ndarray) -> QPixmap:
    #     """
    #     Convert an OpenCV image to a QPixmap for display in a PySide6 label.
    #     """
    #     h, w, ch = img.shape
    #     bytes_per_line = ch * w
    #     q_img = QImage(img.data, w, h, bytes_per_line, QImage.Format_BGR888)
    #     return QPixmap.fromImage(q_img)
