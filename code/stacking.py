import cv2
import numpy as np


def stack_images(scale, image_array):
    """
    This is legit copy and paste from a youtube video. Pretty much think of subplots but that actually works
    :param scale: how much to scale the image (vertical/Horizontal)
    :param image_array: An image
    :return: a subplot of images
    """
    # Getting the length of the row and column
    rows = len(image_array)
    cols = len(image_array[0])

    # Checking if there is any empty space in the row
    rows_available = isinstance(image_array[0], list)

    # Getting the shape size
    width = image_array[0][0].shape[1]
    height = image_array[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, cols):
                if image_array[x][y].shape[:2] == image_array[0][0].shape[:2]:
                    image_array[x][y] = cv2.resize(image_array[x][y], (0, 0), None, scale, scale)
                else:
                    image_array[x][y] = cv2.resize(image_array[x][y], (image_array[0][0].shape[1], image_array[0][0].shape[0]),
                                                   None, scale, scale)
                if len(image_array[x][y].shape) == 2: image_array[x][y] = cv2.cvtColor(image_array[x][y], cv2.COLOR_GRAY2BGR)
        image_blank = np.zeros((height, width, 3), np.uint8)
        hor = [image_blank] * rows
        hor_con = [image_blank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(image_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if image_array[x].shape[:2] == image_array[0].shape[:2]:
                image_array[x] = cv2.resize(image_array[x], (0, 0), None, scale, scale)
            else:
                image_array[x] = cv2.resize(image_array[x], (image_array[0].shape[1], image_array[0].shape[0]), None, scale, scale)
            if len(image_array[x].shape) == 2: image_array[x] = cv2.cvtColor(image_array[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(image_array)
        ver = hor
    return ver