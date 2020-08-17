import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    # Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)
    
    # Do an invert binarize the image 
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow("mask_frame", mask)
    if (cv2.waitKey(1) & 0xff ) == 27:
        break

cap.release()
cv2.destroyAllWindows()