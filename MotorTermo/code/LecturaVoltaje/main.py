import serial
import matplotlib as plt
import numpy
from drawnow import *


arduinoData = serial.Serial('/dev/ttyACM0',9600)
listaVoltaje = []

def main():

    while (arduinoData.inWaiting()==0):
        pass

    arduinoString = arduinoData.readline()
    print(arduinoString)
    voltaje = float(arduinoString)
    listaVoltaje.append(voltaje)

    main()

if __name__== "__main__":
    main()