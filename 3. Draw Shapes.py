import cv2

# Open the default camera
cam = cv2.VideoCapture(0)

while True:
    # Read an image from the camera
    cam_status, image = cam.read()

    # Draw a rectangle (x1, y1) to (x2, y2) in green
    cv2.rectangle(image, (50, 50), (150, 150), (0, 255, 0), 2)

    # Draw a circle at center (cx, cy) with radius r in blue
    cv2.circle(image, (300, 150), 50, (255, 0, 0), 3)

    # Draw a red horizontal line
    cv2.line(image, (300, 300), (500, 300), (0, 0, 255), 2)

    # Add text: "Python" at position (50, 250)
    cv2.putText(image, "Python", (50, 250), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 0), 3)

    # Display the image
    cv2.imshow('Output', image)

    # Waits for 1 millisecond for a key press
    key = cv2.waitKey(1)

    # Press 'q' to quit
    if key == ord('q'):
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
