import busio
import board
import adafruit_bmp280

i2c = busio.I2C(
    scl = board.GP1,
    sda = board.GP0
)

bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

def get_readings():
    try:
        temperature = bmp280.temperature
        pressure = bmp280.pressure
    except RuntimeError:
        print("Sensor communication error")
        temperature = None
        pressure = None
    except Exception as problem:
        print(problem, "Error")
        temperature = None
        pressure = None
    # Can add data validity later on after figuring out the bounds
    data = {
        "temperature": temperature,
        "pressure": pressure
    }
    
    return data