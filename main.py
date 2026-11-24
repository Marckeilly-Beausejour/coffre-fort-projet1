import machine
import time
from Pins import Pins
# Assignation de variable

# Capteur RFID
RFID_SDA = machine.Pin(Pins.D10)
RFID_SCK =  machine.Pin(Pins.D13)
RFID_MOSI =  machine.Pin(Pins.D11)
RFID_RST =  machine.Pin(Pins.D12)

# Servo
servo =  machine.Pin(Pins.D5)

# Buzzer
buzzer =  machine.Pin(Pins.D6)

# Reed Switch
reed_switch =  machine.Pin(Pins.D7)

# Traffic Light
TL_Vert =  machine.Pin(Pins.D3)
TL_Jaune =  machine.Pin(Pins.D4)
TL_Rouge =  machine.Pin(Pins.D5)

# Écran
ecran_SDA =  machine.Pin(Pins.A4)
ecran_SCL =  machine.Pin(Pins.A5)

# Potentiomètre
potentiometre =  machine.Pin(Pins.A0)