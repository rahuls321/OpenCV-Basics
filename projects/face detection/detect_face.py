import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to image')
ap.add_argument('--face', required=True, help='Path to HaarCascade XML file')
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(args["face"])
total_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)

print("No. of faces present {}".format(len(total_faces)))
for (x,y,w,h) in total_faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Face_detector", img)
cv2.waitKey(0)

