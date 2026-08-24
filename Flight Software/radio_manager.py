import busio 
import board
import digitalio
import adafruit_rfm9x

SPI = busio.SPI(
    clock = board.GP2,
    MOSI = board.GP3,   
    MISO = board.GP4
)

cs = digitalio.DigitalInOut(board.GP5)
reset = digitalio.DigitalInOut(board.GP6)

radio = adafruit_rfm9x.RFM9x(
    SPI, 
    cs,
    reset,
    915.0 )    #confirm frequency later

def send_data(data):
    try:
        message = "TEMP;{},PRESS{}".format(
            data["temperature"],
            data["pressure"]
        )
        message_bytes = message.encode("utf-8")
        radio.send(message_bytes)
    except Exception as problem:
        print(problem,"Radio transmission error")
