import cv2
import time
import mediapipe as mp
import pyautogui as pag

#set window measurements
wCam, hCam = 640, 680
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)

#detect hand and draw coordinates
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

screen_width, screen_height = 1920, 1080

def map_coordinates(hand_x, hand_y):
    mapped_x = int(hand_x * screen_width)
    mapped_y = int(hand_y * screen_height)
    return mapped_x, mapped_y

#main while loop
while True:
    success, img = cap.read()                              #capturing video from webcam
    if not success:
        break                        
    # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)        #converting colors (optional)
    img = cv2.flip(img, 1)
    results = hands.process(img)
    multiLandMarks = results.multi_hand_landmarks          #detetct any hand in the video and stores it in result var. multiLandMarks shows the coordinates
    # print(multiLandMarks)

    if multiLandMarks:
        for hand_landmarks in multiLandMarks:
            mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)
            index_finger  = hand_landmarks.landmark[8]
            hand_x, hand_y = index_finger.x, index_finger.y
            screen_x, screen_y = map_coordinates(hand_x, hand_y)
            pag.moveTo(screen_x, screen_y)
        

        

      



    #video displaying
    cv2.imshow("image",img)
    cv2.setWindowProperty("image", cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(1)