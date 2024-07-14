if (distance < 20) {
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
} else {
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
}
