#include <LiquidCrystal.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

// Initializing LCD pin's
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// Initializing BNO055 Sensor
Adafruit_BNO055 bno = Adafruit_BNO055(55);

void setup() {
  // The baud rate for the sensor
  Serial.begin(9600);
  
  // Determines if the BNO055 Sensor is detected
  if(!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
  delay(1000);

  // If no errors, then the sensor is True
  bno.setExtCrystalUse(true);
  
  // set up the LCD's number of columns and rows:
  lcd.begin(20, 4);

  // Creating the constant for the BNO055 (Accelemeter, Gryoscope, and Magnometer)
  uint8_t system, gyro, accel, mag;
  system = gyro = accel = mag = 0;
  bno.getCalibration(&system, &gyro, &accel, &mag);

  // Creating the constant for the BNO055 (Temperature)
  int8_t  temp = bno.getTemp();
  
  // Setup for the BNO055 calibration setup (gryoscope, accelerometer, euler, and magnetometer)
//  while (True){
        // 
        // adafruit_bno055_offsets_t calibrationData;
        
//    }
}

void loop() {
  // Get the updated/new evented from the BNO055 sensor
  sensors_event_t event;
  bno.getEvent(&event);

  // Display the information (Column, Row) (First Information Title)
  lcd.setCursor(0, 0);
  lcd.print("Accelorometer");

  // Display the information (Column, Row) (Second Information X)
  lcd.setCursor(0, 1);
  lcd.print("X: ");
  lcd.setCursor(3, 1);
  lcd.print(event.orientation.x, 4);
  lcd.setCursor(15, 1);
  lcd.print("m/s^2");

  // Display the information (Column, Row) (Third Information Y)
  lcd.setCursor(0, 2);
  lcd.print("Y: ");
  lcd.setCursor(3, 2);
  lcd.print(event.orientation.y, 4);
  lcd.setCursor(15, 2);
  lcd.print("m/s^2");

  // Display the information (Column, Row) (Fourth Information Z)
  lcd.setCursor(0, 3);
  lcd.print("Z: ");
  lcd.setCursor(3, 3);
  lcd.print(event.orientation.z, 4);
  lcd.setCursor(15, 3);
  lcd.print("m/s^2");

  // A small delay for the SENSOR to the LCD
  delay(200);
}
