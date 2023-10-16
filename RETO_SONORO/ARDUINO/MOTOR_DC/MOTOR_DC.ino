//cosa basicona para el motor dc
int speedPin = 11;
int dirPin1 = 12;
int dirPin2 = 13;
int velocidad = 255;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(speedPin,OUTPUT);//el pin va a enviar la informacion al driver
pinMode(dirPin1,OUTPUT);
pinMode(dirPin2,OUTPUT);
} 

void loop() {
  // put your main code here, to run repeatedly:
//primero le vamos a decir en que direccion va a ir
digitalWrite(dirPin1,HIGH);
digitalWrite(dirPin2,LOW);
//ahora le mandamos la velocidad
analogWrite(speedPin,velocidad);
}
