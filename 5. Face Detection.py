import cv2
from cvzone.FaceDetectionModule import FaceDetector

# Initialize webcam
cam = cv2.VideoCapture(0)

# Initialize FaceDetector with minDetectionCon = 0.75
detector = FaceDetector(minDetectionCon=0.75)

while True:
    # Read a frame from the webcam
    cam_status, image = cam.read()

    # Detect faces
    image, bboxs = detector.findFaces(image)

    # Display the output
    cv2.imshow('CVZone Face Detection', image)

    # Waits for 1 millisecond for a key press
    key = cv2.waitKey(1)

    # Press 'q' to quit
    if key == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
