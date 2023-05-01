#include <SoftwareSerial.h>
#include <Adafruit_GPS.h>

// Define RX/TX pins
#define RX_PIN 0
#define TX_PIN 1

// Initialize GPS module
SoftwareSerial GPSSerial(RX_PIN, TX_PIN);
Adafruit_GPS GPS(&GPSSerial);

// Set GPSECHO to 'false' to turn off echoing the GPS data to the Serial console
// Set to 'true' if you want to debug and listen to the raw GPS sentences
#define GPSECHO false

uint32_t timer = millis();

void setup()
{
  // Connect to the Serial Monitor
  Serial.begin(115200);
  while (!Serial);

  // Connect to the GPS module
  GPSSerial.begin(9600);
  
  // Wait for GPS module to initialize
  delay(1000);
  
  // Turn on RMC (recommended minimum) and GGA (fix data) including altitude
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  
  // Set the update rate
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ); // 1 Hz update rate
  
  // Request updates on antenna status, comment out to keep quiet
  GPS.sendCommand(PGCMD_ANTENNA);
  
  // Ask for firmware version
  GPSSerial.println(PMTK_Q_RELEASE);
}

void loop() // run over and over again
{
  // Read data from the GPS module
  char c = GPS.read();
  
  // If GPSECHO is true, print the GPS data to the Serial Monitor
  if (GPSECHO)
  {
    if (c) Serial.print(c);
  }
  
  // If a sentence is received, check the checksum and parse it
  if (GPS.newNMEAreceived())
  {
    if (!GPS.parse(GPS.lastNMEA()))
    {
      return;
    }
  }
  
  // Print out the current stats approximately every 2 seconds or so
  if (millis() - timer > 2000)
  {
    timer = millis(); // reset the timer
    
    Serial.print("\nTime: ");
    if (GPS.hour < 10) { Serial.print('0'); }
    Serial.print(GPS.hour, DEC); Serial.print(':');
    if (GPS.minute < 10) { Serial.print('0'); }
    Serial.print(GPS.minute, DEC); Serial.print(':');
    if (GPS.seconds < 10) { Serial.print('0'); }
    Serial.print(GPS.seconds, DEC); Serial.print('.');
    if (GPS.milliseconds < 10) { Serial.print("00"); }
    else if (GPS.milliseconds > 9 && GPS.milliseconds < 100) { Serial.print("0"); }
    Serial.println(GPS.milliseconds);
    
    Serial.print("Date: ");
    Serial.print(GPS.day, DEC); Serial.print('/');
    Serial.print(GPS.month, DEC); Serial.print("/20");
    Serial.println(GPS.year, DEC);
    
    Serial.print("Fix: "); Serial.print((int)GPS.fix);
    Serial.print(" quality: "); Serial.println((int)GPS.fixquality);
    if (GPS.fix)
    {
      Serial.print("Location: ");
      Serial.print(GPS.latitude, 4); Serial.print(GPS.lat);
      Serial.print(", ");
      Serial.print(GPS.longitude, 4); Serial.println(GPS.lon);
      Serial.print("Speed (knots): "); Serial.println(GPS.speed);
      Serial.print("Angle: "); Serial.println(GPS.angle);
      Serial.print("Altitude: "); Serial.println(GPS.altitude);
      Serial.println((int)GPS.satellites);
}}}
