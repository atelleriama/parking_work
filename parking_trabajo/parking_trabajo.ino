int sensorEntrada = 2;
int sensorSalida = 3;
int sensorGas = A0;
int cars_inside = 0;
int total_spaces = 10;
int lastEntrada = HIGH;
int lastSalida = HIGH;
int gasLimit = 450;

void setup() {
  Serial.begin(9600);
  pinMode(sensorEntrada, INPUT_PULLUP);
  pinMode(sensorSalida, INPUT_PULLUP);
  pinMode(sensorGas, INPUT);
}
