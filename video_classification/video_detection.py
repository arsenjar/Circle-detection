import cv2
import numpy as np
from circle_detection import Circledetector

def main():
    video_path = "can_video.mp4"
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Video does not exist!")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Problem with reading the stream")
            break

        #circles detection
        rudi = Circledetector(frame).detectCircles()
        cv2.imshow('Rolling Coca-Cola', rudi)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()