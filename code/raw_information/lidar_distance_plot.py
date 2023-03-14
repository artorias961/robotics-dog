import numpy as np
import matplotlib.pyplot as plt


def calculate_lidar_distance():
    # Evenly spaced vector
    x_reference = np.linspace(start=0, stop=525, num=7)

    # Creating domain for actual distance in millimeters
    ruler_millimeters = [127, 254, 381, 508, 381, 254, 127]

    # What we got from the lidar sensor
    lidar_dist = [106, 239, 361, 492, 374, 240, 101]

    # Creating an empty list
    error_percent_list = list()

    # Creating a for loop to iterate
    for index_one, index_two in zip(ruler_millimeters, lidar_dist):
        # Getting the error percent
        temp_error = (np.abs(index_two - index_one) / index_one) * 100
        temp = f"{temp_error:.2f}%"

        # Add it to the list
        error_percent_list.append(temp)

    # Print the error percent
    print(error_percent_list)


    # Plot the data (x, y)
    plt.plot(x_reference, ruler_millimeters, '-b', label='Reference Distance')
    plt.plot(x_reference, lidar_dist, '-r', label='Lidar Actual Distance')
    plt.title('LiDAR Actual vs Reference Distance')
    plt.grid(visible=True, color='green', linestyle='-', linewidth=0.5)
    plt.xlabel('Millimeters (x-axis)')
    plt.ylabel('Millimeters (y-axis)')
    plt.legend(loc='lower center')
    plt.ylim(70, 515)
    plt.xlim(-10, 530)
    plt.show()


if __name__ == "__main__":
    calculate_lidar_distance()

