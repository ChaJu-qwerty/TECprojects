// Definir los pines para el sensor ultrasónico
const int trigPin = 7;
const int echoPin = 6;

// Variables para almacenar la duración del pulso y la distancia calculada
long duration;
int distance;

void setup() {
  Serial.begin(9600); // Iniciar la comunicación serial para la depuración
  pinMode(trigPin, OUTPUT); // Configurar el pin TRIG como salida
  pinMode(echoPin, INPUT); // Configurar el pin ECHO como entrada
}

void loop() {
  // Generar un pulso corto en el pin TRIG
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Medir el tiempo que tarda en llegar el eco
  duration = pulseIn(echoPin, HIGH);
  
  // Calcular la distancia en centímetros
  	//la velocidad del sonido en el aire es de aprox 343 m/s que es aprox a 0.0343 cm/micro seg
  	//se divide entre 2 porque el ECHO "recorre" dos veces la distancia
  distance = duration * 0.034 / 2;
  
  // Mostrar la distancia en el monitor serie
  Serial.print("Distancia: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  // Esperar un momento antes de realizar la siguiente lectura
  delay(1000);
}