import cv2
import mediapipe as mp
import pyautogui as auto
cap=cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
du=mp.solutions.drawing_utils
screen_width,screen_height = auto.size()
index_y=0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame_height,frame_width,_= frame.shape
    rbg_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rbg_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hands in hands:
            du.draw_landmarks(frame,hands)
            landmarks=hands.landmark
            for id, landmarks in enumerate(landmarks):
                x=int(landmarks.x*frame_width)
                y=int(landmarks.y*frame_height)

                if id == 8:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    index_x=screen_width/frame_width*x
                    index_y=screen_height/frame_height*y

                    auto.moveTo(index_x,index_y)

                if id == 12:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    thumb_x=screen_width/frame_width*x
                    thumb_y=screen_height/frame_height*y
                    print('outside',abs(index_y-thumb_y))
                    if abs(index_y-thumb_y) <= 30:
                        auto.click()
                if id == 5:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    indexbottom_x = screen_width / frame_width * x
                    indexbottom_y = screen_height / frame_height * y
                    print('outside', abs(index_y - indexbottom_y))
                    if abs(index_y - indexbottom_y) <= 30:
                        auto.vscroll(-10)
                if id == 20:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    pinky_x = screen_width / frame_width * x
                    pinky_y = screen_height / frame_height * y
                    print('outside', abs(index_y - pinky_y))
                    if abs(index_y - pinky_y) <= 30:
                        auto.vscroll(10)
                if id == 4:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    thumb_x=screen_width/frame_width*x
                    thumb_y=screen_height/frame_height*y
                    if abs(index_y - thumb_y) <= 30:
                        auto.rightClick()
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)