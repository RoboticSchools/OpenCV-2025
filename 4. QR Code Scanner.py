import cv2

cap = cv2.VideoCapture(0)
qr_detector = cv2.QRCodeDetector()

while True:
    cam_status, image = cap.read()
    image = cv2.flip(image, 1)

    # 📦 Detect and decode QR code from the image
    data, bbox, _ = qr_detector.detectAndDecode(image)

    if bbox is not None:
        # Draw 4 lines between the bounding box points
        for i in range(4):
            x1, y1 = int(bbox[0][i][0]), int(bbox[0][i][1])

            # Trick to wrap around: after 3, connect back to 0
            if i == 3: i = -1  # This makes (i + 1) = 0 on the next line

            x2, y2 = int(bbox[0][i + 1][0]), int(bbox[0][i + 1][1])
            # Draw line from current point to next point
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

        if data:
            cv2.putText(image, data, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

    cv2.imshow("QR Code Scanner", image)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# 🧹 Cleanup
cap.release()
cv2.destroyAllWindows()
