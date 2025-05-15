import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize the HandDetector
detector = HandDetector(maxHands=2, minTrackCon=0.8)

# Open the default webcam
cam = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    cam_status, img = cam.read()

    # Detect hands in the frame (returns list of hands and image with annotations)
    hands, img = detector.findHands(img, draw=False)

    # If hands are detected
    if hands:
        for hand in hands:

            # Get hand type ("Left" or "Right")
            hand_type = hand["type"]

            # Display hand type on screen
            if hand_type == "Left":
                cv2.putText(img, "Left", (900, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            elif hand_type == "Right":
                cv2.putText(img, "Right", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show the annotated webcam feed
    cv2.imshow("Live Camera", img)

    # Press 'q' to quit
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
