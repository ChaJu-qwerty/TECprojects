const int irPin = A0; // Pin analógico para sensor IR
int irValue;

void setup() {
  Serial.begin(9600);
}

void loop() {
  irValue = analogRead(irPin);
  Serial.print("IR Value: ");
  Serial.println(irValue);
  delay(500);
}