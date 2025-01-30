import math
'''import rclpy
from rclpy.node import Node
from std_msgs.msg import String''' # TODO uncomment to use ROS2 modules

def get_wheel_speed(wheel_vector):
    return math.sqrt(wheel_vector[0]*wheel_vector[0] + wheel_vector[1]*wheel_vector[1])

def get_wheel_angle(wheel_vector):
    # arctan2(x_component, y_component)
    # zero is straight ahead (need to verify what angle range in radians is)
    return math.atan2(wheel_vector[0], wheel_vector[1])

def get_wheel_vectors(rotational_velocity, vehicle_translation):
    # x component is vehicle_translation +/- rot_vel*body_width/2
    # y component is vehicle_translation +/- rot_vel*body_height/2
    # + or - depends on what wheel it is
    
    BODY_HEIGHT = 1 
    BODY_WIDTH = 1  #TODO GET BODY HEIGHT AND WIDTH 
    
    # see "derivation of inverse kinematics for swerve" figure 5
    # possible x components 
    A = vehicle_translation[0] - ((rotational_velocity)*(BODY_HEIGHT/2))
    B = vehicle_translation[0] + ((rotational_velocity)*(BODY_HEIGHT/2))

    # possible y components
    C = vehicle_translation[1] - ((rotational_velocity)*(BODY_WIDTH/2))
    D = vehicle_translation[1] + ((rotational_velocity)*(BODY_WIDTH/2))

    FL_vector = [B, D]
    FR_vector = [B, C]
    BL_vector = [A, D]
    BR_vector = [A, C]

    # returns a list containing vectors [front left, front right, back left, back right]
    return [FL_vector, FR_vector, BL_vector, BR_vector]

# converts wheel velocity to RPM
# takes a velocity vector [x_vel, y_vel]
def speed_to_rpm(velocity, wheel_radius):
    linear_vel = math.sqrt(pow(velocity[0], 2) + pow(velocity[1], 2))
    return (linear_vel / (2*math.pi * wheel_radius)) * 60

# Currently assuming this file will recieve data in the form of a desired rotational translational and rotational velocity 
def main():
    initial_dummy_data = (1, [2, 2])
    print("received data: " + str(initial_dummy_data[0]) + ", " + str(initial_dummy_data[1]))
    wheel_vectors = get_wheel_vectors(initial_dummy_data[0], initial_dummy_data[1])
    print(str(wheel_vectors)) 
    print(speed_to_rpm(wheel_vectors[0], 1))
    # TODO send this info to correct modules, convert data into correct form to send messages, etc
    


if __name__ == '__main__':
    main()

