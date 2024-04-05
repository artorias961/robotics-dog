import cv2
import numpy as np

def apply_analog_filter_to_frame(frame):
    # Ensure the frame has 3 channels
    if len(frame.shape) != 3 or frame.shape[2] != 3:
        return frame

    # Apply a sepia effect
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    sepia_frame = cv2.transform(frame, kernel)

    # Add grain
    row, col, ch = sepia_frame.shape
    mean = 0
    var = 30
    sigma = var**0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch)).astype(np.uint8)
    sepia_frame = cv2.add(sepia_frame, gauss)

    # Apply vignette
    X_resultant_kernel = cv2.getGaussianKernel(col, 150)
    Y_resultant_kernel = cv2.getGaussianKernel(row, 150)
    resultant_kernel = Y_resultant_kernel * X_resultant_kernel.T
    mask = 255 * resultant_kernel / np.linalg.norm(resultant_kernel)
    vignette = np.dstack((mask, mask, mask))
    sepia_frame = sepia_frame * vignette / 255

    return sepia_frame

# Capture video from camera
cap = cv2.VideoCapture(0)

while True:
    # Read a new frame
    ret, frame = cap.read()
    if not ret:
        break

    # Apply the analog filter
    filtered_frame = apply_analog_filter_to_frame(frame)

    # Display the resulting frame
    cv2.imshow('Analog Filter Effect', filtered_frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
