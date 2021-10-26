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
int pinLED = 3;
int pinPhotoresister = A1;
int photoresisterValue = 300;
///////photoresister///////

///////wind speed///////
int interruptPin = 2;
float revolutions=0;
int rpm=0; // max value 32,767 16 bit
int revo = 0;
long  startTime=0;
long  elapsedTime;
int anemometerRadius = 6;    //unit is "inch"
int diameter = 2;
int anemometerDiameter = diameter * anemometerRadius;   //(2*6) unit is "inch"
float piValue = 3.142;    //value of pi
float inchesKilometer = 39370.1;
float anemometerCircumference = anemometerDiameter * piValue;   //unit is "inch"
float circumferenceRpm = 0.00;
float divideInches = 0.00;
float speedOfAir = 0.00;
//const byte            ah3582_pin = 2;   // used for interrupt, 2 or 3 for Nano/ATmega328
//const unsigned int    period     = 2000; // measurement period in ms
//volatile unsigned int pulses;           // 1 per rotation, used in ISR, hence volatile
///////wind speed///////

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

///////wind speed///////
  pinMode(interruptPin, INPUT);           // set pin to input
//  pinMode(ah3582_pin, INPUT); 
//  attachInterrupt(digitalPinToInterrupt(ah3582_pin), ah3582InterruptPin, FALLING);
///////wind speed///////
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
//    delay(1000);
//    digitalWrite(pinLED, LOW);
//    delay(1000);
    Serial.print(" , ");          // create space
    Serial.print("LED ON");
  }
  else {
    digitalWrite(pinLED, LOW);
    Serial.print(" , ");          // create space
    Serial.print("LED OFF");
  }
///////photoresister///////

///////wind speed///////
  revolutions=0; 
  rpm=0;
  revo = 0;
  circumferenceRpm = 0.00;
  divideInches = 0.00;
  speedOfAir = 0.00;
  startTime=millis();         
  attachInterrupt(digitalPinToInterrupt(interruptPin),interruptFunction,RISING);
  delay(3000);
  detachInterrupt(interruptPin);                
//now let's see how many counts we've had from the hall effect sensor and calc the RPM
  elapsedTime=millis()-startTime;     //finds the time, should be very close to 1 sec
  if(revolutions>0) {
    rpm=(max(1, revolutions) * 60000) / elapsedTime;        //calculates rpm
    revo = revolutions;
    circumferenceRpm = anemometerCircumference * rpm;       //unit is "inches per minute"
    divideInches = circumferenceRpm / inchesKilometer;      //unit is "kilometer per minute"
    speedOfAir = divideInches * 60;                  //unit is "kilometer per hour"
    }
  Serial.print(" , ");          // create space
  Serial.print(revo);
  Serial.print(" , ");          // create space
  Serial.print(rpm);
  Serial.print(" , ");          // create space
  Serial.println(speedOfAir);
//  unsigned int pulses_read;
//  pulses = 0; 
//  delay(period);
//  pulses_read = pulses;
//  Serial.print(" , ");          // create space
//  Serial.print((unsigned long)pulses_read); // revolutions
//  Serial.print(" , ");          // create space
//  Serial.println(((unsigned long)pulses_read * 60000) / period); // RPM
///////wind speed///////
  delay(3000);
}
void interruptFunction() //interrupt service routine
{  
  revolutions++;
}
//void ah3582InterruptPin()
//{
//   pulses++;
//}
