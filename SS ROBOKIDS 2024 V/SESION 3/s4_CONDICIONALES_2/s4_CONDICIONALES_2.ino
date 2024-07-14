const int ledRojo = 8;
const int ledVerde = 9;
const int ledAzul = 10;
const int pulsador = 11;

void setup() {
  pinMode(ledRojo, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  pinMode(ledAzul, OUTPUT);
  pinMode(pulsador, INPUT);
}

void loop() {
  int estadoPulsador = digitalRead(pulsador);

  switch (estadoPulsador) {
    case HIGH: // Si el pulsador está presionado
      digitalWrite(ledRojo, HIGH);
      digitalWrite(ledVerde, LOW);
      digitalWrite(ledAzul, LOW);
      break;
    case LOW: // Si el pulsador no está presionado
      digitalWrite(ledRojo, LOW);
      digitalWrite(ledVerde, HIGH);
      digitalWrite(ledAzul, LOW);
      break;
    default: // Estado por defecto (pulsador no conectado o mal conectado)
      digitalWrite(ledRojo, LOW);
      digitalWrite(ledVerde, LOW);
      digitalWrite(ledAzul, LOW);
  }
}