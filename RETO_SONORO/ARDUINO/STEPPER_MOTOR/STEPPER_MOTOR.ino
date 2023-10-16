#include <Stepper.h>
int PasosPorRevolucion = 2048; //cuando pasos necesita nuestro motor para dar una vuelta; documentacion
int StepperVel = 10; //en rovoluciones por minuto
Stepper myStepper(PasosPorRevolucion,8,10,9,11);

void setup() {
  // put your setup code here, to run once:
myStepper.setSpeed(StepperVel);
}

void loop() {
  // put your main code here, to run repeatedly:
myStepper.step(PasosPorRevolucion);
}
