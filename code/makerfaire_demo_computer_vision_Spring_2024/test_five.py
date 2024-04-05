import cv2
import mediapipe as mp
import pygame
import numpy as np

# Initialize MediaPipe solutions
mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands
mp_face_detection = mp.solutions.face_detection
pose = mp_pose.Pose()
hands = mp_hands.Hands()
face_detection = mp_face_detection.FaceDetection()

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize Pygame
pygame.init()
screen_width, screen_height = 520 * 2, 360 * 2
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Independent Functions for Each Feature
def detect_pose(frame_rgb):
    results_pose = pose.process(frame_rgb)
    frame_pose = frame_rgb.copy()
    if results_pose.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(frame_pose, results_pose.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    return frame_pose

def classify_image(frame_rgb):
    results_faces = face_detection.process(frame_rgb)
    frame_faces = frame_rgb.copy()
    if results_faces.detections:
        for detection in results_faces.detections:
            mp.solutions.drawing_utils.draw_detection(frame_faces, detection)
    return frame_faces

def segment_image(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    return thresholded

def recognize_gesture(frame_rgb):
    results_hands = hands.process(frame_rgb)
    frame_hands = frame_rgb.copy()
    if results_hands.multi_hand_landmarks:
        for hand_landmarks in results_hands.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame_hands, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    return frame_hands

def process_frame(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame_pose = detect_pose(frame_rgb)
    frame_faces = classify_image(frame_rgb)
    thresholded = segment_image(frame)
    frame_hands = recognize_gesture(frame_rgb)

    # Convert frames back to BGR for consistent Pygame display
    frame_pose_bgr = cv2.cvtColor(frame_pose, cv2.COLOR_RGB2BGR)
    frame_faces_bgr = cv2.cvtColor(frame_faces, cv2.COLOR_RGB2BGR)
    frame_hands_bgr = cv2.cvtColor(frame_hands, cv2.COLOR_RGB2BGR)

    return frame, thresholded, frame_pose_bgr, frame_faces_bgr, frame_hands_bgr

def display_frame(surface, frame, x, y):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
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

    frame, thresholded, frame_pose, frame_faces, frame_hands = process_frame(frame)

    # Display the frames
    display_frame(screen, frame, 0, 0)              # Original
    display_frame(screen, thresholded, 520, 0)     # Segmented
    # display_frame(screen, frame_pose, 0, 360)      # Pose
    display_frame(screen, frame_faces, 0, 360)   # Faces (Image Classification)
    display_frame(screen, frame_hands, 520, 360)   # Hands (Gesture Recognition)

    pygame.display.flip()
    clock.tick(30)

cap.release()
pygame.quit()
