import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Initialize MediaPipe solutions
mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands
pose = mp_pose.Pose()
hands = mp_hands.Hands()

# Initialize video capture
cap = cv2.VideoCapture(0)

def process_frame(frame):
    # Convert frame to RGB (MediaPipe requirement)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Apply threshold
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    # People detection with Pose
    results_pose = pose.process(frame_rgb)
    if results_pose.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(
            frame, results_pose.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Hand/arm segmentation with Hands
    results_hands = hands.process(frame_rgb)
    if results_hands.multi_hand_landmarks:
        for hand_landmarks in results_hands.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    return frame, thresholded

def update(_):
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        return

    frame, thresholded = process_frame(frame)

    # Update plots
    imgs[0].set_data(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    imgs[1].set_data(thresholded)
    # To update with results from Pose and Hands, modify here

fig, axs = plt.subplots(2, 2)
imgs = [axs[i][j].imshow(np.zeros((480, 640, 3), dtype=np.uint8)) for i in range(2) for j in range(2)]

ani = FuncAnimation(fig, update, interval=50)

plt.show()

cap.release()
cv2.destroyAllWindows()
