import cv2
from cvzone.HandTrackingModule import HandDetector
import time

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width of the frame
cap.set(4, 720)   # Set height of the frame

# Initialize hand detector (only 1 hand)
detector = HandDetector(detectionCon=0.8, maxHands=1)

last_capture_time = 0  # Last time a photo was taken
photo_counter = 1      # Counter for saved image filenames

while True:
    # Read a frame from the webcam
    cam_status, img = cap.read()

    # Detect hand(s) and get landmark information
    hands, img = detector.findHands(img)  # Draw=True by default

    if hands:
        # Work only with the first detected hand
        hand = hands[0]
        lmList = hand['lmList']  # Get list of 21 landmark points

        # Thumb tip = landmark 4, Index finger tip = landmark 8
        thumb_tip = lmList[4]
        index_tip = lmList[8]

        # Calculate distance between thumb tip and index tip
        # We use only (x, y) positions here
        length, info, img = detector.findDistance(thumb_tip[:2], index_tip[:2], img)

        # If the distance is less than threshold (like pinching gesture)
        if length < 40:

            if time.time() - last_capture_time > 2:
                filename = f"photo_{photo_counter}.jpg"
                cv2.imwrite(filename, img)  # Save the image
                print(f"📸 Photo Captured: {filename}")
                photo_counter += 1
                last_capture_time = time.time()  # Reset capture time

    # Display the webcam feed
    cv2.imshow("Touch to Capture", img)

    # Break loop if 'q' is pressed
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release camera and close all windows
cap.release()
cv2.destroyAllWindows()
