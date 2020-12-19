#include <SoftwareSerial.h>
SoftwareSerial softSerial(0,1);
#include <pcmConfig.h>// library of speaker
#include <pcmRF.h> //"
#include <TMRpcm.h>//"
#include <SD.h> //sd card module library
// cs 4
// sck 13
// mosi 11
// miso 12
#define SD_ChipSelectPin 10
//#define sp 9

TMRpcm tmrpcm;

void setup(){
tmrpcm.speakerPin = 9;
Serial.begin(9600);
if (!SD.begin(SD_ChipSelectPin)) {
Serial.println("SD fail");
return;
}
}

void loop(){ 
  if(Serial.available())
  { if(Serial.read())
  {tmrpcm.setVolume(5);
tmrpcm.play("Dndnha.Com.Hassan.Shakosh.Ft.Omar.Kamal.Han3mal.Lagbtita.wav");}}
}
