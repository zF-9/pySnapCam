import cv2 
from datetime import datetime
import numpy as np 

vids = 'output.avi' # video output
snaps = 'saved_img.png' # picture output

cap = cv2.VideoCapture(0) #adjust to webcam interface 
last_mean = 0 
now = datetime.now()
detected_motion = False 
frame_rec_count = 0 
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(vids, fourcc, 20.0, (640, 480))

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = np.abs(np.mean(gray) - last_mean)
    print(result)
    last_mean = np.mean(gray)

    print(result)

    if result > 0.3:
        print("motion detected")
        print("start recording")
        detected_motion = True

    if detected_motion:
        # Log time : motion detection
        f = now.strftime("%H:%M")
        print(f)

        # Start recording webcam
        out.write(frame)
        frame_rec_count = frame_rec_count+1

        # silent webcam snapshot 
        cv2.imwrite(filename = snaps, img = frame)

    # end prog using specific keystroke || video duration 
    if (cv2.waitKey(1) & 0xFF == ord('q') ):# or frame_rec_count == 240): 
        break 
 
        
cap.release()
cv2.destroyAllWindows()
    