## 📦 Requirements

### 🖥️ Software
- **Python**  
  - `opencv-python` (for video capture & image processing)  
  - `mediapipe` (for hand detection & tracking)  
  - `pyfirmata2` (for communication with Arduino)  

- **Arduino IDE**  
  - `StandardFirmata` sketch for serial communication  

---

### 🔌 Hardware
- Arduino Uno
- Breadboard
- LED
- 220Ω Resistor
- Jumper wires (for connections)

---

## 🖼️ Preview

![Preview](MainFile-project/images/prev.gif)


---

## 📂 Project Files

- `gesture-led-control.py` — Python script for gesture detection & LED control
- `images/Circuit-diagram.png` — Circuit layout
- `images/prev.gif` — Project demo preview

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

   ![Circuit Diagram](MainFile-project/images/Circuit-diagram.png)

4. **Run the script:**
   ```bash
   python gesture-led-control.py
