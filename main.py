import cv2
import cvzone
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

class Button():
    def __init__(self, pos, text, size=[70, 70]):
        self.pos = pos
        self.size = size
        self.text = text

buttonList = []

# Button sizing and spacing
key_height = 60
row_spacing = 10
col_spacing = 10
keyboard_margin_bottom = 40

# Calculate total keyboard height
keyboard_height = len(keys) * (key_height + row_spacing)

# Starting y to place keyboard from bottom
start_y = 720 - keyboard_height - keyboard_margin_bottom

for i, row in enumerate(keys):
    row_width = 0
    row_buttons = []

    # Calculate row width first
    for key in row:
        width = 70
        if key in ["Tab", "Caps", "Enter", "Back"]:
            width = 100
        elif key == "Space":
            width = 500
        row_width += width + col_spacing
    row_width -= col_spacing  # remove last spacing

    # Center x for this row
    start_x = (1280 - row_width) // 2

    # Add buttons in the row
    x_offset = start_x
    for key in row:
        width = 70
        if key in ["Tab", "Caps", "Enter", "Back"]:
            width = 100
        elif key == "Space":
            width = 500
        buttonList.append(Button([x_offset, start_y + i * (key_height + row_spacing)], key, [width, key_height]))
        x_offset += width + col_spacing

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size

        # Semi-transparent background
        overlay = img.copy()
        alpha = 0.3
        cv2.rectangle(overlay, (x, y), (x + w, y + h), (255, 255, 255), -1)
        cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

        # Rounded white border
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2, cv2.LINE_AA)

        # Centered text
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size = cv2.getTextSize(button.text, font, 0.8, 2)[0]
        text_x = x + (w - text_size[0]) // 2
        text_y = y + (h + text_size[1]) // 2
        cv2.putText(img, button.text, (text_x, text_y), font, 0.8, (0, 0, 0), 2)
    return img

while True:
    success, img = cap.read()
    if not success:
        break

    hands, img = detector.findHands(img)
    img = drawAll(img, buttonList)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
