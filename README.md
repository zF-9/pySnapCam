# pySnapCam
prototype of a (some-what) background webcam motion detection surveillance using Python.

## Concept ##
Normal webcam utilizing OpenCV Bayesian (probability) based foreground and background segmentation to detect motion.

 ## Project Requirements ##
    - Python 3.X.X 
    - OpenCV 
    - numpy

  ### Install Dependencies (Linux/Windows)
  ```
    pip install opencv-python
    pip install numpy 
  ```

## Workflow ##
By accessing a normal imaging HID and implementing opencv library, a normal web could be deploy as a local motion detector surveillance. webcam triggers recording session by motion, and if motion exceeds a specific frame number.
an image will be extracted from the video recording session. 

## Limitation ##
 ```
 - pre-processed data dependant on quality of webcam
 - requires good amount RAM for running openCV
```

## prospect ##
 ```
    1. confined space monitoring system
    2. low cost surveillance deployment option.
    3. physical desk / cubicle monitoring system.
    4. on prem visitor / customer counter
 ```

### Reading material 
[Basic motion detection and tracking with Python and OpenCV](https://pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/);
[Extract and Saving Frame from Videos in Python — Idiot Developer](https://nikhilroxtomar.medium.com/extract-and-saving-frame-from-videos-in-python-idiot-developer-207d38dfbda9);
[Reading and Writing Videos using OpenCV](https://opencv.org/blog/reading-and-writing-videos-using-opencv/).
