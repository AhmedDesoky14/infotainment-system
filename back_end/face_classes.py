# main.py
import cv2
import numpy as np
import face_recognition
import time
import os
from captured_images import CapturedImages

# Get the directory of the main script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the data file
data_file_path = os.path.join(script_dir, "captured_images_data.py")

# Initialize the CapturedImages class
captured_images = CapturedImages(data_file_path)

class CameraOperations:
    def __init__(self, camera_path):
        self.camera_path = camera_path
        self.scale_factor = 0.25  # Configurable scaling factor
        self.font = cv2.FONT_HERSHEY_COMPLEX
        self.font_scale = 1
        self.font_thickness = 2

    def _draw_face_info(self, img, face_loc, name, color):
        """
        Helper method to draw rectangles and text for a detected face.
        """
        y1, x2, y2, x1 = face_loc
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4  # Scale back to original size

        # Draw rectangle around the face
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        # Draw filled rectangle for the name label
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), color, cv2.FILLED)
        # Put the name on the image
        cv2.putText(img, name, (x1 + 6, y2 - 6), self.font, self.font_scale, (255, 255, 255), self.font_thickness)

    def user_recognition(self, timer_duration=10):
        """
        Perform real-time face recognition using the webcam.
        Returns:
            1 if a recognized face is found.
            0 if no recognized face is found within the timer duration.
        """
        class_names, encode_list_known = captured_images.get_loaded_data()
        cap = cv2.VideoCapture(self.camera_path)

        if not cap.isOpened():
            print("Error: Could not open camera.")
            return 0

        start_time = time.time()
        recognized = 0

        try:
            while True:
                success, img = cap.read()
                if not success:
                    print("Error: Failed to capture image.")
                    break

                # Display the countdown timer
                elapsed_time = time.time() - start_time
                remaining_time = max(0, timer_duration - int(elapsed_time))
                cv2.putText(img, f"Time: {remaining_time}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                # Resize and convert the image for face recognition
                img_small = cv2.resize(img, (0, 0), None, self.scale_factor, self.scale_factor)
                img_small_rgb = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)

                # Detect faces in the current frame
                face_locations = face_recognition.face_locations(img_small_rgb)
                face_encodings = face_recognition.face_encodings(img_small_rgb, face_locations)

                for encode_face, face_loc in zip(face_encodings, face_locations):
                    # Compare the current face with known faces
                    matches = face_recognition.compare_faces(encode_list_known, encode_face)
                    face_distance = face_recognition.face_distance(encode_list_known, encode_face)
                    match_index = np.argmin(face_distance)

                    if matches[match_index]:
                        name = class_names[match_index]
                        color = (0, 255, 0)  # Green for recognized faces
                        recognized = 1
                    else:
                        name = "Unknown"
                        color = (0, 0, 255)  # Red for unknown faces

                    # Draw face information on the image
                    self._draw_face_info(img, face_loc, name, color)

                # Display the image
                cv2.imshow('Face Recognition', img)

                # Exit on 'q' key press or when the timer ends
                if cv2.waitKey(1) & 0xFF == ord('q') or elapsed_time >= timer_duration:
                    break

        finally:
            # Release the camera and close all OpenCV windows
            cap.release()
            cv2.destroyAllWindows()

        return recognized

    def add_user_by_photo_name(self, user_name, timer_duration=10):
        """
        Add a new user by capturing their photo and encoding their face.
        Returns:
            1 if the user is added successfully.
            0 if the user already exists or no face is detected.
        """
        class_names, _ = captured_images.get_loaded_data()
        if user_name.lower() in [name.lower() for name in class_names]:
            print(f"User '{user_name}' already exists.")
            return 0

        cap = cv2.VideoCapture(self.camera_path)
        if not cap.isOpened():
            print("Error: Could not open camera.")
            return 0

        start_time = time.time()

        try:
            while True:
                success, img = cap.read()
                if not success:
                    print("Error: Failed to capture image.")
                    break

                # Display the countdown timer
                elapsed_time = time.time() - start_time
                remaining_time = max(0, timer_duration - int(elapsed_time))
                cv2.putText(img, f"Time: {remaining_time}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                # Show the frame
                cv2.imshow('Add User', img)

                # Break the loop if the timer ends
                if elapsed_time >= timer_duration:
                    break

                # Exit on 'q' key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # Capture the image after the timer ends
            _, img = cap.read()

            # Encode the captured image
            img_small = cv2.resize(img, (0, 0), None, self.scale_factor, self.scale_factor)
            img_small_rgb = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(img_small_rgb)
            face_encodings = face_recognition.face_encodings(img_small_rgb, face_locations)

            # Save the encoded image and name permanently
            if face_encodings:
                captured_images.add_image(user_name.lower(), face_encodings[0].tolist())
                print(f"User '{user_name}' added successfully.")
                return 1
            else:
                print("No face detected.")
                return 0

        finally:
            # Release the camera and close all OpenCV windows
            cap.release()
            cv2.destroyAllWindows()

    def remove_user_by_name(self, user_name):
        """
        Remove a user by their name.
        Returns:
            1 if the user is removed successfully.
            0 if the user does not exist.
        """
        class_names, _ = captured_images.get_loaded_data()
        if user_name.lower() in [name.lower() for name in class_names]:
            captured_images.remove_image(user_name)
            print(f"User '{user_name}' removed successfully.")
            return 1
        else:
            print(f"User '{user_name}' not found.")
            return 0

