#include <cvzone.h>
SerialData serialdata(6,1);
int led1=2;
int led2=4;
int led3=7;
int led4=8;
int led5=13;
int led6=12;
int data[6];
void setup() {
  // put your setup code here, to run once:
serialdata.begin(9600);
pinMode(led1,OUTPUT);
pinMode(led2,OUTPUT);
pinMode(led3,OUTPUT);
pinMode(led4,OUTPUT);
pinMode(led5,OUTPUT);
pinMode(led6,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
serialdata.Get(data);
digitalWrite(led1,data[0]);
digitalWrite(led2,data[1]);
digitalWrite(led3,data[2]);
digitalWrite(led4,data[3]);
digitalWrite(led5,data[4]);
digitalWrite(led6,data[5]);

}
