// Create IO pins and variables used in program

// Reaction time experiment of one LED.


// Button variables
int buttonPin = 2;
int buttonState = LOW;
int data;
// Time variables
long newT;
long oldT;
long deltaT;
//bool inProgress; 
//int count = 0;
// The setup function runs once when press reset or power the board.
void setup() {

  //initialize button pin as input.
  pinMode(buttonPin, INPUT);

  //initialize serial communication.
  Serial.begin(9600);
  
}

// The loop function runs over and over again forever until the arduino loses power
void loop() {

  //Always check to see if button is pressed
  buttonState = digitalRead(buttonPin);

  //Criteria for trial end.
  if(buttonState == HIGH) {
    //count++;
    Serial.write('A');
    delay(1000);
  }


}
