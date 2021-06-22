#include <Servo.h> 
Servo myservo;  // create servo object to control a servo
int pos = 0;

void setup()
{
  Serial.begin(9600);
  myservo.attach(3);
  myservo.write(pos);
}

void loop()
{

   if(Serial.available()){
    char char_data=Serial.read(); //read one byte from serial buffer and save it to the variable
    if(char_data=='o')
    {
      openlock();
    }
    else if(char_data=='c')
    {
      closelock();
    }
    delay(500);
  }
}

void openlock()
{
  if(pos==0)
  {
    pos=90;
    myservo.write(pos);
    Serial.println("DOOR OPEN");
  }
  else
  {
    Serial.println("DOOR ALREADY OPEN");
  }
}

void closelock()
{
  if(pos==90)
  {
    pos=0;
    myservo.write(pos);
    Serial.println("Door CLOSED");
  }
  else
  {
    Serial.println("DOOR ALREADY CLOSED");
  }
}
