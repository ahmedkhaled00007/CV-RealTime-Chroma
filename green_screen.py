import cv2 as cv
import numpy as np
import time

# Open webcam
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()

# Wait 3 seconds to capture background
print("📸 Get ready! Capturing background in 3 seconds...")
time.sleep(3)


ret, background = cap.read()
if not ret:
    print("❌ Failed to grab background")
    exit()

background = cv.resize(background, (500, 500))
print("✅ Background captured! Starting green screen...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    frame = cv.resize(frame, (500, 500))

    # Convert BGR → HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Green HSV range
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    # Create mask for green areas
    green_mask = cv.inRange(hsv, lower_green, upper_green)
    green_mask = cv.morphologyEx(green_mask, cv.MORPH_OPEN, np.ones((5,5), np.uint8))
    green_mask = cv.morphologyEx(green_mask, cv.MORPH_CLOSE, np.ones((5,5), np.uint8))

    # Invert mask → keep foreground
    mask_inv = cv.bitwise_not(green_mask)

    # Extract foreground
    fg = cv.bitwise_and(frame, frame, mask=mask_inv)

    # Extract background only where green was
    bg = cv.bitwise_and(background, background, mask=green_mask)

    # Combine foreground and backgroundq
    final = cv.add(fg, bg)

    # Show result
    cv.imshow("Green Screen Effect", final)

    # Press 'q' to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
