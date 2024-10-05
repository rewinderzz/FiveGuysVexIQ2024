#Global Directions
GYRO_EAST = 0
GYRO_NORTH = 90
GYRO_WEST = 180
GYRO_SOUTH = 270

def get_heading_difference(from_heading, to_heading):
    difference = to_heading - from_heading
    if difference > 180:
        return difference - 360
    if difference <= -180:
        return difference + 360
    return difference

def gyro_turn_by_heading(target_heading, velocity, momentum_buffer):
    LeftDrive.set_velocity(abs(velocity), PERCENT)
    RightDrive.set_velocity(abs(velocity), PERCENT)
    heading_difference = get_heading_difference(gyro_11.heading(), target_heading)
    if heading_difference  == 0:
        return
    elif heading_difference < 0:
        while get_heading_difference(gyro_11.heading(), target_heading) < -momentum_buffer:
            LeftDrive.spin(FORWARD)
            RightDrive.spin(REVERSE)
            wait(20, MSEC)
    else:
        while get_heading_difference(gyro_11.heading(), target_heading) > momentum_buffer:
            LeftDrive.spin(REVERSE)
            RightDrive.spin(FORWARD)
            wait(20, MSEC)
    LeftDrive.stop()
    RightDrive.stop()

def when_started1():
    global LeftDriveSpeed, RightDriveSpeed, ShootingSpeed, message1
    gyro_11.calibrate(GyroCalibrationType.NORMAL)
    wait(2, SECONDS) # this is important otherwise gyro sensor has not completed calibration
    LeftDrive.set_position(0, DEGREES)
    RightDrive.set_position(0, DEGREES)
    gyro_11.set_heading(GYRO_WEST)
    wait(0.2, SECONDS)
    # LeftDrive.spin_for(REVERSE, 415, DEGREES, wait=False)
    # RightDrive.spin_for(REVERSE, 415, DEGREES)
    move_straight(-415, GYRO_WEST, 50, 2)
    wait(0.2, SECONDS)
    gyro_turn_by_heading(GYRO_NORTH, 25, 15)
    wait(0.3, SECONDS)

def move_straight(distance, heading, velocity, correction_coefficient):
    LeftDrive.set_position(0, DEGREES)
    RightDrive.set_position(0, DEGREES)
    heading_difference = 0
    correction = 0
    if distance == 0:
        return
    elif distance > 0:
        while LeftDrive.position(DEGREES) < distance:
            heading_difference = get_heading_difference(gyro_11.heading(), heading)
            correction = heading_difference * correction_coefficient
            LeftDrive.set_velocity(abs(velocity) - correction, PERCENT)
            RightDrive.set_velocity(abs(velocity) + correction, PERCENT)
            LeftDrive.spin(FORWARD)
            RightDrive.spin(FORWARD)
            wait(20, MSEC)
    else:
        while LeftDrive.position(DEGREES) > distance:
            heading_difference = get_heading_difference(gyro_11.heading(), heading)
            correction = heading_difference * correction_coefficient
            LeftDrive.set_velocity(abs(velocity) + correction, PERCENT)
            RightDrive.set_velocity(abs(velocity) - correction, PERCENT)
            LeftDrive.spin(REVERSE)
            RightDrive.spin(REVERSE)
            wait(20, MSEC)
    LeftDrive.stop()
    RightDrive.stop()
