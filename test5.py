from PoseModule import PoseDetector
import cv2
import pafy

url='https://www.youtube.com/watch?v=VgIuqT9pPaY'
videoPafy = pafy.new(url)
best = videoPafy.getbest()
cap = cv2.VideoCapture(best.url)

# cap = cv2.VideoCapture(0)
detector = PoseDetector()
pcount =0
up=0
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
    if bboxInfo:
        center = bboxInfo["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

        if up==0 and lmList[19][2] <lmList[11][2] or lmList[20][2] <lmList[12][2]:
            up=1
        if up==1 and lmList[19][2] > lmList[11][2]:
            up=0
            pcount +=1
            print(pcount)
            
        # print(lmList)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()