import cv2
from circle_detection import Circledetector # importing circle detection class

#main function
def main():
    video_path = "output_video.avi" # importing video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Video does not exist!")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Problem with reading the stream")
            break

        #circles detection
        detected_circles_frame = Circledetector(frame).detectCircles() #calling detection on each frame
        cv2.imshow('Rolling Coca-Cola', detected_circles_frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()
