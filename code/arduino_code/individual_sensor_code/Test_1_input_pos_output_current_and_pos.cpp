#include <Servo.h>
#include <LiquidCrystal.h>
#include <math.h>

//----------------------------Variable Setup-------------------------------
Servo servo_test_1;
int cs_pin = A1;
int fbservo_pin = A0;
int input_pos = 0;
int index = 0;
int pos_check;
int ADC_servo;
int ADC_current;
int fb_pos;
int fb_pos_prev;
float volt = 0.0;
float prev_amp = 0.0;
float after_amp = 0.0;
int m = 0.03314;
int b = 1.962;
int delay_s;
int var_mult = 1;
int array_size = 180/var_mult;

//-----------------------buffer-------------------------------------------
char buf_input[20];
char buf_output[20];
char buf_index[20];

//-----------------------LCD Setup----------------------------------------
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);


int pos[180] = {0}; // Servo motor position array
float current[180] = {0}; // Servo motor position array
int fbpos[180] = {0}; // Servo motor position array

void setup() {
  //----------------------------Begin Serial Protocol----------------------------------
  Serial.begin(9600);
  //----------------------------Servo Motor Setup--------------------------------------
  servo_test_1.attach(9);
  servo_test_1.write(0);

  //----------------------------LCD 20x4 Display Setup---------------------------------
  lcd.begin(20,4);

  lcd.setCursor(0,0);
  lcd.print("Test 1: 1I/2O");

  lcd.setCursor(0,1);
  lcd.print("In Position/");

  lcd.setCursor(0,2);
  lcd.print("Out Position +");

  lcd.setCursor(0,3);
  lcd.print("Amp value");
  delay(3000);

  lcd.clear();
  //--------------------Display the empty array data-----------------------------
  display_value_table();
}

void loop() {
  while(input_pos < 181){

    delay(300);

    servo_test_1.write(input_pos);
    pos[index] = input_pos;

    while((fb_pos < (input_pos+2)) && (fb_pos < (input_pos-2))){
      //---------------Current sensor--------------------
      ADC_current = analogRead(cs_pin);
      volt = (ADC_current * 5.0) / 1023.0;
      prev_amp = (volt - 2.5) / 0.185;
      current[index] = prev_amp;

      //--------------Feeback servo sensor---------------
      ADC_servo = analogRead(fbservo_pin);
      //fb_pos = (ADC_servo * m) + b;
      fb_pos = round(map(ADC_servo,63,610,0,180));
      fbpos[index] = fb_pos;

      display_value_table();
      display_lcd(prev_amp,input_pos,fb_pos,index);
      
      delay(1);

    }
    index++;
    input_pos = index * var_mult;
  }
  delay(1000);
  input_pos = pos[index - 1];

  while(input_pos > -1){

    delay(300);

    servo_test_1.write(input_pos);
    pos[index] = input_pos;

   while((fb_pos > (input_pos+2)) && (fb_pos > (input_pos-2))){
      //---------------Current sensor--------------------
      ADC_current = analogRead(cs_pin);
      volt = (ADC_current * 5.0) / 1023.0;
      prev_amp = (volt - 2.5) / 0.185;
      current[index] = prev_amp;

      //--------------Feeback servo sensor---------------
      ADC_servo = analogRead(fbservo_pin);
      //fb_pos = (ADC_servo * m) + b;
      fb_pos = round(map(ADC_servo,63,610,0,180));
      fbpos[index] = fb_pos;

      display_value_table();
      display_lcd(prev_amp,input_pos,fb_pos,index);
      
      delay(1);
    }
    index--;
    input_pos = index * var_mult;
  }

  input_pos = pos[index + 1];
  delay(1000);
}
//-----------------------------Function-------------------------------------
void loding_screen(int seconds){
  for(int i = 0; i < seconds; i++){
    Serial.println(".");
    delay(1000);
  }
}

void display_value_table(){
  for(int array_count = 0; array_count <= 12; array_count++){
    Serial.print("["); Serial.print(pos[array_count]); Serial.print("|");Serial.print(fbpos[array_count]); Serial.print("|");
    Serial.print(current[array_count]);Serial.print("]");
  }
  Serial.println("");
}
void display_lcd(float amp, int in_pos, int out_pos, int ind){
  sprintf(buf_input, "Input Pos: %3d ", in_pos);
  lcd.setCursor(0,0);
  lcd.print(buf_input);

  lcd.setCursor(0,1);
  lcd.print("Current: ");lcd.print(amp,2);

  sprintf(buf_output, "Output Pos: %3d ", out_pos);
  lcd.setCursor(0,2);
  lcd.print(buf_output);

  sprintf(buf_index, "Index: %2d ", ind);
  lcd.setCursor(0, 3);
  lcd.print(buf_index);
}

void display_value(int index){
  Serial.print("[Pos: "); Serial.print(pos[index]); Serial.print("| Feedback Pos: ");Serial.print(fbpos[index]); Serial.print("| Current: ");
  Serial.print(current[index]);Serial.print("] - ");Serial.print("Index: ");Serial.print(index);Serial.println("");
}