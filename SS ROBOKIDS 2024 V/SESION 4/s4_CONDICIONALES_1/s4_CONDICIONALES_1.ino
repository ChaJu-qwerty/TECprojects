const int ledRojo = 8; // Pin del LED rojo
const int ledVerde = 9; // Pin del LED verde
const int pulsador = 10; // Pin del pulsador

void setup() {
  pinMode(ledRojo, OUTPUT); // Configuramos el pin del LED rojo como salida
  pinMode(ledVerde, OUTPUT); // Configuramos el pin del LED verde como salida
  pinMode(pulsador, INPUT); // Configuramos el pin del pulsador como entrada
}

void loop() {
  int estadoPulsador = digitalRead(pulsador); // Leemos el estado del pulsador

  if (estadoPulsador == HIGH) { // Si el pulsador está presionado
    digitalWrite(ledRojo, HIGH); // Encendemos el LED rojo
    digitalWrite(ledVerde, LOW); // Apagamos el LED verde
  } else { // Si el pulsador no está presionado
    digitalWrite(ledRojo, LOW); // Apagamos el LED rojo
    digitalWrite(ledVerde, HIGH); // Encendemos el LED verde
  }
}