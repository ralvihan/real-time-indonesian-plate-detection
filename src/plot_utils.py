import matplotlib.pyplot as plt

def plot_counts(frames, plate_counts):
    plt.figure()
    plt.plot(frames, plate_counts, label='License Plates', color='green')
    plt.xlabel('Frames')
    plt.ylabel('Count')
    plt.title('Indonesian License Plate Detection Counts Over 15 Seconds')
    plt.legend()
    plt.grid(True)
    plt.show()
