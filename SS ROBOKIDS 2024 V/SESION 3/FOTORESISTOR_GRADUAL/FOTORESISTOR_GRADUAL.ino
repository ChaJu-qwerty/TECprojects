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
  // Leer el valor del fotoresistor que va entre 49 y 969 en este caso
  int sensorValue = analogRead(sensorPin);
  
  // Imprimir el valor leído en el monitor serie
  Serial.println(sensorValue);
  
  // Hace "equivalencias" de los valores que puede recolectar del foto resistor con los valores analogicos que puede tener un led
	int brillo = map(sensorValue,49,969,0,255);
  analogWrite(ledPin, brillo);
 
  
  // Esperar un momento antes de la siguiente lectura
  delay(100);
}