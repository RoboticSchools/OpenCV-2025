import cv2
from cvzone.HandTrackingModule import HandDetector
from PIL import Image
import google.generativeai as genai

# Configure Gemini API with your API key
genai.configure(api_key="AIzaSyBKEActcuG1LOOwesVh1dRpSWDQW9Y7LUQ")
model = genai.GenerativeModel("gemini-1.5-flash")

# Open webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Set width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Set height

# Initialize hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# List to store drawing points
draw_points = []

while True:
    # Read frame from webcam
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flip for mirror effect

    # Detect hand
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]               # Use the first hand
        lmList = hand["lmList"]       # Get landmark list
        fingers = detector.fingersUp(hand)  # Check which fingers are up

        # If only the index finger is up, record its tip for drawing
        if fingers[1] == 1 and sum(fingers) == 1:
            x, y = lmList[8][0], lmList[8][1]  # Index finger tip
            draw_points.append((x, y))
        else:
            draw_points.append(None)  # Pause drawing when finger lifted

    # Draw lines between recorded points
    for i in range(1, len(draw_points)):
        if draw_points[i - 1] is not None and draw_points[i] is not None:
            cv2.line(img, draw_points[i - 1], draw_points[i], (255, 0, 255), 7)

    # Show live webcam with drawing
    cv2.imshow("Draw with Index Finger", img)

    # Listen for key press
    key = cv2.waitKey(1)

    # Press 'x' to capture and send image to Gemini for analysis
    if key == ord('x'):
        print("🖼️ Capturing image and sending to Gemini...")

        # Convert to RGB and then to PIL image
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img_rgb)

        # Ask Gemini to analyze the image
        response = model.generate_content([pil_img, "Give me only solution to the drawing math problem on the screen"])
        print("🤖 Gemini says:", response.text)

        # Clear drawing after sending
        draw_points = []

    # Press 'q' to quit the application
    if key == ord('q'):
        break

# Release webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
