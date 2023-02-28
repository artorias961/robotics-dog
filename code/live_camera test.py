import cv2
import numpy as np
from stacking import stack_images


class LiveCamera:
    def __init__(self):
        self.video = None
        self.camera_detected = False
        self.frame = None

        # Applying filters/transformation
        self.grayscale_frame = np.ndarray
        self.hsv_frame = np.ndarray
        self.hsl_frame = np.ndarray

    def camera(self):
        # Defining the video capture object
        self.video = cv2.VideoCapture(0)

        # An infinite loop to keep the camera running
        while True:
            # Get the camera current update data/frame
            self.camera_detected, self.frame = self.video.read()

            # Show current frame
            cv2.imshow('Current Frame', self.frame)

            # Creating a conditional statement to quit the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Destroy all windows
        self.video.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # lc = LiveCamera
    # lc.camera()

    # define a video capture object
    vid = cv2.VideoCapture(0)

    while True:

        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        # Apply Grayscale, HSV, HSL, and CIE
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsl_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
        cie_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2Lab)

        # Stacking the images
        images = stack_images(0.7, ([gray_frame, hsv_frame], [hsl_frame, cie_frame]))

        # Display the resulting frame
        cv2.imshow('frame', images)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


