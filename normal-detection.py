import cv2
import numpy as np

new_dimensions = (400, 400)

class Circledetector:
    def __init__(self, picture, minRadius):
        self.picture = picture
        self.minRadius = minRadius

    def detectCircles(self):
        # MainAlgorithm
        img         = self.picture.copy()
        output      = self.picture.copy()
        resized_img = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_AREA)
        img_gray    = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur    = cv2.GaussianBlur(img_gray, (5, 5), 0)

        circles = cv2.HoughCircles(
            img_blur,
            cv2.HOUGH_GRADIENT,
            dp=1,
            minDist=100,
            param1=100,
            param2=40,
            minRadius=60,
            maxRadius=1000
        )

        if circles is not None:
            circles = np.uint16(np.around(circles))
            x, y, r = circles[0][0]
            cv2.circle(output, (x, y), r, (0, 255, 0), 2)
            cv2.circle(output, (x, y), 2, (0, 0, 255), 3)

        return output

def main():
    image = cv2.imread("3.jpg")
    rudi = Circledetector(image, 60).detectCircles()
    cv2.imshow('Detected Circle', rudi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()
