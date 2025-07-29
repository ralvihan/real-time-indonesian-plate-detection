import numpy as np
import cv2
import matplotlib.pyplot as plt
import time

plateCascade = cv2.CascadeClassifier('Cascades/haarcascade_indonesian_plate_number.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height
plate_counts = []
frames = []

start_time = time.time()
frame_count = 0

while True:
    ret, img = cap.read()
    if not ret:
        print("Failed to capture image. Exiting...")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect Indonesian license plates
    plates = plateCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    plate_count = len(plates)

    for (x, y, w, h) in plates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle for plate

    frame_count += 1
    frames.append(frame_count)
    plate_counts.append(plate_count)

    cv2.imshow('Video', img)

    # Stop detection after 15 seconds
    if time.time() - start_time > 15:
        break

    # Exit when 'ESC' is pressed
    k = cv2.waitKey(30) & 0xFF
    if k == 27:  # ESC key
        break


plt.figure()
plt.plot(frames, plate_counts, label='License Plates', color='green')
plt.xlabel('Frames')
plt.ylabel('Count')
plt.title('Indonesian License Plate Detection Counts Over 15 Seconds')
plt.legend()
plt.grid(True)
plt.show()


time.sleep(2)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, img = cap.read()
    if not ret:
        print("Failed to capture image. Exiting...")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect Indonesian license plates
    plates = plateCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles around detected plates
    for (x, y, w, h) in plates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle for plate

    # Display the resulting frame
    cv2.imshow('Video', img)

    # Exit when 'ESC' is pressed
    k = cv2.waitKey(30) & 0xFF
    if k == 27:  # ESC key
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
