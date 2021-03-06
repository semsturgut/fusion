// Gyro degerleri sapitiyor.
#include "mbed.h"
#include "COMPASS_DISCO_L476VG.h"
#include "GYRO_DISCO_L476VG.h"

Serial serialPort(PA_0, PA_1);
GYRO_DISCO_L476VG gyro;
COMPASS_DISCO_L476VG compass;

int main() {
  int16_t accData[3];
  float gyroData[3];

  while (true) {
    wait(0.1);
    gyro.GetXYZ(gyroData);
    compass.AccGetXYZ(accData);
    // serialPort.printf("\r\n AX:%d AY:%d AZ:%d", accData[1], accData[2], accData[3]);
    serialPort.printf("\r\n GX:%d GY:%d GZ:%d", gyroData[1], gyroData[2], gyroData[3]);
    // serialPort.printf("%d\r\n",gyroData[1]);
  }
    return 0;
}
