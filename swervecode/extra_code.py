# NOTE: this might have to be in a diff area in our code - just importing it for now
# pass the result of get_wheel_vectors to this function
def move_rover(wheels_group):
    speeds = [get_wheel_speed(wheels_group[0]),get_wheel_speed(wheels_group[1]), get_wheel_speed(wheels_group[2]),get_wheel_speed(wheels_group[3])]

    #Normalize speeds
    max = 0
    for i in range(len(speeds)):
        if max<speeds[i]:
            max = speeds[i]
            
    if (max > 1):
            for i in range(len(speeds)) :
                speeds[i] /= max
            
        
    # const FL_velocity = wheels_group.FL_wheel_speed * Math.cos(wheels_group.FL_wheel_angle);
    # const FR_velocity = wheels_group.FR_wheel_speed * Math.cos(wheels_group.FR_wheel_angle);
    # const BL_velocity = wheels_group.BL_wheel_speed * Math.cos(wheels_group.BL_wheel_angle);
    # const BR_velocity = wheels_group.BR_wheel_speed * Math.cos(wheels_group.BR_wheel_angle);
    
    FL_velocity = speeds[0]
    FR_velocity = speeds[1]
    BL_velocity = speeds[2]
    BR_velocity = speeds[3]
    
    # velocity and angle
    v = (FL_velocity + FR_velocity + BL_velocity + BR_velocity) / 4
    w = (FR_velocity - FL_velocity + BR_velocity - BL_velocity) / 20; 
    
    return [v, w] # velocity of body and angle of body