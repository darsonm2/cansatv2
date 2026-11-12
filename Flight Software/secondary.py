import Controller
import math
LOOP_TIME = 0.01


target_tilt = 0
pitch_controller = Controller(kP=0, kI=0.0, kD=0.0, kG=0.0, kS=0.0)
roll_controller = Controller(kP=0, kI=0.0, kD=0.0, kG=0.0, kS=0.0)
while True:
    local_pitch = math.sin()

    pitch_correction_power = pitch_controller.output(target_tilt, local_pitch)
    roll_correction_power = roll_controller.output(target_tilt, local_roll)

