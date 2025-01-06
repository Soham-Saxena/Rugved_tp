import cv2
import numpy as np

vid = cv2.VideoCapture("Ball_tracking.mp4")

while vid.isOpened():
    ret, frame = vid.read()
    if not ret:
        break
    lower_range = np.array([40, 40, 40])
    upper_range = np.array([80, 255, 255])
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    masked_image = cv2.inRange(frame_hsv, lower_range, upper_range)
    contours, hierarchy = cv2.findContours(masked_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        x, y, width, height = cv2.boundingRect(max(contours, key=cv2.contourArea))
        cv2.circle(frame, (int(x+(width/2)),int(y+(height/2))), int((width+height)/4), (255,0,0),2)
    
    cv2.imshow("Ball Tracking",frame)

    if cv2.waitKey(10) & 0xFF == ord('e'):
        break

vid.release()
cv2.destroyAllWindows()
