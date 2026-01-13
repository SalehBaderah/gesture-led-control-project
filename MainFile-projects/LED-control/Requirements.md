##  Requirements

###  Software
- **Python**  
  - `opencv-python` (for video capture & image processing)  
  - `mediapipe` (for hand detection & tracking)  
  - `pyfirmata2` (for communication with Arduino)  

- **Arduino IDE**  
  - `StandardFirmata` sketch for serial communication  

---

###  Hardware
- Arduino Uno
- Breadboard
- LED
- 220Ω Resistor
-  wires (for connections)



##  Project Files

- `gesture-led-control.py` — Python script for gesture detection & LED control
- `Mediapipe_landmarks.md` — Mediapipe Landmarks indexes
---

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

 ![Image](https://github.com/user-attachments/assets/32e70806-d949-49ed-829a-e71a7d886b21))

4. **Run the script:**
   ```bash
   python gesture-led-control.py

  ---

##  Preview

![Image](https://github.com/user-attachments/assets/ce57934d-8b1e-4431-aee5-08b7da787283)


---
