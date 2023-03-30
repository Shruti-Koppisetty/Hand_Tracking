import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    results = hands.process(img)
    print(results.multi_hand_landmarks)

    cv2.imshow("Live Feed", img)
    cv2.waitKey(1)




