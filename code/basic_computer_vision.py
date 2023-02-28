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


if __name__ == '__main__':
    test = DetectObject
