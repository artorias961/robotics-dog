import cv2
import mediapipe as mp
import pygame
import numpy as np

# Initialize MediaPipe solutions
mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands
pose = mp_pose.Pose()
hands = mp_hands.Hands()

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize Pygame
pygame.init()
screen_width, screen_height = 520 * 2, 360 * 2
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

def process_frame(frame):
    # Convert frame to RGB (MediaPipe requirement)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Threshold
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    # Create copies for different processing
    frame_pose = frame.copy()
    frame_hands = frame.copy()

    ###
    # MediaPipe processing
    ###
    
    # People detection with Pose
    results_pose = pose.process(frame_rgb)
    if results_pose.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(frame_pose, results_pose.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Hand/arm segmentation with Hands
    results_hands = hands.process(frame_rgb)
    if results_hands.multi_hand_landmarks:
        for hand_landmarks in results_hands.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame_hands, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    return frame, thresholded, frame_pose, frame_hands

def display_frame(surface, frame, x, y):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert frame to RGB
    frame = np.rot90(frame)  # Rotate frame
    frame = pygame.surfarray.make_surface(frame)  # Convert to Pygame surface
    screen.blit(frame, (x, y))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ret, frame = cap.read()
    if not ret:
        break

    frame, thresholded, frame_pose, frame_hands = process_frame(frame)

    # Display the frames
    display_frame(screen, frame, 0, 0)              # Top-left
    display_frame(screen, thresholded, 520, 0)     # Top-right
    display_frame(screen, frame_pose, 0, 360)           # Bottom-left
    display_frame(screen, frame_hands, 520, 360)   # Bottom-right

    pygame.display.flip()
    clock.tick(30)

cap.release()
pygame.quit()
