import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-v', '--video', help='Path to video')
ap.add_argument('--face', required=True, help='Path to HaarCascade XML file')
args = vars(ap.parse_args())

face_cascade = cv2.CascadeClassifier(args["face"])
if(args["video"]):
    cap = cv2.VideoCapture(args["video"])
else:
    cap = cv2.VideoCapture(0)
    
while cap.isOpened():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    total_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)

    print("No. of faces present {}".format(len(total_faces)))
    for (x,y,w,h) in total_faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    
    cv2.putText(frame, "No. of faces "+str(len(total_faces)),(50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Face_detector", frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
