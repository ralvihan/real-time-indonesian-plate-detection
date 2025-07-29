from src.camera_utils import setup_camera
from src.plate_detection import detect_and_display, continuous_detection
from src.plot_utils import plot_counts
import cv2
import time

# Load classifier
plateCascade = cv2.CascadeClassifier('Cascades/haarcascade_indonesian_plate_number.xml')

# Setup camera
cap = setup_camera()

# Run detection for 15 seconds
frames, plate_counts = detect_and_display(cap, plateCascade, duration=15)

# Plot results
plot_counts(frames, plate_counts)

# Wait 2 seconds before continuous detection
time.sleep(2)

# Re-open camera
cap = setup_camera()

# Run continuous detection until ESC pressed
continuous_detection(cap, plateCascade)
