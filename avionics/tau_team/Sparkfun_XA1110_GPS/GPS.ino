//////////////////////////////////ISP_Avionics//////////////////////////////////
/*  Created: 3.5.20 by Blake Shaffer
 *     Name: GPS
 * Function: Connects Teensy 3.2 to SparkFun GPS Breakout - XA1110 
 *    Notes: Need to install 2 libraries. SparkFun lib can be found in the 
 *           lib manager. TinyGPS can be found here:
 *            https://github.com/mikalhart/TinyGPSPlus
 *           The SparkFun lib is for grabbing the data from the GPS in the 
 *           standard NMEA format. The TinyGPS++ lib parses this data into a 
 *           much more friendly format for display/manipulation.
 *  Updates: 
 */
///////////////////////////////////Libraries!///////////////////////////////////
#include <SparkFun_I2C_GPS_Arduino_Library.h>  //lib for grabbing data from GPS
#include <TinyGPS++.h>                         //parses NMEA data SUPER nicely

/////////////////////////////Variables and #Defines/////////////////////////////
#define sm Serial  //define 'sm' so you dont type 'Serial1' every time

I2CGPS myI2CGPS;   //hook object to SparkFun lib
TinyGPSPlus gps;   //declare gps object to call methods on

//////////////////////////////////////MAIN//////////////////////////////////////
void setup(){
  sm.begin(9600);  //begin serial comm w/ arduino serial monitor
  sm.println("GPS DATA READING PROGRAM");

  while(true){
    if (myI2CGPS.begin() == false){
      sm.println("Module failed to respond. Please check wiring.");
      delay(500);  //wait 0.5s to check again
    }
    else{
      sm.println("GPS module found!");
      break;
    }
  }
}

void loop(){
  //available() rets num of new GPS bytes available
  while (myI2CGPS.available()){   
    gps.encode(myI2CGPS.read());  //feed GPS parser
  }
  
  //Check to see if new GPS info is available
  if (gps.time.isUpdated()){ 
    displayInfo();  //print formatted data to serial monitor
  }
}

///////////////////////////////////Functions!///////////////////////////////////
/*******************************************************************************
* Description: Prints GPS time, date, lat/long, speed, and course.
*       Input: VOID
*  Out/Modify: VOID
*******************************************************************************/
void displayInfo(){
  //print date/time info
  if (gps.time.isValid()){
    sm.print(F("Date: ")); 
    sm.print(gps.date.month());  sm.print(F("/"));
    sm.print(gps.date.day()  );  sm.print(F("/"));
    sm.print(gps.date.year() );  sm.println();

    sm.print(("Time: "));
    if (gps.time.hour() < 10)    sm.print(F("0")); 
    sm.print(gps.time.hour());   sm.print(F(":"));
    if (gps.time.minute() < 10)  sm.print(F("0"));
    sm.print(gps.time.minute()); sm.print(F(":"));
    if (gps.time.second() < 10)  sm.print(F("0"));
    sm.print(gps.time.second()); sm.println();
  }
  else sm.println(F("Time not yet valid"));
  
  //print lat/long info
  if (gps.location.isValid()){
    sm.print("Location: ");
    sm.print(gps.location.lat(), 6);  sm.print(F(", "));
    sm.print(gps.location.lng(), 6);  sm.println();
  }
  else sm.println(F("Location not yet valid"));

  //print speed info
  if (gps.speed.isValid()){
    sm.print("mph: ");  sm.print(gps.speed.mph(), 6);   sm.print(F(", "));
    sm.print("kmph: "); sm.print(gps.speed.kmph(), 6);  sm.print(F(", "));
    sm.print("mps: ");  sm.print(gps.speed.mps(), 6);   sm.println();
  }
  else sm.println(F("Speed not yet valid"));
  
  //print direction info
  if (gps.course.isValid()){
    sm.print("Degrees: ");  sm.print(gps.course.deg(), 6); sm.print(F(", "));
    sm.print("Cardinal: "); sm.println(gps.cardinal(gps.course.deg()));
  }
  else sm.println(F("Course not yet valid"));

  sm.println(); //print blank line
}

/*******************************************************************************
* Description: 
*       Input: 
*  Out/Modify: 
*******************************************************************************/

//////////////////////////////////ISP_Avionics//////////////////////////////////
