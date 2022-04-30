float lectura;

float volt;


void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  pinMode(A0, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  lectura = analogRead(A0);
  volt = lectura/1023 * 5.0;
  Serial.print(volt);
  delay(250);
}
