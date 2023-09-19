from matplotlib.lines import lineStyles
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

class BatteryCalculation:
    def __init__(self) -> None:
        # Getting the voltage output
        self.voltage_output = float

        # The battery capacity (mAh)
        self.battery_capacity = float

        # Discharge rate (C)
        self.discharge_rate = float

        # User expect to use in Amps
        self.user_expected_current_draw = float

        # Discharge Current (A)
        self.discharge_current = float

        # Time of battery lasting
        self.battery_time_expectancy = float


    def get_user_input(self):
        """
        Getting the user prompt about the battery.

        return: N/A
        """
        # Creating a prompt for the user
        prompt_text = "Input the Voltage Output, Discharge Capacity (mAh), and Discharge Rate (C). "  \
        "A graphical chart will be produce for you and all the necessary information you need!!!"


        # Printing the output
        print(prompt_text)

        # Getting the user input about the battery
        self.voltage_output = float(input("The voltage output (V) of the battery is: "))
        self.battery_capacity = float(input("The Discharge Capacity (mAh) of the battery is: "))
        self.discharge_rate = float(input("The Discharge Rate (C) of the battery is: "))

        # Getting the user input of the load on the system
        self.user_expected_current_draw = float(input("Input the expected current (A) draw of the entire system: "))

        # Creating a conditional statement
        if (self.voltage_output < 0) or (self.battery_capacity < 0) or (self. discharge_rate < 0):
            # Print an error then break
            raise("Input values greater than 0!!!!")
        
        # Print a wall
        print("========================================")

    def max_amp_rating(self):
        """
        Gets the Impulse Discharge Current Rate (max current rate for a few seconds 
        before killing the battery)

        """
        # Creating the prompt
        print("Discharge Current = Discharge Capacity * Discharge Rate")

        # Determining the max rating amps of the battery
        self.discharge_current = (self.battery_capacity / 1000.0) * self.discharge_rate

        # Print the output
        print(f"Your Discharge Current is: {self.discharge_current}")

        # Print a wall
        print("========================================")

    def battery_expectancy_time(self):
        """
        Calculates the battery time depending on the user current draw

        """
        # Creating a prompt
        print(" Time of battery = (1 hour / User Expected Current Draw) * (60 mins / 1 hour)")

        # Getting the time = (Ah/A) * (mins/h) = mins
        self.battery_time_expectancy = ((self.battery_capacity / 1000.0 )/ self.user_expected_current_draw) * (60.0)

        # Printing the output
        print(f"The battery will last about: {self.battery_time_expectancy:.2f} mins")

        # Print a wall
        print("========================================")

    def plotting_battery_time(self):
        # Creating a list of points
        time = np.arange(int(self.discharge_current))
        
        # Copying the same value of the current
        current_draw_array = time.copy()

        # Applying the calculations for the current draw array [expression for item in iterable]
        current_draw_array = [( ((self.battery_capacity / 1000.0 )/ counter_index) * (60.0)) for counter_index in current_draw_array]

        # Plotting the system
        sns.lineplot(x=time, y=current_draw_array, marker='o', markersize=7, color='green')
        # Styling the plot
        sns.set_style("darkgrid")


        # Creating the label
        plt.title("Battery: Time vs Current")
        plt.ylabel("Current (A)")
        plt.xlabel("Time (mins)")

        # Showing the plot
        plt.show()
    
    def prompt_warning(self):
        pass

    def main(self):
        # Runs the first function
        self.get_user_input()

        # Runs the second function
        self.max_amp_rating()

        # Runsthe third function
        self.battery_expectancy_time()

        # Plotting the system
        self.plotting_battery_time()


if __name__ == "__main__":
    # Calling the class
    BC = BatteryCalculation()

    # Calling the main function from the class
    BC.main()