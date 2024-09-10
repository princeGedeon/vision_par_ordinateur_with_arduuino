#include <cvzone.h>

SerialData serialData(1,1);
int valsRec[1];
int led = 8;

void setup() {
  serialData.begin();
  pinMode(led, OUTPUT);
 

void loop() {
 serialData.Get(valsRec);
   digitalWrite(red, valsRec[0]);
}
