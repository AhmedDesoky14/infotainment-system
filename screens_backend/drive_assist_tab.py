# drive_assist_tab.py
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
import screens
from b_hand_control import HandLandmarkDetector

class drive_assist_tab:
    def __init__(self):
        self.__collision_timer = QTimer()
        self.__collision_toggler = False
        self.hand_detector = None  # HandLandmarkDetector instance

    def set_frame(self):
        """Initialize the HandLandmarkDetector and start the camera feed."""
        try:
            # Initialize the HandLandmarkDetector
            self.hand_detector = HandLandmarkDetector(camera_index=0, label=screens.main_screen_ui.usercamera_view)
            self.hand_detector.start()  # Start the camera feed

            # Set up a timer to periodically check for commands
            self.command_timer = QTimer()
            self.command_timer.timeout.connect(self.update_direction_from_hand)
            self.command_timer.start(20)  # Check for commands every 100 ms
        except Exception as e:
            print(f"Error initializing camera: {e}")
            self.hand_detector = None

    def update_direction_from_hand(self):
        """Update the direction icons based on the detected hand command."""
        if self.hand_detector:
            command = self.hand_detector.return_dir()  # Get the detected command
            self.update_direction_icons(command)  # Update the direction icons

    def reset_usercamera(self):
        """Clear the camera view in the GUI."""
        
        if self.hand_detector:  # Check if hand_detector is initialized
            self.hand_detector.close_event()  # Stop the camera feed
            self.hand_detector = None  # Reset to None
        
        screens.main_screen_ui.usercamera_view.setPixmap(QPixmap())
        screens.main_screen_ui.usercamera_view.setStyleSheet("")  # Remove all styles

    """---
        Directions icons set and reset for driving assist tab
    ---"""

    def set_brakes(self):
        screens.main_screen_ui.warningx.setPixmap(QPixmap(u":/drive_assist/icons/drive_assist/brake.png"))

    def reset_brakes(self):
        screens.main_screen_ui.warningx.setPixmap(QPixmap())

    def set_right_direction(self):
        screens.main_screen_ui.right_icon.setPixmap(QPixmap(u":/drive_assist/icons/drive_assist/green_right.png"))

    def reset_right_direction(self):
        screens.main_screen_ui.right_icon.setPixmap(QPixmap())

    def set_left_direction(self):
        screens.main_screen_ui.left_icon.setPixmap(QPixmap(u":/drive_assist/icons/drive_assist/green_left.png"))

    def reset_left_direction(self):
        screens.main_screen_ui.left_icon.setPixmap(QPixmap())

    def set_forward_direction(self):
        screens.main_screen_ui.foreward_icon.setPixmap(QPixmap(u":/drive_assist/icons/drive_assist/greed_forward.png"))

    def reset_forward_direction(self):
        screens.main_screen_ui.foreward_icon.setPixmap(QPixmap())

    def set_backward_direction(self):
        screens.main_screen_ui.warningx.setPixmap(QPixmap(u":/drive_assist/icons/drive_assist/green_backward.png"))

    def reset_backward_direction(self):
        screens.main_screen_ui.warningx.setPixmap(QPixmap())

    def update_direction_icons(self, command):
        """
        Update the direction icons based on the detected command.
        """
        # Reset all icons first
        self.reset_brakes()
        self.reset_right_direction()
        self.reset_left_direction()
        self.reset_forward_direction()
        self.reset_backward_direction()

        # Activate only the corresponding icon
        if command == "left":
            self.set_left_direction()
        elif command == "right":
            self.set_right_direction()
        elif command == "forward":
            self.set_forward_direction()
        elif command == "backward":
            self.set_backward_direction()
        elif command == "stop":
            self.set_brakes()  # Stop command activates brakes