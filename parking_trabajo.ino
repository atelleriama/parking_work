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

void loop() {
int entrada = digitalRead(sensorEntrada);
int salida = digitalRead(sensorSalida);
int air_value = analogRead(sensorGas);

// Coche entrando
if (entrada == LOW && lastEntrada == HIGH) {
if (cars_inside < total_spaces) {
cars_inside++;
}
}

// Coche saliendo
if (salida == LOW && lastSalida == HIGH) {
if (cars_inside > 0) {
cars_inside--;
}
}

lastEntrada = entrada;
lastSalida = salida;

int free_spaces = total_spaces - cars_inside;

String gate_status;

if (free_spaces <= 0 || air_value > gasLimit) {
gate_status = "BLOCKED";
} else {
gate_status = "ALLOW";
}

Serial.print(cars_inside);
Serial.print(",");
Serial.print(total_spaces);
Serial.print(",");
Serial.print(free_spaces);
Serial.print(",");
Serial.print(air_value);
Serial.print(",");
Serial.println(gate_status);

delay(1000);
}
