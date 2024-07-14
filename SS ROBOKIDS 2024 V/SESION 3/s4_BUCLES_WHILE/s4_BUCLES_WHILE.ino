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
    int contador = 0; // Variable para contar las iteraciones
    while (contador < 10) { // Bucle while que se repite hasta que `contador` llegue a 10
      digitalWrite(ledRojo, HIGH); // Encendemos el LED rojo
      delay(500); // Esperamos 500 milisegundos
      digitalWrite(ledRojo, LOW); // Apagamos el LED rojo
      delay(500); // Esperamos 500 milisegundos
      contador++; // Incrementamos el contador
    }
  } else { // Si el pulsador no está presionado
    // No hacemos nada
  }
}
