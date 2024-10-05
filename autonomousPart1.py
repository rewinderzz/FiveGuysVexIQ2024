#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
LeftDrive = Motor(Ports.PORT9, True)
RightDrive = Motor(Ports.PORT3, False)
gyro_11 = Gyro(Ports.PORT11)
Conveyor_motor_a = Motor(Ports.PORT8, True)
Conveyor_motor_b = Motor(Ports.PORT2, False)
Conveyor = MotorGroup(Conveyor_motor_a, Conveyor_motor_b)

#endregion VEXcode Generated Robot Configuration

import time
#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
LeftDrive = Motor(Ports.PORT9, True)
RightDrive = Motor(Ports.PORT3, False)
gyro_11 = Gyro(Ports.PORT11)
Conveyor_motor_a = Motor(Ports.PORT8, True)
Conveyor_motor_b = Motor(Ports.PORT2, False)
Conveyor = MotorGroup(Conveyor_motor_a, Conveyor_motor_b)



# Make random actually random
def setRandomSeedUsingAccel():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    urandom.seed(int(xaxis + yaxis + zaxis))
    
# Set random seed 
setRandomSeedUsingAccel()

LeftDriveSpeed = 0
RightDriveSpeed = 0
ShootingSpeed = 0
message1 = Event()

def GyroTurn_heading_velocity_momentum(GyroTurn_heading_velocity_momentum__heading, GyroTurn_heading_velocity_momentum__velocity, GyroTurn_heading_velocity_momentum__momentum):
    global LeftDriveSpeed, RightDriveSpeed, ShootingSpeed, message1
    if GyroTurn_heading_velocity_momentum__heading > gyro_11.heading():
        while GyroTurn_heading_velocity_momentum__heading - GyroTurn_heading_velocity_momentum__momentum > gyro_11.heading():
            LeftDrive.set_velocity(GyroTurn_heading_velocity_momentum__velocity, PERCENT)
            RightDrive.set_velocity(GyroTurn_heading_velocity_momentum__velocity, PERCENT)
            LeftDrive.spin(REVERSE)
            RightDrive.spin(FORWARD)
            wait(20, MSEC)
    else:
        while GyroTurn_heading_velocity_momentum__heading + GyroTurn_heading_velocity_momentum__momentum < gyro_11.heading():
            LeftDrive.set_velocity(GyroTurn_heading_velocity_momentum__velocity, PERCENT)
            RightDrive.set_velocity(GyroTurn_heading_velocity_momentum__velocity, PERCENT)
            LeftDrive.spin(FORWARD)
            RightDrive.spin(REVERSE)
            wait(20, MSEC)
    LeftDrive.stop()
    RightDrive.stop()
    LeftDrive.set_velocity(LeftDriveSpeed, PERCENT)
    RightDrive.set_velocity(RightDriveSpeed, PERCENT)

def Arc_Forward_Distance_Velocity_Offset_Direction(Arc_Forward_Distance_Velocity_Offset_Direction__Distance, Arc_Forward_Distance_Velocity_Offset_Direction__Velocity, Arc_Forward_Distance_Velocity_Offset_Direction__Offset, Arc_Forward_Distance_Velocity_Offset_Direction__Direction):
    global LeftDriveSpeed, RightDriveSpeed, ShootingSpeed, message1
    if Arc_Forward_Distance_Velocity_Offset_Direction__Direction == 1:
        LeftDrive.set_velocity((Arc_Forward_Distance_Velocity_Offset_Direction__Velocity - Arc_Forward_Distance_Velocity_Offset_Direction__Offset), PERCENT)
        RightDrive.set_velocity(Arc_Forward_Distance_Velocity_Offset_Direction__Velocity, PERCENT)
    else:
        LeftDrive.set_velocity(Arc_Forward_Distance_Velocity_Offset_Direction__Velocity, PERCENT)
        RightDrive.set_velocity((Arc_Forward_Distance_Velocity_Offset_Direction__Velocity - Arc_Forward_Distance_Velocity_Offset_Direction__Offset), PERCENT)
    LeftDrive.spin(FORWARD)
    RightDrive.spin(FORWARD)
    wait(Arc_Forward_Distance_Velocity_Offset_Direction__Distance, SECONDS)
    LeftDrive.stop()
    RightDrive.stop()
    LeftDrive.set_velocity(LeftDriveSpeed, PERCENT)
    RightDrive.set_velocity(RightDriveSpeed, PERCENT)



def GyroTurnV2_Heading_Velocity_Momentum(GyroTurnV2_Heading_Velocity_Momentum__Heading, GyroTurnV2_Heading_Velocity_Momentum__Velocity, GyroTurnV2_Heading_Velocity_Momentum__Momentum):
    global LeftDriveSpeed, RightDriveSpeed, ShootingSpeed, message1
    LeftDrive.set_velocity(GyroTurnV2_Heading_Velocity_Momentum__Velocity, PERCENT)
    RightDrive.set_velocity(GyroTurnV2_Heading_Velocity_Momentum__Velocity, PERCENT)
    while (gyro_11.heading() < GyroTurnV2_Heading_Velocity_Momentum__Heading - GyroTurnV2_Heading_Velocity_Momentum__Momentum or gyro_11.heading() > GyroTurnV2_Heading_Velocity_Momentum__Heading + GyroTurnV2_Heading_Velocity_Momentum__Momentum):
        if gyro_11.heading() < GyroTurnV2_Heading_Velocity_Momentum__Heading - GyroTurnV2_Heading_Velocity_Momentum__Momentum:
            LeftDrive.spin(FORWARD)
            RightDrive.spin(REVERSE)
        else:
            LeftDrive.spin(REVERSE)
            RightDrive.spin(FORWARD)
        wait(10, MSEC)
    LeftDrive.stop()
    RightDrive.stop()

def when_started1():
    global LeftDriveSpeed, RightDriveSpeed, ShootingSpeed, message1
    gyro_11.calibrate(GyroCalibrationType.NORMAL)
    LeftDrive.set_position(0, DEGREES)
    RightDrive.set_position(0, DEGREES)
    wait(0.2, SECONDS)
    LeftDrive.spin_for(REVERSE, 450, DEGREES, wait=False)
    RightDrive.spin_for(REVERSE, 450, DEGREES)
    wait(0.2, SECONDS)
    GyroTurnV2_Heading_Velocity_Momentum(270, 25, 10)
    wait(0.3, SECONDS)
    LeftDrive.set_velocity(50, PERCENT)
    RightDrive.set_velocity(50, PERCENT)

def onevent_buttonRight_pressed_0():
    global LeftDriveSpeed, RightDriveSpeed, ShootingSpeed, message1
    LeftDriveSpeed = 100
    RightDriveSpeed = 100
    Arc_Forward_Distance_Velocity_Offset_Direction(8, 81, 10, 2)
    wait(5, SECONDS)

def onevent_buttonCheck_pressed_0():
    global LeftDriveSpeed, RightDriveSpeed, ShootingSpeed, message1
    pass



# repeating forward and backward

myVariable = 0
error = 0
output = 0

def PStraight_distance_heading_velocity_kp(PStraight_distance_heading_velocity_kp__distance, PStraight_distance_heading_velocity_kp__heading, PStraight_distance_heading_velocity_kp__velocity, PStraight_distance_heading_velocity_kp__kp):
    global myVariable, error, output
    LeftDrive.set_position(0, DEGREES)
    RightDrive.set_position(0, DEGREES)
    if PStraight_distance_heading_velocity_kp__velocity > 0:
        while LeftDrive.position(DEGREES) < PStraight_distance_heading_velocity_kp__distance:
            error = PStraight_distance_heading_velocity_kp__heading - gyro_11.rotation()
            output = error * PStraight_distance_heading_velocity_kp__kp
            LeftDrive.set_velocity((PStraight_distance_heading_velocity_kp__velocity - output), PERCENT)
            RightDrive.set_velocity((PStraight_distance_heading_velocity_kp__velocity + output), PERCENT)
            LeftDrive.spin(FORWARD)
            RightDrive.spin(FORWARD)
            wait(20, MSEC)
    else:
        while LeftDrive.position(DEGREES) > PStraight_distance_heading_velocity_kp__distance:
            error = PStraight_distance_heading_velocity_kp__heading - gyro_11.rotation()
            output = error * PStraight_distance_heading_velocity_kp__kp
            LeftDrive.set_velocity((PStraight_distance_heading_velocity_kp__velocity - output), PERCENT)
            RightDrive.set_velocity((PStraight_distance_heading_velocity_kp__velocity + output), PERCENT)
            LeftDrive.spin(FORWARD)
            RightDrive.spin(FORWARD)
            wait(20, MSEC)
    LeftDrive.stop()
    RightDrive.stop()

# execution

def MoveForwardAndBackward():
    Conveyor.set_velocity(100, PERCENT)
    LeftDrive.set_velocity(45, PERCENT)
    RightDrive.set_velocity(45, PERCENT)
    counter = 0
    while True:      
        # move forward
        LeftDrive.spin_for(FORWARD, 2.85, TURNS, wait=False)
        RightDrive.spin_for(FORWARD, 2.85, TURNS)

        #Scoring First Ball
        Conveyor.set_timeout(4,SECONDS)
        Conveyor.spin(FORWARD)
        wait(4,SECONDS)
        Conveyor.stop()
        if counter < 1:
            for i in range(3):
                Conveyor.set_velocity(100, PERCENT)
                LeftDrive.set_velocity(50, PERCENT)
                RightDrive.set_velocity(50, PERCENT)
                LeftDrive.spin_for(REVERSE, 0.12, TURNS, wait=False)
                RightDrive.spin_for(REVERSE, 0.12, TURNS)
                wait(20,MSEC)
                LeftDrive.spin_for(FORWARD, 0.12, TURNS, wait=False)
                RightDrive.spin_for(FORWARD, 0.12, TURNS)
        # Conveyor.set_velocity(70, PERCENT)
        # LeftDrive.set_velocity(70, PERCENT)
        # RightDrive.set_velocity(70, PERCENT)

        # moving backwards
        LeftDrive.spin_for(REVERSE, 2.85, TURNS, wait=False)
        RightDrive.spin_for(REVERSE, 2.85, TURNS, wait = False)
        # pickup ball, start conveyor for 1s
        Conveyor.set_timeout(4, SECONDS)
        Conveyor.spin(FORWARD)
        wait(4, SECONDS)
        Conveyor.stop()
        counter += 1


def reset_encoders():
    LeftDrive.set_position(0, DEGREES)
    RightDrive.set_position(0, DEGREES)

def get_average_distance():
    return (LeftDrive.set_position(DEGREES) + RightDrive.set_position(DEGREES)) / 2
# system event handlers
brain.buttonRight.pressed(onevent_buttonRight_pressed_0)
brain.buttonCheck.pressed(onevent_buttonCheck_pressed_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()
MoveForwardAndBackward()