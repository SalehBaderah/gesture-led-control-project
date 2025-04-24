import math
import cv2
import mediapipe as mp
import pyfirmata2

#Initialize Arduino board
board = pyfirmata2.Arduino('COM6')
ledPin = board.get_pin("d:6:o")  # (digital,pinNum,output)

#SETUP FOR WEBCAM CAPTURE
width , height  = 600 , 400  
cap = cv2.VideoCapture(0)  # default cam = 0

cap.set(3, width) # 3 for width
cap.set(4, height) # 4 for height


# Initialize mediapipe hand tracking
mp_hands = mp.solutions.hands  # Hand detecting and tracking
mp_drawing = mp.solutions.drawing_utils  # For drawing the landmarks
hand = mp_hands.Hands(max_num_hands=1)  # Initialize the hand tracking model


while True:
    success, frame = cap.read()  # Read the frame

    if success:
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB frame
        result = hand.process(RGB_frame)  # Process the frame for hand landmarks

        if result.multi_hand_landmarks:
            for landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

                thumb = landmarks.landmark[4] # Thump index
                indextip = landmarks.landmark[8] # Index tip

                # Calculate the  distance between the thumb and index tip
                dis = math.sqrt((thumb.x - indextip.x)**2 + (thumb.y - indextip.y)**2)
                print(f"Distance: {dis}")

        

                if dis < 0.1:  # Adjust this threshold as needed
                    ledPin.write(0)  # Turn OFF LED
                else:
                    ledPin.write(1)  # Turn ON LED   

        # Display the frame with landmarks
        cv2.imshow("FRAME", frame)

        # Exit the loop when the 'c' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('c'):
            break

    else:
        print('Failed to read frame')  # In case the frame didn't show
        break

cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows
