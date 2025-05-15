import cv2
import numpy as np

# Global variables
drawing = False
ix, iy = -1, -1

# Mouse callback function
def draw_line(event, x, y, flags, param):
    global drawing, ix, iy, canvas

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(canvas, (ix, iy), (x, y), (0, 0, 255), 5)
            ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(canvas, (ix, iy), (x, y), (0, 0, 255), 5)

    elif event == cv2.EVENT_RBUTTONDOWN:
        # Right-click clears the canvas
        canvas[:] = 0
        print("🧹 Canvas cleared!")

# Open webcam
cam = cv2.VideoCapture(0)
cv2.namedWindow("Live Draw")

# Get frame size for canvas
cam_status, image = cam.read()
canvas = np.zeros_like(image)

# Set mouse callback
cv2.setMouseCallback("Live Draw", draw_line)

while True:
    cam_status, image = cam.read()

    # Blend drawing with live video
    blended = cv2.addWeighted(image, 0.9, canvas, 1.0, 0)

    # Show output
    cv2.imshow("Live Draw", blended)

    # Waits for 1 millisecond for a key press
    key = cv2.waitKey(1)

    # Press 'q' to quit
    if key == ord('q'):
        break

# Release and close
cam.release()
cv2.destroyAllWindows()
