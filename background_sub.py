import cv2

cap = cv2.VideoCapture('vid.mp4')
i=0
while True:

    # frame = cv2.imread('./frames/frame-'+str(i)+'.jpg')
    _, frame = cap.read()
    if _ is False:
        print("Ret is false")
        exit()
    backSub = cv2.createBackgroundSubtractorKNN()
    fgmask = backSub.apply(frame)

    cv2.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv2.putText(frame, str(cap.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
               cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    


    cv2.imshow("frame", frame)
    cv2.imshow("frame", fgmask)
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break
    
    # cv2.imwrite('./frames/frame-'+str(i)+'.jpg',frame)
    i=i+1
cap.release()
cv2.destroyAllWindows()
