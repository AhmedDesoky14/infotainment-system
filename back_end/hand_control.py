import cv2
import mediapipe as mp

class HandLandmarkDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils
        self.tip_ids = [4, 8, 12, 16, 20]  # Landmark IDs for finger tips
        self.cap = None
        self.running = False  # Flag to control the loop
        self.cap = cv2.VideoCapture(0)
        self.command = None

    def detect_finger_state(self, lm_list, fingers):
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
        if fingers == [1, 0, 0, 0, 0]:  # Thumb up
            return "left"
        elif fingers == [0, 0, 0, 0, 1]:  # Pinky up
            return "right"
        elif fingers == [1, 1, 1, 1, 1]:  # Index up
            return "forward"
        elif fingers == [0, 0, 0, 0, 0]:  # All fingers down
            return "stop"
        else:
            return "unknown"

    def hand_detection(self):
        success, img = self.cap.read()
        if not success:
            return 0
        
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        lm_list = []
        fingers = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_list.append([id, cx, cy])

                self.mp_draw.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                if len(lm_list) == 21:
                    fingers = self.detect_finger_state(lm_list, fingers)
                    self.command = self.analyze_fingers(fingers)
                    
                    
        else:
            fingers = [0, 0, 0, 0, 0]
            self.command = self.analyze_fingers(fingers)
            
            
            

        cv2.imshow("Hand Landmark Detection", img)
       
        # Exit loop on 'Esc' key press
        if cv2.waitKey(5) & 0xFF == 27:  
            self.stop_detection()

    def return_input_direction(self):
        return self.command

