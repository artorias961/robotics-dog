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

        # Resizing
        self.x_resize = None
        self.y_resize = None
        self.scale_percent = 60
        self.resize_image = np.ndarray

        # Histogram Setup
        self.image_width = int
        self.image_height = int
        self.b_channel = np.ndarray
        self.g_channel = np.ndarray
        self.r_channel = np.ndarray

        # Histogram Image
        self.histo_image = np.ndarray
        self.bin_width = int
        self.histo_size = int
        self.b_histo = np.ndarray
        self.g_histo = np.ndarray
        self.r_histo = np.ndarray

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
        # self.image = cv2.imread(r"..\image_folder\artyGRB.png")
        # self.image = cv2.imread(r"..\image_folder\131_255_69_98_149_255_255_10_197.png")
        # self.image = cv2.imread(r"..\image_folder\test_blue.png")

    def image_information(self):
        """
        Getting the information of an image

        :return: the height and width of the given image
        """
        # Getting the height, width, and total channels
        self.image_height, self.image_width, _ = self.image.shape

        # Creating the size of the histogram
        self.histo_size = 256

        # Creating an evenly window section
        self.bin_width = int(round(self.image_width / self.histo_size))

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
        """
        Gets the binary values of the image

        :return: a threshold image
        """
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

    def histogram_calculation(self):
        """
        Splits the image into three channels then proceed to calculate the histograms

        :return: calculated histogram
        """
        # Splitting the image into 3 variables into one
        bgr_image = cv2.split(self.image)

        # Creating the range of the histogram (the upper is exclusive)
        histo_range = (0, 256)

        # To gather the image
        accumulate_logic = False

        # Splitting the BGR channels into their own variable
        self.b_channel = cv2.calcHist(bgr_image, [0], None, [self.histo_size], histo_range, accumulate_logic)
        self.g_channel = cv2.calcHist(bgr_image, [1], None, [self.histo_size], histo_range, accumulate_logic)
        self.r_channel = cv2.calcHist(bgr_image, [2], None, [self.histo_size], histo_range, accumulate_logic)

    def histogram_normalization(self):
        """
        To draw the histogram, the data needs to be normalized so its values fall in the range indicated by
        the parameters entered


        :return: normalize dataset
        """
        # Normalize the dataset
        self.b_histo = cv2.normalize(self.b_channel, self.b_channel, alpha=0, beta=self.image_height,
                                     norm_type=cv2.NORM_MINMAX)
        self.g_histo = cv2.normalize(self.g_channel, self.g_channel, alpha=0, beta=self.image_height,
                                     norm_type=cv2.NORM_MINMAX)
        self.r_histo = cv2.normalize(self.r_channel, self.r_channel, alpha=0, beta=self.image_height,
                                     norm_type=cv2.NORM_MINMAX)

    def create_histogram_image(self):
        # Create an empty image
        self.histo_image = np.zeros((self.image_height, self.image_width, 3), dtype=np.uint8)

        # Creating a for loop to iterate every intensity value of BGR
        for index in range(1, self.histo_size):
            # Create a line for BLUE
            self.histo_image = cv2.line(self.histo_image,
                                        (self.bin_width * (index - 1),
                                         self.image_height - int(self.b_histo[index - 1])),
                                        (self.bin_width * index,
                                         self.image_height - int(self.b_histo[index])),
                                        (255, 0, 0),
                                        thickness=2)

            # Create a line for GREEN
            self.histo_image = cv2.line(self.histo_image,
                                        (self.bin_width * (index - 1),
                                         self.image_height - int(self.g_histo[index - 1])),
                                        (self.bin_width * index,
                                         self.image_height - int(self.g_histo[index])),
                                        (0, 255, 0),
                                        thickness=2)

            # Create a line for RED
            self.histo_image = cv2.line(self.histo_image,
                                        (self.bin_width * (index - 1),
                                         self.image_height - int(self.r_histo[index - 1])),
                                        (self.bin_width * index,
                                         self.image_height - int(self.r_histo[index])),
                                        (0, 0, 255),
                                        thickness=2)

    def resize(self):
        """
        Resizes the image

        :return: resize image
        """
        # Getting the new width and new height
        new_width = int(self.image_height * self.scale_percent / 100)
        new_height = int(self.image_height * self.scale_percent / 100)

        # Getting the dimension of the image
        dim = (new_width, new_height)

        # Resized image
        self.resize_image = cv2.resize(self.histo_image, dim, interpolation=cv2.INTER_AREA)

    def load_image(self):
        """
        Displays an image

        :return: N/A
        """
        # Load the image
        cv2.imshow("A Image", self.resize_image)
        cv2.waitKey(0)

    def main(self):
        # General
        self.find_directory()
        self.image_information()
        self.convert_color_format()
        self.thresholding()

        # Find Histogram
        self.histogram_calculation()
        self.histogram_normalization()
        self.create_histogram_image()

        # For Gray
        self.histogram_equalization()

        # Load Image
        self.resize()
        self.load_image()


if __name__ == '__main__':
    cd = ColorDetection()
    cd.main()
