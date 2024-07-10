// Definir los pines
const int sensorPin = A0;  // Pin analógico donde está conectado el fotoresistor
const int ledPin = 10;     // Pin digital donde está conectado el LED

void setup() {
  // Configurar el pin del LED como salida
  pinMode(ledPin, OUTPUT);
  
  // Iniciar la comunicación serie para depuración
  Serial.begin(9600);
}

void loop() {
  // Leer el valor del fotoresistor
  int sensorValue = analogRead(sensorPin);
  
  // Imprimir el valor leído en el monitor serie
  Serial.println(sensorValue);
  
  // Encender el LED si el valor del sensor es menor a un umbral
  if (sensorValue > 100) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
  
  // Esperar un momento antes de la siguiente lectura
  delay(100);
}