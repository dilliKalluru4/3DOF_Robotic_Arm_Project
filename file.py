import numpy as np
from time import sleep
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Servo Control Simulation Functions ---
# Simulated servo motor control functions
def move_servo_1(angle):
    print(f"Simulating Servo 1 moving to {angle} degrees")

def move_servo_2(angle):
    print(f"Simulating Servo 2 moving to {angle} degrees")

def move_servo_3(angle):
    print(f"Simulating Servo 3 moving to {angle} degrees")

def move_servo_4(angle):
    print(f"Simulating Servo 4 moving to {angle} degrees")

# --- Robot Class ---
class Robot:
    def __init__(self):
        print("created robot")
        self.a1 = 38.55    # Length of the first link
        self.a2 = 120      # Length of the second link
        self.a3 = 187.75   # Length of the third link

    def IK(self, pWx, pWy, pWz):
        # Moving pWz from frame 0 to frame 1
        pWz -= self.a1

        # Calculating cos(theta3)
        c3 = (pWx**2 + pWy**2 + pWz**2 - self.a2**2 - self.a3**2) / (2 * self.a2 * self.a3)
        
        # Check for the validity of the solution
        if np.abs(c3) > 1:
            print("Point outside workspace")
            return 0 
        
        # Calculating possible values for sin(theta3)
        s3_pos = np.sqrt(1 - c3**2)  # sin(theta3) for the first solution
        s3_neg = -s3_pos            # sin(theta3) for the second solution

        # Calculating possible values for theta3
        theta3_1 = np.arctan2(s3_pos, c3)  # First solution for theta3
        theta3_2 = np.arctan2(s3_neg, c3)  # Second solution for theta3

        # Calculating possible values for theta2
        theta2_1 = np.arctan2(pWz,np.sqrt(pWx**2 + pWy**2)) - np.arctan2((self.a3*np.sin(theta3_1)),(self.a2 + self.a3*np.cos(theta3_1)))
        theta2_2 = np.arctan2(pWz,np.sqrt(pWx**2 + pWy**2)) - np.arctan2((self.a3*np.sin(theta3_2)),(self.a2 + self.a3*np.cos(theta3_2)))

        # Calculating possible values for theta1
        theta1_1 = np.arctan2(pWy, pWx)  # First solution for theta1
        theta1_2 = np.arctan2(-pWy, -pWx)  # Second solution for theta1

        # Choosing the combination of theta2 and theta3 values in respective permissible ranges
        if theta2_1 >= 0 and theta2_1 <= np.pi and theta3_1 >= -np.pi/2 and theta3_1 <= np.pi/2:
            theta2 = theta2_1
            theta3 = theta3_1

        elif theta2_2 >= 0 and theta2_2 <= np.pi and theta3_2 >= -np.pi/2 and theta3_2 <= np.pi/2:
            theta2 = theta2_2
            theta3 = theta3_2
        else:
            print("No unique combination of theta 2 and theta 3 within constraints")
            return 0

        # Choosing theta1 in permissible range and making changes to theta2 and theta3 to accomodate for it if necessary
        if theta1_1 >= 0 and theta1_1 <= np.pi:
            theta1 = theta1_1
        elif theta1_2 >= 0 and theta1_2 <= np.pi:
            theta1 = theta1_2
            theta2 = np.pi-theta2
            theta3 = -theta3
        else:
            print("No unique theta 1 within constraints")
            return 0
        
        # Returning successfully calculated theta values
        return {
            "theta1": np.rad2deg(theta1),
            "theta2": np.rad2deg(theta2),
            "theta3": np.rad2deg(theta3)
        }

# --- Visualization Function ---
def plot_robot_position(theta1, theta2, theta3):
    a1 = 38.55  # Length of the first link
    a2 = 120    # Length of the second link
    a3 = 187.75 # Length of the third link

    # Compute the position of the end effector using forward kinematics
    x = a1 * np.cos(theta1) + a2 * np.cos(theta2) + a3 * np.cos(theta3)
    y = a1 * np.sin(theta1) + a2 * np.sin(theta2) + a3 * np.sin(theta3)
    z = 0  # Assuming movement in the 2D plane for simplicity

    return x, y, z

# --- Main Execution ---
if __name__ == "__main__":
    # Set initial servo angles
    move_servo_1(0)
    move_servo_2(0)
    move_servo_3(0)
    move_servo_4(-30)  # Open gripper by setting servo 4 to -30 degrees

    # Initialize the robot
    robot = Robot()
    
    # Initialize list for storing the end effector positions
    end_effector_positions = []

    # Generate points to fill the 3D space
    for i in range(250):  # Generate 1000 points for a denser workspace
        theta1 = np.random.uniform(0, 2*np.pi)   # theta1 can range from 0 to 2π (full rotation)
        theta2 = np.random.uniform(-np.pi/2, np.pi/2)  # theta2 between -90° and 90° (for a broader range)
        theta3 = np.random.uniform(-np.pi, np.pi)  # theta3 can range from -180° to 180°

        # Simulate the robot moving to these angles
        #print(f"Simulating Servo 1 moving to {theta1} degrees")
        move_servo_1(theta1)
        sleep(0.1)  # Short delay for simulation effect

        #print(f"Simulating Servo 2 moving to {theta2} degrees")
        move_servo_2(theta2)
        sleep(0.1)

        #print(f"Simulating Servo 3 moving to {theta3} degrees")
        move_servo_3(theta3)
        sleep(0.1)

        # Calculate the position of the end effector and append to the list
        position = plot_robot_position(theta1, theta2, theta3)  # Calculate end effector position
        end_effector_positions.append(position)  # Append the position to the list

    # Now you can plot all the positions
    all_x = [pos[0] for pos in end_effector_positions]
    all_y = [pos[1] for pos in end_effector_positions]
    all_z = [pos[2] for pos in end_effector_positions]

    # Plotting all positions
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(all_x, all_y, all_z, marker='o')

    # Setting labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Show the plot
    plt.show()
