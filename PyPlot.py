import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("sampleText.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

# import serial
# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.animation as animation
# import time

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
# serialFile = open("sampleText.txt", "r+")

# def animate(serialFile):
#     pullData = serialFle.read()
#     dataArray = pullData.split('\n')
#     xar = []
#     yar = []
#     for eachLine in dataArray:
#         if len(eachLine)>1:
#             x,y = eachLine.split(',')
#             xar.append(int(x))
#             yar.append(int(y))
#             ax1.clear()
#             ax1.plot(xar,yar)

# def portCheck(serialFile):
#     serialPort = serial.Serial(
#         port='/dev/tty.usbserial-FTVTZPQN',
#         baudrate=9600,
#         parity=serial.PARITY_NONE,
#         stopbits=serial.STOPBITS_ONE,
#         bytesize=serial.EIGHTBITS,
#         timeout=0.5)
#     main(serialPort, serialFile)

# def main(serialPort, serialFile):
#     i=1
#     while True:
#         if serialPort.isOpen():
#             line = serialPort.readline()
#             # print line
#             serialFile.write(str(i)+","+line+"\n")
#             i = i + 1
#             ani = animation.FuncAnimation(fig, animate(serialFle), interval=1000)
#             plt.show()
            
# try:
#     portCheck(serialFile)
# except KeyboardInterrupt:
#     print 'Interrupted!'
