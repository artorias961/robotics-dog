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
        video = cv2.VideoCapture(0)

        # An infinite loop to keep the camera running
        while True:
            # Get the camera current update data/frame
            ret, frame = video.read()

            # Show current frame
            cv2.imshow('Current Frame', frame)

            # Creating a conditional statement to quit the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Destroy all windows
        video.release()
        cv2.destroyAllWindows()

    def main(self):
        # Runs the camera function
        self.camera()


if __name__ == "__main__":
    # lc = LiveCamera
    # lc.main()

    # define a video capture object
    vid = cv2.VideoCapture(0)

    # An infinite loop
    while True:

        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        # Apply Grayscale, HSV, HSL, and CIE
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsl_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
        cie_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2Lab)
        frame_canny = cv2.Canny(gray_frame, 50, 50)

        # Applying Gaussian Blur
        blur_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        # Getting the threshold
        frame_threshold_ret, frame_threshold = cv2.threshold(gray_frame, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

        # Find the contours
        contours, hierarchy = cv2.findContours(frame_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Draw contours
        frame_copy = frame
        draw_contours = cv2.drawContours(frame_copy, contours, -1, (0,255,0), 3)


        # Applying histogram
        hsv_frame_split = cv2.split(hsv_frame)
        hsl_frame_split = cv2.split(hsl_frame)
        histo_range = (0, 256)
        accumulate_logic = False
        frame_height, frame_width, _ = frame.shape
        histo_size = 256
        bin_width = int(round(frame_width / histo_size))

        # Split channels
        h_frame_hsv = cv2.calcHist(hsv_frame_split, [0], None, [histo_size], histo_range, accumulate_logic)
        s_frame_hsv = cv2.calcHist(hsv_frame_split, [1], None, [histo_size], histo_range, accumulate_logic)
        v_frame_hsv = cv2.calcHist(hsv_frame_split, [2], None, [histo_size], histo_range, accumulate_logic)
        h_frame_hsl = cv2.calcHist(hsl_frame_split, [0], None, [histo_size], histo_range, accumulate_logic)
        s_frame_hsl = cv2.calcHist(hsl_frame_split, [1], None, [histo_size], histo_range, accumulate_logic)
        l_frame_hsl = cv2.calcHist(hsl_frame_split, [2], None, [histo_size], histo_range, accumulate_logic)

        # Normalization
        h_histo_hsv = cv2.normalize(h_frame_hsv, h_frame_hsv, alpha=0, beta=frame_height, norm_type=cv2.NORM_MINMAX)
        s_histo_hsv = cv2.normalize(s_frame_hsv, s_frame_hsv, alpha=0, beta=frame_height, norm_type=cv2.NORM_MINMAX)
        v_histo_hsv = cv2.normalize(v_frame_hsv, v_frame_hsv, alpha=0, beta=frame_height, norm_type=cv2.NORM_MINMAX)
        h_histo_hsl = cv2.normalize(h_frame_hsl, h_frame_hsl, alpha=0, beta=frame_height, norm_type=cv2.NORM_MINMAX)
        s_histo_hsl = cv2.normalize(s_frame_hsl, s_frame_hsl, alpha=0, beta=frame_height, norm_type=cv2.NORM_MINMAX)
        l_histo_hsl = cv2.normalize(l_frame_hsl, l_frame_hsl, alpha=0, beta=frame_height, norm_type=cv2.NORM_MINMAX)

        # Black images
        blank_frame_one = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
        blank_frame_two = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

        # Apply color histogram
        for index in range(1, histo_size):
            # Create a line for HUE
            blank_frame_one = cv2.line(blank_frame_one,
                                       (bin_width * (index - 1),
                                        frame_height - int(h_histo_hsv[index - 1])),
                                       (bin_width * index,
                                        frame_height - int(h_histo_hsv[index])),
                                       (255, 0, 0),
                                       thickness=2)

            # Create a line for SATURATION
            blank_frame_one = cv2.line(blank_frame_one,
                                       (bin_width * (index - 1),
                                        frame_height - int(s_histo_hsv[index - 1])),
                                       (bin_width * index,
                                        frame_height - int(s_histo_hsv[index])),
                                       (0, 255, 0),
                                       thickness=2)

            # Create a line for VALUE
            blank_frame_one = cv2.line(blank_frame_one,
                                       (bin_width * (index - 1),
                                        frame_height - int(v_histo_hsv[index - 1])),
                                       (bin_width * index,
                                        frame_height - int(v_histo_hsv[index])),
                                       (0, 0, 255),
                                       thickness=2)

            # Create a line for HUE
            blank_frame_two = cv2.line(blank_frame_two,
                                       (bin_width * (index - 1),
                                        frame_height - int(h_histo_hsl[index - 1])),
                                       (bin_width * index,
                                        frame_height - int(h_histo_hsl[index])),
                                       (255, 0, 0),
                                       thickness=2)

            # Create a line for SATURATION
            blank_frame_two = cv2.line(blank_frame_two,
                                       (bin_width * (index - 1),
                                        frame_height - int(s_histo_hsl[index - 1])),
                                       (bin_width * index,
                                        frame_height - int(s_histo_hsl[index])),
                                       (0, 255, 0),
                                       thickness=2)

            # Create a line for LIGHTNESS
            blank_frame_two = cv2.line(blank_frame_two,
                                       (bin_width * (index - 1),
                                        frame_height - int(l_histo_hsl[index - 1])),
                                       (bin_width * index,
                                        frame_height - int(l_histo_hsl[index])),
                                       (0, 0, 255),
                                       thickness=2)

        # Stacking the images
        images_one = stack_images(0.7, ([hsv_frame, blank_frame_one], [hsl_frame, blank_frame_two]))
        # images_two = stack_images(0.7, ([blank_frame_one], [blank_frame_two]))
        images = stack_images(0.7, ([frame, gray_frame], [hsv_frame, hsl_frame]))
        images_one = stack_images(0.7, ([hsv_frame, hsl_frame], [frame_threshold, frame_canny]))
        images_two = stack_images(0.7, ([frame, gray_frame], [blur_frame, draw_contours]))


        # Display the resulting frame
        # cv2.imshow('HSV (top) vs HSL (bottom)', blank_frame_two)
        cv2.imshow('HSV (top) vs HSL (bottom)', images_one)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
