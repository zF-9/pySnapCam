import cv2
#webcam = cv2.VideoCapture(1) # Number which capture webcam in my machine
# try either VideoCapture(0) or (1) based on your camera availability
# in my desktop it works with (1)
#check, frame = webcam.read()
#cv2.imwrite(filename=r'saved_img.jpg', img=frame)
#webcam.release()

video = cv2.VideoCapture(0)

video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

video.set(cv2.CAP_PROP_FOURCC, 0x32595559)

video.set(cv2.CAP_PROP_FPS, 25)

if video.isOpened():
    current_frame = 0
    while True:
        ret, frame = video.read()
        if ret:
            name = f'frameIn/frame{current_frame}.jpg'
            print(f"Creating file... {name}")
            cv2.imwrite(name, frame)
            frame.append(name)
        current_frame += 1
    video.release()
cv2.destroyAllWindows()

