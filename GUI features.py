import cv2
import numpy as np


# Image
img = cv2.imread('./opencv-tutorial/jp.png')

cv2.imshow("Output image: ", img)
k = cv2.waitKey(0)

if k==ord('s'):
    cv2.imwrite('starry_night.jpg', img)

Camera Video
cap = cv2.VideoCapture(0) # 0 or -1 for webcam and 2 for external camera
if not cap.isOpened():
    print("Cannot open camera!")
    exit()
while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame!")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image ", gray)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#Read Video from file
cap = cv2.VideoCapture('vid.mp4') # 0 or -1 for webcam and 2 for external camera
while cap.isOpened():
    ret, frame = cap.read()

    # if not ret:
    #     print("Can't receive frame!")
    #     break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame ", gray)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#Drawing functions or different shape
img = np.zeros((512,512,3), np.uint8)

img = cv2.line(img, (0,0), (511,511), (255,0,0), 5)
img = cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow("output", img)
cv2.waitKey(0)

#Mouse CLick
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()


def nothing(x):
    pass
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')
# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27: #ASCII value of esc
        break
    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
cv2.destroyAllWindows()