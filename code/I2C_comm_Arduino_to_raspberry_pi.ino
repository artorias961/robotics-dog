/*
  Arduino Slave for Raspberry Pi Master
  i2c_slave_ard.ino
  Connects to Raspberry Pi via I2C
  
  DroneBot Workshop 2019
  
*/
 
// Include the Wire library for I2C
#include <Wire.h>
 
int n;
 
void setup() {
  // Join I2C bus as slave with address 8
  Wire.begin(0x8);
  
  // Call receiveEvent when data received                
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvents);
}
 
// Function that executes whenever data is received from master
void receiveEvent(int howMany) 
{
  n = Wire.read(); // receive byte as a character
  Serial.print("Recieved data from Master: ");Serial.println(n);
}

void requestEvents()
{
  Serial.print("sending value : ");Serial.println(n);
  Wire.write(n);
}
void loop() {
  delay(100);
}