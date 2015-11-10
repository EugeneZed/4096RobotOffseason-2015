#! python3
"""
Module for Autonomous code
"""

import time



def init( robot ):
	"""
	This function is run once each time the robot enters autonomous mode.
	"""
	# Save real-world timestamp when auto starts.
	# All other auto events below are relative to this start time
	robot.auto_start_time = time.time( )


def periodic( robot ):
	"""
	This function is called periodically during autonomous.
	"""
	auto_time = time.time( ) - robot.auto_start_time

	# Clamps
	if auto_time >=  4.5:
		clamp_value = False
	else:
		clamp_value = True

	robot.clamp_solenoid1.set( not clamp_value )
	robot.clamp_solenoid2.set( clamp_value )
	robot.clamp_solenoid3.set( not clamp_value )
	robot.clamp_solenoid4.set( clamp_value )
	
	# Lift
	if auto_time >= 0.5 and auto_time < 1.0:
		# go up
		robot.lift_motor1.set( 0.5 )
		robot.lift_motor2.set( -0.5 )
	else:
		robot.lift_motor1.set( 0 )
		robot.lift_motor2.set( 0 )


	# Drive
	if auto_time >= 0.75 and auto_time < 3.50:
		#robot.drive.drive( 0.5, 0 )
		robot.drive.mecanumDrive_Cartesian( 0, 0.5, 0, 0 )
	else:
		#robot.drive.drive( 0, 0 )
		robot.drive.mecanumDrive_Cartesian( 0, 0, 0, 0 )

