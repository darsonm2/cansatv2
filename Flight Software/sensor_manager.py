import busio
import board
import adafruit_bmp280

i2c = busio.I2C(
    scl=board.GP1,
    sda=board.GP0
)

bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

def get_readings():
    try:
        temperature = bmp280.temperature
        pressure = bmp280.pressure
    except RuntimeError:
#print() for ground testing and impossible numbers for errors in acutal run
        print("Sensor communication error")
        temperature = -999.0
        pressure = -999.0
#calculate pressure on ground        
    except Exception as problem:
        print(problem, "Error")
        temperature = -999.0
        pressure = -999.0
        
    data = {
        "temperature": temperature,
        "pressure": pressure
    }
        
    return data
