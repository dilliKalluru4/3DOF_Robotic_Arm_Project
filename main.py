import numpy as np
from time import sleep
import servo
from robot import Robot
from visualization import plot_robot_position  # Import the visualization function
import matplotlib.pyplot as plt

# Function to set the angle for each servo
def set_angle_1(ang):
    servo.move_servo_1(ang) 

def set_angle_2(ang):
    servo.move_servo_2(ang)

def set_angle_3(ang):
    servo.move_servo_3(ang)

def set_angle_4(ang):
    servo.move_servo_4(ang)

def open_gripper():
    set_angle_4(-30)  # Open gripper by setting servo 4 to -30 degrees

# Function to compute the position of the end effector
def forward_kinematics(theta1, theta2, theta3):
    a1 = 38.55  # Length of the first link
    a2 = 120    # Length of the second link
    a3 = 187.75 # Length of the third link
    
    # Compute the position of the end effector using forward kinematics
    x = a1 * np.cos(theta1) + a2 * np.cos(theta2) + a3 * np.cos(theta3)
    y = a1 * np.sin(theta1) + a2 * np.sin(theta2) + a3 * np.sin(theta3)
    z = 0  # Assuming movement in the 2D plane for simplicity
    
    return (x, y, z)

# Function to plot the trajectory of the end effector
def plot_trajectory(path_points):
    all_x = [pos[0] for pos in path_points]
    all_y = [pos[1] for pos in path_points]
    all_z = [pos[2] for pos in path_points]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the path as a dashed line
    ax.plot(all_x, all_y, all_z, color='gray', linestyle='--', label='End-Effector Path')

    # Plot the initial and final positions
    ax.scatter(all_x[0], all_y[0], all_z[0], color='blue', label='Initial Pose', s=100)
    ax.scatter(all_x[-1], all_y[-1], all_z[-1], color='red', label='Final Pose', s=100)

    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Sample Trajectory: Move from Initial to Final Position")
    ax.legend()

    plt.show()

# Example of generating a series of points (theta1, theta2, theta3 values)
end_effector_positions = []

# Generate points to fill the 3D space
for i in range(250):  # Generate 1000 points for a denser workspace
    # Adjust the random angle ranges to allow more exploration of the 3D space
    theta1 = np.random.uniform(0, 2*np.pi)   # theta1 can range from 0 to 2π (full rotation)
    theta2 = np.random.uniform(-np.pi/2, np.pi/2)  # theta2 between -90° and 90° (for a broader range)
    theta3 = np.random.uniform(-np.pi, np.pi)  # theta3 can range from -180° to 180°

    # Simulate the robot moving to these angles
   #print(f"Simulating Servo 1 moving to {theta1} degrees")
    set_angle_1(theta1)
    sleep(0.1)  # Short delay for simulation effect

    #print(f"Simulating Servo 2 moving to {theta2} degrees")
    set_angle_2(theta2)
    sleep(0.1)

    #print(f"Simulating Servo 3 moving to {theta3} degrees")
    set_angle_3(theta3)
    sleep(0.1)

    # Calculate the position of the end effector using forward kinematics and append to the list
    position = forward_kinematics(theta1, theta2, theta3)  # Calculate end effector position
    end_effector_positions.append(position)  # Append the position to the list

# Plot the trajectory with initial and final poses
plot_trajectory(end_effector_positions)
