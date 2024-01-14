/**
 * This program is used to control the amount of spray produced by scent viles.
 */


// Pin used to intercept the on/off behavior of the diffuser boards.
const int optoPin = 5; 

/**
 * Set up the connection.
 */
void setup() {
  // Set the optocoupler pin as the output.
  Serial.begin(115200);
  pinMode(optoPin, OUTPUT);
}

/**
 * Activate the optocupler
 */
void loop() {

  // Set the pin
  digitalWrite(5, LOW);
  delay(3000);

  // Activate the optocoupler (pull high and wait to activate)
  digitalWrite(optoPin, HIGH);
  delay(60000);
}
