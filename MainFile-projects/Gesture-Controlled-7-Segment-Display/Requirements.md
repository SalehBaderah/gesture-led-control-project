##  Requirements
###  Software
- **Python**  
  - `opencv-python` (for video capture & image processing)  
  - `mediapipe` (for hand detection & tracking)  
  - `pyfirmata2` (for communication with Arduino)
  - `math` (for frame display) optional

- **Arduino IDE**  
  - `StandardFirmata` sketch for serial communication  

---

###  Hardware
- Arduino Uno
- Breadboard
- 7-segment display
- 220Ω Resistor
-  wires (for connections)

##  Project Files

- `7-segment.py` — Main Python script 
- `7-segment_test.py` — Python script (without the arduino for testing)
- `Mediapipe_landmarks.md` - Mediapipe landmarks and 7-segments digits

##  Setup Instructions

1. **On Arduino IDE:**
   - Open the IDE
   - Go to: `File > Examples > Firmata > StandardFirmata`
   - Upload it to your Arduino Uno

2. **On Python:**
   - Install the required libraries:
     ```bash
     pip install opencv-python mediapipe pyfirmata2
     ```

3. **Connect the hardware** as shown below:
<img src="https://github.com/user-attachments/assets/c22b0967-fbf5-4fac-b4c3-8d38fcfe9a74" width="400">
<img src="https://github.com/user-attachments/assets/bb6977a0-7c11-49cd-aff6-9d2ef26cb529" width="400">


4. **Run the script:**
   ```bash
   python 7-segment.py

  ---
  ##  Preview

![Image](https://github.com/user-attachments/assets/c0602c65-b421-477e-a9b2-aac2c1655cab)



