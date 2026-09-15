import storage
import board
import digitalio

jumper = digitalio.DigitalInOut(board.GP7)
jumper.direction = digitalio.Direction.INPUT
jumper.pull = digitalio.Pull.UP

if jumper.value:
    storage.remount("/", readonly=False)
