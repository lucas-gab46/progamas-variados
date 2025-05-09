import time

def move_square(side_length=1.0, speed=0.5):
    """
    Makes the robot move in a square pattern.
    
    Args:
        side_length (float): Length of each side in meters (default: 1.0)
        speed (float): Linear speed in meters/second (default: 0.5)
    """
    # Ensure parameters are positive
    side_length = abs(float(side_length))
    speed = abs(float(speed))
    
    # Calculate time for straight movement
    straight_time = side_length / speed
    turn_time = 1.57 / 1.0  # 90 degrees at 1 rad/s
    
    for _ in range(4):  # 4 sides of the square
        # Move straight
        start_time = time.time()
        while time.time() - start_time < straight_time:
            send_robot_velocity(speed, 0, 0)  # Linear movement forward
            time.sleep(0.05)
        
        # Stop the robot
        send_robot_velocity(0, 0, 0)
        time.sleep(0.1)
        
        # Turn 90 degrees
        start_time = time.time()
        while time.time() - start_time < turn_time:
            send_robot_velocity(0, 0, 1.0)  # Angular movement (CCW)
            time.sleep(0.05)
        
        # Stop the robot
        send_robot_velocity(0, 0, 0)
        time.sleep(0.1)

# Execute the trajectory
if __name__ == "__main__":
    try:
        move_square()
    except NameError:
        print("Error: 'send_robot_velocity' function is not defined")
    except KeyboardInterrupt:
        # Ensure robot stops if interrupted
        send_robot_velocity(0, 0, 0)
        print("Movement interrupted by user")