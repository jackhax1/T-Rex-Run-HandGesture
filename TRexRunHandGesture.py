import cv2
import pyautogui

cap = cv2.VideoCapture(0) # openwebcam
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
palm_cascade = cv2.CascadeClassifier('aGest.xml')

while(True):
    ret, gray = cap.read() #ret = return value , frame = the picture
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY) #convert image to gray
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    #gray = cv2.flip(gray,1) # mirror the image

    faces = palm_cascade.detectMultiScale(gray, 1.3, 5) # x,y,w,h

    for (x,y,w,h) in faces:
        gray = cv2.rectangle(gray, (x, y), (x+w, y+h), (23, 199, 47), 2)
        pyautogui.press('space')

    cv2.imshow('frame',gray) #display picture


    if(cv2.waitKey(10) & 0xFF == 27): #wait 100ms and see the key is esc
        break

cap.release() #turn off webcam
cv2.destroyAllWindows() # close window
