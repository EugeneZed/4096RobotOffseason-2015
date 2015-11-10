#! python3
"""
Module for Teleoperated code
"""

### CONSTANTS ###

# Gamepad axes
GP_AXIS_LEFT_X		= 0
GP_AXIS_LEFT_Y		= 1
GP_AXIS_RIGHT_X	= 2
GP_AXIS_RIGHT_Y	= 3

# Gamepad Buttons
GP_BTN_X				= 1
GP_BTN_A				= 2
GP_BTN_B				= 3
GP_BTN_Y				= 4
GP_BTN_BUMPER_L	= 5
GP_BTN_BUMPER_R	= 6
GP_BTN_TRIGGER_L	= 7
GP_BTN_TRIGGER_R	= 8
GP_BTN_BACK			= 9
GP_BTN_START		= 10
GP_BTN_STICK_L		= 11
GP_BTN_STICK_R		= 12



def init( robot ):
	pass


def periodic( robot ):
	"""
	This function is called periodically during operator control.
	asdf
	"""

	### DRIVE ###

	gyro_angle = 0

	#Read the axes, multiply by the slider values.
	# Slider fully down = move at half speed
	#joy_left_modifier = 1.0 - ( robot.joystick_left.getZ( ) + 1.0 ) / 2.0
	joy_left_x = robot.joystick_left.getX( ) #* joy_left_modifier

	#joy_right_modifier = 1.0 - ( robot.joystick_right.getZ( ) + 1.0 ) / 2.0
	joy_right_x = robot.joystick_right.getX( ) #* joy_right_modifier
	joy_right_y = robot.joystick_right.getY( ) #* joy_right_modifier

	#robot.log_info( 'JL = {0:.2f},{1:.2f}, JR = {2:.2f},{3:.2f}'.format( joy_left_x, joy_left_modifier, joy_right_x, joy_right_y ) )

	# Drive it
	robot.drive.mecanumDrive_Cartesian( -joy_right_x, -joy_right_y, -joy_left_x, gyro_angle )

	### CLAMPS ###

	# Unless button is held, we're clamping
	clamp_value = False

	if robot.gamepad.getRawButton( GP_BTN_TRIGGER_R ):
		clamp_value = True

	# Set clamps value
	robot.clamp_solenoid1.set( clamp_value )
	robot.clamp_solenoid2.set( not clamp_value )
	robot.clamp_solenoid3.set( clamp_value )
	robot.clamp_solenoid4.set( not clamp_value )


	### LIFTER ###

	lift_value = 0.0

	if robot.gamepad.getRawButton( GP_BTN_TRIGGER_L ):
		lift_value = robot.gamepad.getRawAxis( GP_AXIS_RIGHT_Y ) * -1.0
	
		# If Left Shoulder/Bumper button is down, run lift at full speed,
		# otherwise cut range to 0.0 - 0.5
		if not robot.gamepad.getRawButton( GP_BTN_BUMPER_L ):
			lift_value = lift_value * 0.5

	# When reel gets reversed, we want left stick button to invert motor directions
	if robot.gamepad.getRawButton( GP_BTN_STICK_L ):
		lift_value = lift_value * -1.0

	# Set lift motors value
	robot.lift_motor1.set( lift_value )
	robot.lift_motor2.set( lift_value * -1.0 )		# Lift Motor 2 is inverted

