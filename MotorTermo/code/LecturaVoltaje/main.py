import serial
import matplotlib as plt
import numpy
from drawnow import *

plt.ion()  #Activate Interactive Plot on matplotlib


#arduinoData = serial.Serial('/dev/ttyACM0',9600)   #Linux
arduinoData = serial.Serial('COM3' ,9600)   #Windows
listaVoltaje = []

def graficar():
    plt.plot(listaVoltaje)


def main():

    while (arduinoData.inWaiting()==0):
        pass

    arduinoString = arduinoData.readline()
    #print(arduinoString)
    voltaje = float(arduinoString)
    print(voltaje)
    listaVoltaje.append(voltaje)

    drawnow(graficar)


    main()

if __name__== "__main__":
    main()