const int ledRojo = 8;
const int ledVerde = 9;
const int pulsador = 10;

void setup() {
  pinMode(ledRojo, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  pinMode(pulsador, INPUT);
}

void loop() {
  int estadoPulsador = digitalRead(pulsador);

  if (estadoPulsador == HIGH) { // Si el pulsador está presionado
    for (int i = 0; i < 10; i++) { // Bucle for que se repite 10 veces
      digitalWrite(ledRojo, HIGH); // Encendemos el LED rojo
      delay(500); // Esperamos 500 milisegundos
      digitalWrite(ledRojo, LOW); // Apagamos el LED rojo
      delay(500); // Esperamos 500 milisegundos
    }
  } else { // Si el pulsador no está presionado
    // No hacemos nada
  }
}