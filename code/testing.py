import numpy as np
import cv2

class DetectObject:
    def __init__(self):
        self.is_camera_detected = False
        self.frame_image = list()
        self.grayscale_frame = list()
        self.gaussian_blur_frame = list()
        self.threshold_frame = list()
        self.contours = list()
        self.contours_area = list()
        self.big_contours = list()

    def find_camera(self):
        print(self.is_camera_detected)

    def apply_grayscale(self):
        # Creating a for loop for every image from the list
        for image in self.frame_image:
            # Apply grayscale to the image
            temp_image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)

            # Add it to the access variable
            self.grayscale_frame.append(temp_image)

    def apply_gaussian_blur(self):
        # Creating the kernel size of the blur
        kernel = 5, 5

        # Creating a for loop for every image from the list
        for image in self.grayscale_frame:
            # Apply gaussian blur
            temp_image = cv2.GaussianBlur(src=image, ksize=kernel)

            # Add it to the access variable
            self.gaussian_blur_frame.append(temp_image)

    def apply_threshold(self):  # TODO: Mess with threshold variables (adaptive gaussian thresholding)
        # Creating a for loop for every imag from the list
        for image in self.gaussian_blur_frame:
            # Apply threshold to the image
            temp_image = cv2.threshold(src=image, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

            # Add it to the access variable
            self.threshold_frame.append(temp_image)


class ColorDetection:
    def __init__(self):
        self.image = np.ndarray
        self.hsv_image = np.ndarray
        self.hsl_image = np.ndarray
        self.thresh_hsv_image = np.ndarray
        self.thresh_hsl_image = np.ndarray

    def find_directory(self):
        """
        Finds the image from the given directory

        :return: an image
        """
        # Read the image from the given directory
        self.image = cv2.imread(r"..\image_folder\butterflies.jpg")

    def convert_color_format(self):
        """
        Color space conversion to HSL or HSV to identfy a color since color information is define by Hue, Saturation,
        and Value/Lightness Components

        :return: a converted image
        """
        # Converting the image to HSV (Hue, Saturation, and Value)
        self.hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        # Converting the image to HSL (Hue, Saturation, and Lightness)
        self.hsl_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HLS)

    def thresholding(self):
        # Getting the threshold of hsv image
        self.thresh_hsv_image = cv2.threshhold(self.image, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

        # Getting the threshold of hsl image
        self.thresh_hsl_image = cv2.threshhold(self.image, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

    def get_histrogram(self):
        pass

    def load_image(self):
        """
        Displays an image

        :return: N/A
        """
        # Load the image
        cv2.imshow("A Image", self.hsv_image)
        cv2.waitKey(0)

    def main(self):
        self.find_directory()
        self.convert_color_format()
        #self.thresholding()
        self.load_image()


if __name__ == '__main__':
    cd = ColorDetection()
    cd.main()

