import cv2
import time

def detect_and_display(cap, plateCascade, duration=15):
    plate_counts = []
    frames = []
    frame_count = 0
    start_time = time.time()

    while True:
        ret, img = cap.read()
        if not ret:
            print("Failed to capture image. Exiting...")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        plates = plateCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        plate_count = len(plates)

        for (x, y, w, h) in plates:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        frame_count += 1
        frames.append(frame_count)
        plate_counts.append(plate_count)

        cv2.imshow('Video', img)

        if time.time() - start_time > duration:
            break

        if cv2.waitKey(30) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return frames, plate_counts

def continuous_detection(cap, plateCascade):
    while True:
        ret, img = cap.read()
        if not ret:
            print("Failed to capture image. Exiting...")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        plates = plateCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in plates:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Video', img)

        if cv2.waitKey(30) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
