#include <VarSpeedServo.h>

VarSpeedServo servo1;
VarSpeedServo servo2;
VarSpeedServo servo3;
int Pinservo1=9;
int Pinservo2=10;
int Pinservo3=11;

void setup() {
  // put your setup code here, to run once:
servo1.attach(Pinservo1);
servo2.attach(Pinservo2);
servo3.attach(Pinservo3);

//como estaran al inicio
servo1.write(0,150,true); //angulo, velocidad, va a esperar a que este en 0 para la siguiente linea
servo2.write(0,150,true);
}

void loop() {
  // put your main code here, to run repeatedly:
servo1.write(90,150,true);
servo1.write(0,100,true);
servo2.write(90,150,true);
servo2.write(0,150,false);
servo3.write(90,150,true);
servo3.write(0,150,false);
delay(3000);

}
