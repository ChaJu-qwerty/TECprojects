#include <IRremote.h>

// Pines de motores
const int motorAForward = 2;
const int motorABackward = 3;
const int motorBForward = 4;
const int motorBBackward = 5;

// Pin del receptor IR
const int RECV_PIN = 11;

// Crear el objeto receptor IR
IRrecv irrecv(RECV_PIN);
decode_results results;

void setup() {
  // Configurar pines de motores como salidas
  pinMode(motorAForward, OUTPUT);
  pinMode(motorABackward, OUTPUT);
  pinMode(motorBForward, OUTPUT);
  pinMode(motorBBackward, OUTPUT);

  // Iniciar el receptor IR
  irrecv.enableIRIn();
  Serial.begin(9600);
}

void loop() {
  if (irrecv.decode(&results)) {
    unsigned long value = results.value;

    // Imprimir el valor recibido
    Serial.println(value, HEX);

    // Decodificar las señales del control remoto y controlar los motores
    switch (value) {
      case 0xFFA25D: // Botón "Adelante"
        moveForward();
        break;
      case 0xFF629D: // Botón "Atrás"
        moveBackward();
        break;
      case 0xFFE21D: // Botón "Izquierda"
        turnLeft();
        break;
      case 0xFF22DD: // Botón "Derecha"
        turnRight();
        break;
      case 0xFF02FD: // Botón "Stop"
        stopMotors();
        break;
      default:
        stopMotors();
        break;
    }
    irrecv.resume(); // Recibir la siguiente señal
  }
}

// Funciones para mover el robot
void moveForward() {
  digitalWrite(motorAForward, HIGH);
  digitalWrite(motorABackward, LOW);
  digitalWrite(motorBForward, HIGH);
  digitalWrite(motorBBackward, LOW);
}

void moveBackward() {
  digitalWrite(motorAForward, LOW);
  digitalWrite(motorABackward, HIGH);
  digitalWrite(motorBForward, LOW);
  digitalWrite(motorBBackward, HIGH);
}

void turnLeft() {
  digitalWrite(motorAForward, LOW);
  digitalWrite(motorABackward, HIGH);
  digitalWrite(motorBForward, HIGH);
  digitalWrite(motorBBackward, LOW);
}

void turnRight() {
  digitalWrite(motorAForward, HIGH);
  digitalWrite(motorABackward, LOW);
  digitalWrite(motorBForward, LOW);
  digitalWrite(motorBBackward, HIGH);
}

void stopMotors() {
  digitalWrite(motorAForward, LOW);
  digitalWrite(motorABackward, LOW);
  digitalWrite(motorBForward, LOW);
  digitalWrite(motorBBackward, LOW);
}