import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Example function to plot the robot's position
def plot_robot_position(theta1, theta2, theta3):
    a1 = 38.55  # Length of the first link
    a2 = 120    # Length of the second link
    a3 = 187.75 # Length of the third link

    # Compute the position of the end effector using forward kinematics
    x = a1 * np.cos(theta1) + a2 * np.cos(theta2) + a3 * np.cos(theta3)
    y = a1 * np.sin(theta1) + a2 * np.sin(theta2) + a3 * np.sin(theta3)
    z = 0  # Assuming movement in the 2D plane for simplicity

    return x, y, z

# Generate a set of random joint angles (theta1, theta2, theta3)
num_points = 1000
theta1_values = np.random.uniform(0, np.pi, num_points)   # Random values between 0 and pi
theta2_values = np.random.uniform(-np.pi, np.pi, num_points) # Random values between -pi and pi
theta3_values = np.random.uniform(-np.pi, np.pi, num_points) # Random values between -pi and pi

# Store the end effector positions
end_effector_positions = []

for i in range(num_points):
    theta1 = theta1_values[i]
    theta2 = theta2_values[i]
    theta3 = theta3_values[i]
    
    # Get the position for each set of joint angles
    x, y, z = plot_robot_position(theta1, theta2, theta3)
    end_effector_positions.append((x, y, z))

# Extract x, y, z values for plotting
x_vals = [pos[0] for pos in end_effector_positions]
y_vals = [pos[1] for pos in end_effector_positions]
z_vals = [pos[2] for pos in end_effector_positions]

# Create a figure for plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(x_vals, y_vals, z_vals, c='blue', marker='o', s=1)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Title for the plot
ax.set_title('3DOF Arm Workspace Points')

# Show the plot
plt.show()
