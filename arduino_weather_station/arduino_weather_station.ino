///////humidity and temperature///////
#include "DHT.h"             // DHT sensors library
#define dhtPin 8             // This is data pin
#define dhtType DHT11        // This is DHT 11 sensor
DHT dht(dhtPin, dhtType);    // Initialising the DHT library
float humValue;           // value of humidity
float temperatureValueC;  // value of temperature in degrees Celcius
///////humidity and temperature///////

///////rain///////
int pinRain = A0;
int LEDGreen = 6;
int LEDRed = 7;
int targetValue = 500;
///////rain///////

///////photoresister///////
int pinLED = 2;
int pinPhotoresister = A1;
int photoresisterValue = 300;
///////photoresister///////

void setup(){
  Serial.begin(9600);
///////humidity and temperature///////
  dht.begin();               // start reading the value from DHT sensor
///////humidity and temperature///////

///////rain///////
  pinMode(pinRain, INPUT);
  pinMode(LEDGreen, OUTPUT);
  pinMode(LEDRed, OUTPUT);
  digitalWrite(LEDGreen, LOW);
  digitalWrite(LEDRed, LOW);
///////rain///////

///////photoresister///////
  pinMode(pinLED, OUTPUT);              //initialize the pinLED as an output
  pinMode(pinPhotoresister, INPUT);     //initialize the pinPhotoresister as an output  
///////photoresister///////
}

void loop() {
///////humidity and temperature///////
  humValue = dht.readHumidity();               // value of humidity
  temperatureValueC = dht.readTemperature();   // value of temperature in degrees Celcius
  Serial.print(humValue);     // get value of humidity
  Serial.print(" , ");          // create space after the value of humidity
  Serial.print(temperatureValueC);  // get value of temperature in degrees Celcius
///////humidity and temperature///////

///////rain///////
  int rainSensor = analogRead(pinRain);
  Serial.print(" , ");          // create space
  Serial.print(rainSensor);
  if(rainSensor < targetValue){
    digitalWrite(LEDGreen, LOW);
    digitalWrite(LEDRed, HIGH);
  }
  else {
    digitalWrite(LEDGreen, HIGH);
    digitalWrite(LEDRed, LOW);
  }
///////rain///////

///////photoresister///////
  int photoresisterStatus = analogRead(pinPhotoresister);
  Serial.print(" , ");          // create space
  Serial.print(photoresisterStatus);
  if(photoresisterStatus <= photoresisterValue){
    digitalWrite(pinLED, HIGH);
    delay(1000);
    digitalWrite(pinLED, LOW);
    delay(1000);
    Serial.print(" , ");          // create space
    Serial.println("LED ON");
  }
  else {
    digitalWrite(pinLED, LOW);
    Serial.print(" , ");          // create space
    Serial.println("LED OFF");
  }
///////photoresister///////
  delay(1000);
}
