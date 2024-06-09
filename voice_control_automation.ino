void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();
    if (cmd == '1') {
      digitalWrite(2, HIGH);
    } else if (cmd == '2') {
      digitalWrite(2, LOW);
    } else if (cmd == '3') {
      digitalWrite(3, HIGH);
    } else if (cmd == '4') {
      digitalWrite(3, LOW);
    } else if (cmd == '5') {
      digitalWrite(4, HIGH);
    } else if (cmd == '6') {
      digitalWrite(4, LOW);
    } else if (cmd == '7') {
      digitalWrite(5, HIGH);
    } else if (cmd == '8') {
      digitalWrite(5, LOW);
    } else if (cmd == '9') {
      digitalWrite(2, LOW);
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
      digitalWrite(5, LOW);
    }
  }
}
