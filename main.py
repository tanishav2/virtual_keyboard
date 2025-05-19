import cv2
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text
    def draw(self,img):
        x,y = self.pos
        w,h = self.size
        cv2.rectangle(img, self.pos, (x+w, y+h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, self.text, (x + 20, y + 65),cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
        return img


myButton = Button([100, 100], "Q")
myButton1 = Button([195, 100], "W")
myButton2 = Button([290, 100], "E")

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # returns list of hands and the modified image

    if hands:
        hand = hands[0]  # get the first detected hand
        lmList = hand["lmList"]  # list of 21 landmarks
        bbox = hand["bbox"]  # bounding box (x, y, w, h)
        centerPoint = hand["center"]  # center of the hand (cx, cy)
        handType = hand["type"]  # "Left" or "Right"

    img = myButton.draw(img)
    img = myButton1.draw(img)
    img = myButton2.draw(img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)