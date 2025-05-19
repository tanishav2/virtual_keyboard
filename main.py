import cv2
import cvzone
import time
from cvzone.HandTrackingModule import HandDetector

# Webcam setup
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand detector
detector = HandDetector(detectionCon=0.8)
caps = False

# Keyboard layout
keys = [
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Back"],
    ["Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["Caps", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Enter"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
    ["Space"]
]

# Button class with press detection
class Button():
    def __init__(self, pos, text, size=[70, 70]):
        self.pos = pos
        self.size = size
        self.text = text
        self.lastPressed = 0
        self.isActive = False  # for highlight

    def isPressed(self, fingerPos, delay=0.5):
        x, y = self.pos
        w, h = self.size
        fx, fy = fingerPos

        if x < fx < x + w and y < fy < y + h:
            currentTime = time.time()
            if currentTime - self.lastPressed > delay:
                self.lastPressed = currentTime
                self.isActive = True
        else:
            self.isActive = False

buttonList = []

# Button sizing and spacing
key_height = 60
row_spacing = 10
col_spacing = 10
keyboard_margin_bottom = 40

keyboard_height = len(keys) * (key_height + row_spacing)
start_y = 720 - keyboard_height - keyboard_margin_bottom

# Create all buttons
for i, row in enumerate(keys):
    row_width = 0

    for key in row:
        width = 70
        if key in ["Tab", "Caps", "Enter", "Back"]:
            width = 100
        elif key == "Space":
            width = 500
        row_width += width + col_spacing
    row_width -= col_spacing

    start_x = (1280 - row_width) // 2
    x_offset = start_x

    for key in row:
        width = 70
        if key in ["Tab", "Caps", "Enter", "Back"]:
            width = 100
        elif key == "Space":
            width = 500
        buttonList.append(Button([x_offset, start_y + i * (key_height + row_spacing)], key, [width, key_height]))
        x_offset += width + col_spacing

# Draw all keys
def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size

        overlay = img.copy()
        alpha = 0.3
        color = (0, 255, 0) if button.isActive else (255, 255, 255)
        cv2.rectangle(overlay, (x, y), (x + w, y + h), color, -1)
        cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

        # Border
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2, cv2.LINE_AA)

        # Centered text
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size = cv2.getTextSize(button.text, font, 0.8, 2)[0]
        text_x = x + (w - text_size[0]) // 2
        text_y = y + (h + text_size[1]) // 2
        cv2.putText(img, button.text, (text_x, text_y), font, 0.8, (0, 0, 0), 2)
    return img

# Main loop
while True:
    success, img = cap.read()
    if not success:
        break

    hands, img = detector.findHands(img)

    if hands:
        lmList = hands[0]["lmList"]
        if lmList:
            index_finger_tip = lmList[8][:2]  # (x, y)
            for button in buttonList:
                button.isPressed(index_finger_tip)  # just sets active state if hovered long enough

    img = drawAll(img, buttonList)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
