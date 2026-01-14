import cv2
import numpy as np

#setting up needed dimensions for proper classification
new_dimensions = (400, 400)

#Class that could be further reused for finding circles logic
class Circledetector:
    def __init__(self, picture, minRadius):
        self.picture = picture
        self.minRadius = minRadius
    # main method resposible for detection of the circles.
    def detectCircles(self):
        #image transformations
        img         = self.picture.copy()
        output      = self.picture.copy()
        resized_img = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_AREA)
        img_gray    = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur    = cv2.GaussianBlur(img_gray, (9, 9), 0)

        #circle detection logic
        circles = cv2.HoughCircles(
            img_blur,
            cv2.HOUGH_GRADIENT,
            dp=4,
            minDist=100,
            param1=250,
            param2=80,
            minRadius=60,
            maxRadius=1000
        )
        # Graphing results on the image
        if circles is not None:
            circles = np.uint16(np.around(circles))
            x, y, r = circles[0][0]
            cv2.circle(output, (x, y), r, (0, 255, 0), 3)
            cv2.circle(output, (x, y), 2, (0, 0, 255), 3)

        return output # image that is returned

# testing class
def main():
    image = cv2.imread("3.jpg")
    detected_img = Circledetector(image, 60).detectCircles() # detection of the circle
    cv2.imshow('Detected Circle', detected_img) #showing detected frames
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#calling main function
main()

#Pseudocode
# LOADING IMG -> CONVERT to GRAY -> BLUR -> CIRCLE DETECTION (HoughCircles) -> GRAPH CIRCLES -> SHOWING OUTPUT RESULT

