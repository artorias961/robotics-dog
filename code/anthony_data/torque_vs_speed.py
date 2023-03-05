import numpy as np
import matplotlib.pyplot as plt


def two_leg_trot():
    # Creating the percentage dataset
    percentage = np.linspace(0, 100, num=101, dtype=np.int16)
    print(percentage)

    # The maximum load (weight) of the dog (pounds)
    max_dog_load = 25.0

    # Dividing the weight into two legs
    half_load_lbs = max_dog_load / 2.0

    # Converting the data from pounds to kilograms
    half_load_kg = half_load_lbs * 0.453592

    # The torque needed without factor of safety (picked 12 cm)
    safety_without_load = half_load_kg * 12.0

    # Load at


if __name__ == "__main__":
    two_leg_trot()