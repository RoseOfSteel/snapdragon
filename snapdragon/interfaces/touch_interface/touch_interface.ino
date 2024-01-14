/**
 * This code is used to control multiple vibration motors.
 * It pulses each motore based on a low or high signal and pauses in between.
 */


/**
 * Configure the pins for each motor.
 */
void setup() {
  Serial.begin(115200);
  pinMode(5, OUTPUT);
  pinMode(15, OUTPUT);
}

/**
 * Pulse each motor.
 */
void loop() {
  digitalWrite(5, LOW);
  digitalWrite(15, LOW);
  delay(3000);
  digitalWrite(5, HIGH);
  digitalWrite(15, HIGH);
  delay(3000);
}
