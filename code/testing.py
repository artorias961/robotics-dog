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
        # General
        self.image = np.ndarray
        self.image_width = int
        self.image_height = int
        self.b_channel = np.ndarray
        self.g_channel = np.ndarray
        self.r_channel = np.ndarray

        # Histogram Image
        self.histo_image = np.ndarray

        # For Gray
        self.gray_image = np.ndarray
        self.thresh_gray_image = np.ndarray
        self.histo_gray_equalization = np.ndarray
        self.histo_gray_calculation = None

        # For HSV
        self.hsv_image = np.ndarray
        self.thresh_hsv_image = np.ndarray
        self.histo_hsv_calculation = None

        # For HSL
        self.hsl_image = np.ndarray
        self.thresh_hsl_image = np.ndarray
        self.histo_hsl_calculation = None

    def find_directory(self):
        """
        Finds the image from the given directory

        :return: an image
        """
        # Read the image from the given directory
        self.image = cv2.imread(r"..\image_folder\butterflies.jpg")

    def image_information(self):
        """
        Getting the information of an image

        :return: the height and width of the given image
        """
        # Getting the height, width, and total channels
        self.image_height, self.image_width, _ = self.image.shape

    def convert_color_format(self):
        """
        Color space conversion to HSL or HSV to identify a color since color information is defined by Hue, Saturation,
        and Value/Lightness Components

        :return: a converted image
        """
        # Converting the image to grayscale
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # Converting the image to HSV (Hue, Saturation, and Value)
        self.hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        # Converting the image to HSL (Hue, Saturation, and Lightness)
        self.hsl_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HLS)

    def thresholding(self):
        # Getting the threshold of gray image
        self.thresh_gray_image = cv2.threshold(self.gray_image, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

        # Getting the threshold of hsv image
        self.thresh_hsv_image = cv2.threshold(self.hsv_image, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

        # Getting the threshold of hsl image
        self.thresh_hsl_image = cv2.threshold(self.hsl_image, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

    def histogram_equalization(self):
        """
        Stretches out the intensity range to another distribution that is wider and more uniform of intensity values.
        Essentially, describes the image features (equalizes tge histogram of a grayscale image)

        :return:
        """
        # Normalize the brightness and increases the contrast of the image
        self.histo_gray_equalization = cv2.equalizeHist(self.gray_image)

    def split_bgr_image(self):
        # Splitting the image into 3 variables into one
        bgr_image = cv2.split(self.image)

        # Creating the size of the histogram
        histo_size = 256

        # Creating the range of the histogram (the upper is exclusive)
        histo_range = (0, 256)

        # To gather the image
        accumulate_logic = False

        # Splitting the BGR channels into their own variable
        self.b_channel = (bgr_image, [0], None, [histo_size], histo_range, accumulate_logic)
        self.g_channel = (bgr_image, [1], None, [histo_size], histo_range, accumulate_logic)
        self.r_channel = (bgr_image, [2], None, [histo_size], histo_range, accumulate_logic)

    def create_histogram_image(self):
        pass

    def histogram_calculation(self):
        """


        :return:
        """
        pass

    def load_image(self):
        """
        Displays an image

        :return: N/A
        """
        # Load the image
        cv2.imshow("A Image", self.histo_gray_equalization)
        cv2.waitKey(0)

    def main(self):
        # General
        self.find_directory()
        self.image_information()
        self.convert_color_format()
        self.thresholding()
        self.split_bgr_image()

        # For Gray
        self.histogram_equalization()

        # Load Image
        self.load_image()


if __name__ == '__main__':
    cd = ColorDetection()
    cd.main()
