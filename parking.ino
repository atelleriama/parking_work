int sensorEntrada = 2;
int sensorSalida = 3;

void setup() {
  Serial.begin(9600);

  pinMode(sensorEntrada, INPUT_PULLUP);
  pinMode(sensorSalida, INPUT_PULLUP);
}

void loop() {

}
