# Virtual Hand Gesture Keyboard

This project is a virtual keyboard that uses hand gestures to input text. It leverages **OpenCV** and **CVZone** to detect hand movements and detect key presses based on finger positioning. The keyboard layout is modeled after a standard QWERTY layout with added functionality for special keys such as Backspace, Enter, Tab, and Caps Lock.

## Features
- **Text Input**: Allows users to type letters and numbers with hand gestures.
- **Special Keys**: Includes Backspace (to delete the last character), Enter (to add a new line), Tab (to insert tab space), and Caps Lock (to toggle uppercase).
- **Pinch-to-click Gesture**: Pinch the thumb and index finger to select a key.
- **Fingertip Highlight**: The index finger's tip is highlighted to provide feedback on the detected finger position.
- **Dynamic Text Display**: Displays the typed text on the screen, supporting multi-line text input.

## Requirements
- Python 3.x
- OpenCV
- cvzone
- NumPy

You can install the necessary dependencies by running:

```bash
pip install opencv-python opencv-python-headless cvzone numpy
```
# How to Run
 - Clone this repository:
```bash
git clone https://github.com/your-username/virtual-hand-gesture-keyboard.git
cd virtual-hand-gesture-keyboard
```
  - Run the script:
```bash
python virtual_keyboard.py
```
  - Position your hand in front of the webcam and use pinch gestures (thumb + index finger) to type.


# Controls:
  1. Thumb + Index Finger Pinch: Confirm key press.
  2. Back Key: Deletes the last typed character.
  3. Enter Key: Adds a new line.
  4. Tab Key: Inserts a tab space.
  5. Caps Key: Toggles between uppercase and lowercase letters.


# License
This project is licensed under the MIT License - see the LICENSE file for details.


# Acknowledgements
OpenCV: Used for hand detection and gesture recognition.
CVZone: Provides the HandTrackingModule for easy integration of hand tracking.



---


