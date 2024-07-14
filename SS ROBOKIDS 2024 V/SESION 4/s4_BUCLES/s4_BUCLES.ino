for (int i = 0; i < 4; i++) {
  // Mover hacia adelante
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  delay(1000);
  // Girar
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, HIGH);
  delay(500);
}
