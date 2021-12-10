const int redPin = 3;
void setup() {
  Serial.begin(9600);
  pinMode(redPin, OUTPUT);
}
void loop() {
  while (Serial.available() > 0) {
    int red = Serial.parseInt();
    if (Serial.read() == '\n') {
      red = constrain(red, 0, 255);
      analogWrite(redPin, red);
      Serial.print(red);
      }
    }
}
