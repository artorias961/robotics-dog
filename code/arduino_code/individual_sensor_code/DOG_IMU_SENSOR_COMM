#include <Wire.h>
#include <LiquidCrystal.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>

//defining object of the Adafruit_BNO055 with a default address 0x55
Adafruit_BNO055 myIMU = Adafruit_BNO055(55, 0x28);
//Adafruit_BNO055 myIMU_bot = Adafruit_BNO055(56, 0x29);
//defining the Pins for the LED. If the LEDs are ON, then it means the Gyro or Accel is calibrated.
#define LED_Gyro 9
#define LED_Acc 10
//Define the variables:
bool calibrated = false;
uint8_t sys, gyro,accel, mg = 0; //intializeed system variables to 0
float thetaM; //angle of for the pitch from the accelerometer
float phiM;//angle for the roll from the accelerometer
float theta; //angle of for the pitch
float phi;//angle for the roll
float yaw; //angle of for the yaw
float dt;//time vectors
unsigned long millisOld; // old time being updated within dt

void setup() {
  //setting up serial monitor
  Serial.begin(9600);
  //Setting output pins for the two LEDS. When on, it will tell us if the sensor is calibrated
  pinMode(LED_Gyro, OUTPUT);
  pinMode(LED_Acc, OUTPUT);
  //turing on BNO055
  myIMU.begin();
  //myIMU_bot.begin();
  delay(1000);
  //dont use the crystal on chip, use the one on the board
  myIMU.setExtCrystalUse(true);
  //Start with the sensor calibration  
  while(calibrated == false){
    //get all and system calibrations
    myIMU.getCalibration(&sys, &gyro, &accel, &mg);
    //myIMU_bot.getCalibration(&sys2, &gyro2, &accel2, &mg2);
    if(gyro = 3){
      //If gyro sensor is fully calibrated then it will turn on an LED to indicate is calibrated.
      digitalWrite(LED_Gyro, HIGH);
    }
    if(accel == 3){
      //If Accelerometer sensor is fully calibrated then it will turn on an LED to indicate is calibrated.
      digitalWrite(LED_Acc, HIGH);
      //Since Calibrating the Accelerometer sensor takes longer and onces its fully calibrated, then it will get out from the while loop.
      calibrated = true;
      delay(3000);
    }
  }
  //Turn off the LEDS, so it doesn't consume any current.
  digitalWrite(LED_Gyro, LOW);
  digitalWrite(LED_Acc, LOW)
}

void loop() {
  //Accelerometer data: getting the data by vectors and using the period(dot) symbol to grab x, y or z data. These are raw data.
  imu::Vector<3> acc=myIMU.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  //Accordinng to our calculatins our pitch angle is theta = tan(ax/az). Divede by 9.8 to normalize everything to 1g
  thetaM = atan2(acc.x() / 9.8, acc.z() / 9.8) / 2 / 3.1415 * 360;
  phiM = atan2(acc.y() / 9.8, acc.z() / 9.8) / 2 / 3.1415 * 360;
  //Gyroscope data: getting the data by vectors and using the period(dot) symbol to grpb x, y, and z data. These are raw data.
  imu::Vector<3> gyros=myIMU.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE)
  //Since the raw data from gyro is deg/sec then we multiply dt, which is in sec, to the raw data to get degree. 
  dt=(millis()-millisOld)/1000.;
  millisOld=millis();
  //Pitch:
  theta = (theta - gyros.y() * dt) * .60 + thetaM * .40;
  //Roll:
  phi = (phi + gyros.x() * dt) * .60 + phiM * .40; 
  //Yaw:
  yaw = gyros.z();
  
  delay(50);
}
