import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize webcam
cam = cv2.VideoCapture(0)

# Initialize the Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    # Read a frame from the webcam
    cam_status, image = cam.read()

    # Detect hands
    hands, image = detector.findHands(image)  # with draw=True by default

    # Display the output
    cv2.imshow("Hand Detection", image)
    
    # Waits for 1 millisecond for a key press
    key = cv2.waitKey(1)

    # Press 'q' to quit
    if key == ord('q'):
        break

# Cleanup
cam.release()
cv2.destroyAllWindows()
