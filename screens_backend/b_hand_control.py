# hand_landmark_detector.py
import cv2
import mediapipe as mp
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer

class HandLandmarkDetector:
    def __init__(self, camera_index=0, label=None):
        """
        Initialize the hand landmark detector.
        :param camera_index: Index of the camera (default is 0 for the default camera).
        :param label: QLabel to display the camera feed.
        """
        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils
        self.tip_ids = [4, 8, 12, 16, 20]  # Landmark IDs for finger tips

        # Initialize the camera
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise ValueError("Error: Could not open camera.")

        # Initialize the QLabel for displaying the camera feed
        self.label = label
        if self.label:
            self.label.setScaledContents(True)  # Scale the image to fit the label

        # Set up a timer to update the camera feed
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        # Initialize command state
        self.command = None

    def detect_finger_state(self, lm_list, fingers):
        """
        Detect the state of each finger (extended or not).
        :param lm_list: List of landmark positions.
        :param fingers: List to store the state of each finger.
        :return: Updated list of finger states.
        """
        # Thumb (compare x-coordinates)
        if lm_list[self.tip_ids[0]][1] < lm_list[self.tip_ids[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # Other fingers (compare y-coordinates)
        for tip in range(1, 5):
            if lm_list[self.tip_ids[tip]][2] < lm_list[self.tip_ids[tip] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

    def analyze_fingers(self, fingers):
        """
        Analyze the finger states to determine the command.
        :param fingers: List of finger states.
        :return: The detected command.
        """
        if fingers == [1, 0, 0, 0, 0]:  # Thumb up
            return "left"
        elif fingers == [0, 0, 0, 0, 1]:  # Pinky up
            return "right"
        elif fingers == [1, 1, 1, 1, 1]:  # All fingers up
            return "forward"
        elif fingers == [0, 0, 0, 0, 0]:  # All fingers down
            return "stop"
        elif fingers == [0, 1, 0, 0, 0]:  # Index up
            return "backward"
        else:
            return "unknown"

    def update_frame(self):
        """
        Update the camera feed and perform hand landmark detection.
        """
        try:
            # Read a frame from the camera
            ret, frame = self.cap.read()
            if not ret:
                raise ValueError("Error: Could not read frame.")

            # Flip the frame horizontally for a mirror effect
            frame = cv2.flip(frame, 1)

            # Convert the frame to RGB format (MediaPipe requires RGB)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame with MediaPipe Hands
            results = self.hands.process(frame_rgb)
            lm_list = []
            fingers = []

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw landmarks on the frame
                    self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                    # Extract landmark positions
                    for id, lm in enumerate(hand_landmarks.landmark):
                        h, w, c = frame.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lm_list.append([id, cx, cy])

                    # Detect finger states and analyze the command
                    if len(lm_list) == 21:
                        fingers = self.detect_finger_state(lm_list, fingers)
                        self.command = self.analyze_fingers(fingers)
            else:
                # No hands detected
                fingers = [0, 0, 0, 0, 0]
                self.command = self.analyze_fingers(fingers)

            # Display the command on the frame
            cv2.putText(frame, f"The car's state is : {self.command}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # Convert the frame to QImage
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format.Format_BGR888)

            # Convert QImage to QPixmap and display it in the QLabel
            if self.label:
                self.label.setPixmap(QPixmap.fromImage(q_img))
            
        except Exception as e:
            print(f"Error: {e}")

    def close_event(self):
        """
        Release the camera when the window is closed.
        """
        self.cap.release()

    def start(self):
        """
        Start the camera feed.
        """
        self.timer.start(20)  # Update every 20 ms (50 FPS)

    def stop(self):
        """
        Stop the camera feed.
        """
        self.timer.stop()
        self.close_event()

    def return_dir(self):
        return self.command