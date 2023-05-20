import cv2

cap = cv2.VideoCapture('http://192.168.65.74:4747/video')
tracker = cv2.legacy.TrackerKCF_create()
#commit

success, img = cap.read()
bbox = cv2.selectROI("Tracking", img, False)
tracker.init(img, bbox)

def draw(img, bbox):
    x, y, w, h = [int(v) for v in bbox]
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

while True:
    timer = cv2.getTickCount()
    success, img = cap.read()

    success, bbox = tracker.update(img)

    if success:
        draw(img, bbox)
    else:
        cv2.putText(img, 'Lost!',(75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img, str(int(fps)),(75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    cv2.imshow('Tracking', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break