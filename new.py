import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Example function to plot the robot's position
def plot_robot_position(theta1, theta2, theta3):
    # Length of the robot links
    a1 = 38.55  # Length of the first link
    a2 = 120    # Length of the second link
    a3 = 187.75 # Length of the third link

    # Ensure angles are in radians (if in degrees, convert to radians)
    theta1 = np.radians(theta1) if theta1 > np.pi else theta1
    theta2 = np.radians(theta2) if theta2 > np.pi else theta2
    theta3 = np.radians(theta3) if theta3 > np.pi else theta3

    # Compute the position of the end effector using forward kinematics
    x = a1 * np.cos(theta1) + a2 * np.cos(theta2) + a3 * np.cos(theta3)
    y = a1 * np.sin(theta1) + a2 * np.sin(theta2) + a3 * np.sin(theta3)
    z = 0  # Assuming movement in the 2D plane for simplicity

    # Debug print statement to check the coordinates of the end effector
    print(f"End Effector Position -> X: {x}, Y: {y}, Z: {z}")

    # Create a figure for plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the point (this can be the end effector's position)
    ax.scatter(x, y, z)

    # Set labels for the axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Adjust the axes limits for better visualization
    ax.set_xlim([x-100, x+100])
    ax.set_ylim([y-100, y+100])
    ax.set_zlim([z-10, z+10])

    # Show the plot
    plt.show()
