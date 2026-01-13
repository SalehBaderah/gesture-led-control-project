# This version will print only the digits of open fingers in the terminal

import cv2
import time
import mediapipe as mp


width, height = 600, 400
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hand = mp_hands.Hands(max_num_hands=1)

end = 0

def is_finger_open(landmarks, tip, pip): # check the fingers except the thump is open or not
    return landmarks.landmark[tip].y < landmarks.landmark[pip].y

def thump_state(landmarks, tip, pip): # check the Thump is open or not
    return landmarks.landmark[tip].x < landmarks.landmark[pip].x

def display_digit(digit):
    digit_patterns = {
        0: ['a','b','c','d','e','f',' ',],
        1: [' ', 'b', 'c', ' ', ' ', ' ', ' '],
        2: ['a', 'b', 'g', 'e', 'd', ' ', ' '],
        3: ['a', 'b', 'g', 'c', 'd', ' ', ' '],
        4: ['f', 'b', 'g', 'c', ' ', ' ', ' '],
        5: ['a', 'f', 'g', 'c', 'd', ' ', ' ']
    }

    if digit in digit_patterns:
        segments_to_turn_on = digit_patterns[digit]
        
        for segment in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            
            print(segments_to_turn_on)
        
        for segment in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            if segment in segments_to_turn_on:
                
                print(segments_to_turn_on)
                

while True:
    success, img = cap.read()
    if success:
        RGB_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hand.process(RGB_frame)

        if result.multi_hand_landmarks:
            for landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, landmarks, mp_hands.HAND_CONNECTIONS)

                finger_states = []

                if thump_state(landmarks, 4, 3): # THUMP
                    finger_states.append(0)
                else:
                    finger_states.append(1)

                if is_finger_open(landmarks, 8, 6):
                    finger_states.append(1)
                else:
                    finger_states.append(0)

                if is_finger_open(landmarks, 12, 10):
                    finger_states.append(1)
                else:
                    finger_states.append(0)

                if is_finger_open(landmarks, 16, 14):
                    finger_states.append(1)
                else:
                    finger_states.append(0)

                if is_finger_open(landmarks, 20, 18):
                    finger_states.append(1)
                else:
                    finger_states.append(0)
                
                total_num = finger_states.count(1) # counter for open fingers

                #print(f"Total open fingers: {total_num}")

                if 0 <= total_num <= 5:
                    display_digit(total_num)
                else:
                    print("No LED for this count")

        start = time.time()
        fps = 1 / (start - end)
        end = start
        cv2.putText(img, f'FPS: {int(fps)}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5555, (255, 0, 0), 2)

        cv2.imshow("FRAME", img)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            break
    else:
        print("Failed to read frame")

cap.release()
cv2.destroyAllWindows()
