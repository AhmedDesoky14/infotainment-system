import cv2
import torch
from ultralytics import YOLO

class CarAlarmSystem:
    def __init__(self, model_path='yolov8n.pt'):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = YOLO(model_path).to(self.device)
        self.alarm_status = False
        self.relevant_signs = {'stop sign', 'speed limit', 'traffic light', 'street sign', 'flag', 'pedestrian crossing'}

    def detect_signs(self, frame):
        resized_frame = cv2.resize(frame, (224, 224))  # Further reduce resolution
        results = self.model(resized_frame, device=self.device, verbose=False)

        scale_x = frame.shape[1] / resized_frame.shape[1]
        scale_y = frame.shape[0] / resized_frame.shape[0]

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
                    self.alarm_status = True
                    return 1
                
                
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        return frame, self.alarm_status

    def trigger_alarm(self):
        if self.alarm_status:
            print("ALARM: Relevant Traffic Sign Detected!")
            self.alarm_status = False


def main():
    car_alarm = CarAlarmSystem()
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    cap.set(cv2.CAP_PROP_FPS, 15)

    frame_counter = 0
    skip_frames = 5  # Process every 5th frame for better performance

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = car_alarm.detect_signs(frame)
        if result == 1:
            print("Relevant street sign detected! Returning 1.")
        else:
            print("none")
        cv2.imshow('Car Alarm System', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()