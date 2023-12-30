int ledPin = 22;  // Replace with your actual LED pin
int receivedNumber = 0;


void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);  // Should match the baud rate used in the Python code
}

void loop() {
  // Check if data is available to read from serial
  if (Serial.available() > 0) {
    // Read the incoming number
    receivedNumber = Serial.read() - '0';
    
    // Blink the LED according to the received number

    for (int i = 0; i < receivedNumber ; ++i) {
      
      digitalWrite(ledPin, HIGH);
      delay(1000);
      digitalWrite(ledPin, LOW);
      delay(1000);
   
    }
  }
}
