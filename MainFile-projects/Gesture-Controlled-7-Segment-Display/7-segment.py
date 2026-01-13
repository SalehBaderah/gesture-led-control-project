import cv2
import time
import mediapipe as mp
import pyfirmata2


PORT = 'COM6'
board = pyfirmata2.Arduino(PORT)

print("Connected to Arduino...")

# Define Segment Pins
segments = {
    'a': board.get_pin("d:3:o"),
    'b': board.get_pin("d:2:o"),
    'c': board.get_pin("d:4:o"),
    'd': board.get_pin("d:5:o"),
    'e': board.get_pin("d:6:o"),
    'f': board.get_pin("d:7:o"),
    'g': board.get_pin("d:8:o")
}

# Video Setup
width, height = 1080, 1080
cap = cv2.VideoCapture(1)
cap.set(3, width)
cap.set(4, height)

# MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hand = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

end = 0




def is_finger_open(landmarks, tip, pip):

    return landmarks.landmark[tip].y < landmarks.landmark[pip].y


def is_thumb_open(landmarks, tip, pip, hand_label):


    thumb_tip_x = landmarks.landmark[tip].x
    thumb_ip_x = landmarks.landmark[pip].x

    if "Right" in hand_label:
        return thumb_tip_x < thumb_ip_x
    else:
        return thumb_tip_x > thumb_ip_x


def display_digit(digit):

    digit_patterns = {
        0: ['a', 'b', 'c', 'd', 'e', 'f'],
        1: ['b', 'c'],
        2: ['a', 'b', 'g', 'e', 'd'],
        3: ['a', 'b', 'g', 'c', 'd'],
        4: ['f', 'b', 'g', 'c'],
        5: ['a', 'f', 'g', 'c', 'd']
    }

    # If the digit is valid (0-5)
    if digit in digit_patterns:
        pattern = digit_patterns[digit]


        for char_id, pin in segments.items():
            if char_id in pattern:
                pin.write(1)  # Turn ON
            else:
                pin.write(0)  # Turn OFF
    else:

        for pin in segments.values():
            pin.write(0)




while True:
    success, img = cap.read()
    if not success:
        print("Failed to read frame")
        break


    RGB_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hand.process(RGB_frame)

    finger_count = 0

    if result.multi_hand_landmarks:

        hand_label = result.multi_handedness[0].classification[0].label

        for landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, landmarks, mp_hands.HAND_CONNECTIONS)

            # 1. Thump
            if is_thumb_open(landmarks, 4, 3, hand_label):
                finger_count += 1

            # 2. INDEX
            if is_finger_open(landmarks, 8, 6):
                finger_count += 1

            # 3. MIDDLE
            if is_finger_open(landmarks, 12, 10):
                finger_count += 1

            # 4. RING
            if is_finger_open(landmarks, 16, 14):
                finger_count += 1

            # 5. PINKY
            if is_finger_open(landmarks, 20, 18):
                finger_count += 1



            if finger_count > 5: finger_count = 5
            display_digit(finger_count)

    # FPS
    start = time.time()
    if (start - end) > 0:
        fps = 1 / (start - end)
    else:
        fps = 0
    end = start

    cv2.putText(img, f'FPS: {int(fps)}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('c'):
        break



for pin in segments.values():
    pin.write(0)

cap.release()
cv2.destroyAllWindows()
board.exit()
