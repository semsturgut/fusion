import serial
import time 

def portCheck():
    serialPort = serial.Serial(
        port='/dev/tty.usbserial-FTVTZPQN',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0.5)
    main(serialPort)

def main(serialPort):
    i=1
    line = ''
    while True:
        if serialPort.isOpen():
            if i == 1:
                line = serialPort.readline()
                line = "511\r\n"
            else:
                line = serialPort.readline()
            print line
            serialFile = open("sampleText.txt","a")
            serialFile.write(str(i)+","+line)
            i = i + 1
            
try:
    portCheck()
except KeyboardInterrupt:
    print 'Interrupted!'

    
