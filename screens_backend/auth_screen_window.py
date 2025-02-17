from PySide6.QtCore import QTimer, QDateTime, QObject
from PySide6.QtGui import QPixmap
from enum import Enum
import screens
from face_classes import FaceRecognition
from PySide6.QtGui import QImage, QPixmap
import time
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TEXT_COLOR(Enum):
    RED = """QLabel { color: rgb(192, 28, 40); }"""
    YELLOW = """QLabel { color: rgb(246, 211, 45); }"""
    GREEN = """QLabel { color: rgb(38, 162, 105); }"""

class auth_screen_window(QObject):
    def __init__(self):
        super().__init__()
        self.__date_time_timer = QTimer()
        self.__date_time_timer.timeout.connect(self.__update_date_time)
        self.__date_time_timer.start(10)  # Update time every second

        self.authentication_flag = False  # Flag to track authentication state
        self.label=screens.authentication_screen_ui.auth_camera_label
        # Ensure UI components exist before accessing them
            
        # Initialize face recognition
        self.face_recognition = FaceRecognition(camera_index=0, label=screens.authentication_screen_ui.auth_camera_label)
        self.button = None
        # Timer for face recognition
        self.face_recognition.update_frame_signal.connect(self.update_frame)
        screens.authentication_screen_ui.auth_button.clicked.connect(self.__on_auth_button_click)
        self.button = False

    def __update_date_time(self):
        """Update the home page with current date and time."""
        current_date_time = QDateTime.currentDateTime()
        formatted_date = current_date_time.toString("MMM. dd, yyyy")
        screens.authentication_screen_ui.date_label.setText(f"Date: {formatted_date}")
        screens.authentication_screen_ui.time_label.setText(f"Time: {current_date_time.toString('hh:mm:ss')}")

    def __on_auth_button_click(self):
        """Handle authentication button click."""
        self.button = True


    def set_auth_text(self, text, color: TEXT_COLOR):
        """Set text and color for the authentication label."""
        screens.authentication_screen_ui.auth_text_label.setText(text)
        screens.authentication_screen_ui.auth_text_label.setStyleSheet(color.value)

    def reset_auth_text(self):
        """Reset the authentication label text."""
        screens.authentication_screen_ui.auth_text_label.clear()
        screens.authentication_screen_ui.auth_text_label.setStyleSheet("")

    def set_frame_auth(self):
        """Initialize and start the face recognition process."""
        # Reset the recognition flag
        while not self.button:
            pass
        self.authentication_flag = False

        # Start the face recognition thread
        self.face_recognition.start()
        self.set_auth_text("Authentication Faild", TEXT_COLOR.RED)
        # Connect the update_frame_signal to a method that updates the UI
        self.face_recognition.update_frame_signal.connect(self.update_frame)

        # Wait for authentication to succeed
        while not self.authentication_flag:
            # Check the recognition status periodically
            self.authentication_flag = self.face_recognition.return_recognition_status()
            if self.authentication_flag:
                self.set_auth_text("Authentication Successful", TEXT_COLOR.GREEN)
                self.reset_usercamera()
                return True  # Exit only after successful authentication

            # Add a small delay to avoid busy-waiting
            time.sleep(0.1)  # Sleep for 100 milliseconds

    def update_frame(self, q_img: QImage):
        """
        Updates the UI with the processed frame.
        """
        if self.label:
            self.label.setPixmap(QPixmap.fromImage(q_img))

    def reset_usercamera(self):
        """Stop and clear the camera feed."""
        screens.authentication_screen_ui.auth_camera_label.clear()
        screens.authentication_screen_ui.auth_camera_label.setPixmap(QPixmap())
        self.face_recognition.stop()  # Stop the face recognition process
        
