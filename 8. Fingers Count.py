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
    hands, img = detector.findHands(img, draw=True)

    total_fingers = 0  # Total fingers shown by all hands

    # If hands are detected
    if hands:
        for hand in hands:
            # Count which fingers are up (returns list of 0s and 1s for 5 fingers)
            fingerscount = detector.fingersUp(hand)

            # Add to total finger count
            total_fingers += sum(fingerscount)

    # 🟪 Display the total finger count on the screen
    cv2.putText(img, f"Fingers: {total_fingers}", (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    # Show the annotated webcam feed
    cv2.imshow("Live Camera", img)

    # Press 'q' to quit
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
