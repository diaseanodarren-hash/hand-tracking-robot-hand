# Hand-Tracking-Robot-Hand
A robotic hand controled via mediapipe's hand landmark tracking module

### Demo
[most recent photo here]

## What it does
The robotic hand can perform finger flexion and extension with 1 degree of freedom for each finger. It is controlled from a hand landmark tracking video module on a desktop.

## How it works
- Capture -- OpenCV gets frame from the webcam
- Landmark Detection -- Hand tracking module returns 21 xy coordinate pairs of hand-finger joints
- Scaling -- Distance between tip and base of fingers are scaled to a fixed distance in the hand (wrist to base of middle finger)
- Mapping -- Distance are mapped/clamped between the integers 0-255
- Communication -- The integers are sent to the microcontroller in the form of strings over serial (USB) at a fixed baudrate of 9600
- Decoding -- Microcontroller decodes the string into 5 integer values corresponding to each finger distance
- Actuation -- The 5 integer values are then used to drive servo motors so that it matches the position

## What I used
- Hardware: STM32 Nucelo Board, 5 servo motors, Jumper Wires, Breadboard, wooden sticks (Robotic Hand Sekelton)
- Software/libraries: Hand tracking module, STM32 CUBE IDE, VS Code

## Challenges & what I learned
-[challenges here]

## What I'd improve
-[improvements here]

## Acknowledgements
- [OpenCV](https://opencv.org/) — used for video capture and image processing
- [MediaPipe Hands](https://github.com/google-ai-edge/mediapipe) by Google — hand landmark detection
- Hand detection/tracking module structure adapted from the classic 
  MediaPipe + OpenCV `handDetector` tutorial pattern popularized by 
  Murtaza's Workshop ("30 Days of Computer Vision") and widely 
  reproduced in tutorials such as:
  (https://www.analyticsvidhya.com/blog/2021/07/building-a-hand-tracking-system-using-opencv/)
