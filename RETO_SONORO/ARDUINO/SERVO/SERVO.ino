#include <Servo.h>

#include <Servo.h>

int PinServo = 9;
int anguloServo = 90;
Servo miMotor;
#include <Servo.h>
// C++ code
//
void setup()
{
  miMotor.attach(PinServo);
  Serial.begin(9600);
}

void loop()
{
  miMotor.write(anguloServo);
  delay(2000);
  miMotor.write(180);
  delay(2000);
}
