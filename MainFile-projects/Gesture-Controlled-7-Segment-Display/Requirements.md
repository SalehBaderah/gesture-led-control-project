## 📦 Requirements
### 🖥️ Software
- **Python**  
  - `opencv-python` (for video capture & image processing)  
  - `mediapipe` (for hand detection & tracking)  
  - `pyfirmata2` (for communication with Arduino)
  - `math` (for frame display) optional

- **Arduino IDE**  
  - `StandardFirmata` sketch for serial communication  

---

### 🔌 Hardware
- Arduino Uno
- Breadboard
- 7-segment display
- 220Ω Resistor
-  wires (for connections)

## 📂 Project Files

- `7-segment.py` — Main Python script 
- `7-segment_test.py` — Python script (without the arduino for testing)
- `Mediapipe_landmarks.md` - Mediapipe landmarks and 7-segments digits

## ✅ Setup Instructions

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

![Image](https://github.com/user-attachments/assets/2c3912fe-8ebb-4c25-9d69-872ba55c9608)
![Image](https://github.com/user-attachments/assets/b6d4b3f2-4116-4083-ad71-c1a787ee5ae9)

4. **Run the script:**
   ```bash
   python 7-segment.py

  ---
  ## 🖼️ Preview

![Image](https://github.com/user-attachments/assets/c0602c65-b421-477e-a9b2-aac2c1655cab)



