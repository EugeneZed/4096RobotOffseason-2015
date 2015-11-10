#! python3
"""
Ctrl-Z FRC Team 4096

Replicating LabView code from 2015 competition.
Most of the real code is in teleop & auto modules.
"""

import logging
import time

import wpilib
import random
import teleop
import auto


#logger = logging.getLogger( 'robotpy' )


class MyRobot( wpilib.IterativeRobot ):

	def robotInit( self ):
		"""
		Called once at program startup
		"""
		# Two motors for now
		#self.drive = wpilib.RobotDrive( 0, 1, 2, 3 )
		self.drive = wpilib.RobotDrive( frontLeftMotor = 2, frontRightMotor = 3, rearLeftMotor = 0, rearRightMotor = 1 )
		self.drive.setInvertedMotor( 0, True )
		self.drive.setInvertedMotor( 1, True )
		
		# Two joystick drive
		#self.joystick0 = robotpy_ext.control.xbox_controller.XboxController( 0 )
		self.joystick_left = wpilib.Joystick( 0 )
		self.joystick_right = wpilib.Joystick( 1 )

		self.gamepad = wpilib.Joystick( 2 )

		# Lift motors
		self.lift_motor1 = wpilib.Talon( 4 )
		self.lift_motor2 = wpilib.Talon( 5 )
 
		# Clamp solenoids
		self.clamp_solenoid1 = wpilib.Solenoid( 0 )
		self.clamp_solenoid2 = wpilib.Solenoid( 1 )
		self.clamp_solenoid3 = wpilib.Solenoid( 2 )
		self.clamp_solenoid4 = wpilib.Solenoid( 3 )		

		# Misc
		self.log_interval = 0.25
		self.last_log_time = 0


	### Misc ###

	def log_info( self, message ):
		"""
		Logs info messages, generally to appear in the netconsole listener.
		Makes sure it only logs one message per interval, to prevent logging
		from slowing down the robot processing.
		"""
		cur_time = time.time( )

		if cur_time - self.last_log_time > self.log_interval:
			self.logger.info( message )
			self.last_log_time = cur_time


	### Disabled ###

	def disabledInit( self ):
		pass

	def disabledPeriodic( self ):
		pass


	### Autonomous ###

	def autonomousInit( self ):
		auto.init( self )

	def autonomousPeriodic( self ):
		auto.periodic( self )


	### Teleoperated ###

	def teleopInit( self ):
		teleop.init( self )

		# Gamepad
		#self.log_info( '----\ngp = {0:.2f},{1:.2f} - {2:.2f},{3:.2f}'.format( self.gamepad.getX( ), self.gamepad.getY( ), self.gamepad.getZ( ), self.gamepad.getRawAxis( 3 ) ) )
		#self.log_info( '----\ngp = {0:.2f},{1:.2f},{2:.2f},{3:.2f},{4}'.format( self.gamepad.getRawButton( 1 ), self.gamepad.getRawButton( 2 ), self.gamepad.getRawButton( 3 ), self.gamepad.getRawButton( 4 ), self.gamepad.getButtonCount( ) ) )

		#text = '---\n'
		#for i in range( 1, 13 ):
			#text += 'b{0} = {1}\n'.format( i, self.gamepad.getRawButton( i ) )
		#self.log_info( text )
		
		#print( 'joy10 =', self.joystick1.getRawAxis( 0 ) )

	def teleopPeriodic( self ):
		teleop.periodic( self )

	### Testing ###

	def testPeriodic( self ):
		wpilib.LiveWindow.run( )


### MAIN ###

if __name__ == "__main__":
	wpilib.run( MyRobot )
