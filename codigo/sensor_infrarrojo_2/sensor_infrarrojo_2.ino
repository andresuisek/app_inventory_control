#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "NETLIFE-ONTIVEROS";
const char* password = "ontiveros.2023";
const char* serverName = "http://192.168.100.33:8000/api/inventory_historical/";  // URL del servidor al que enviarás los datos

const int IR_SENSOR_PIN__IN = 22; 
const int IR_SENSOR_PIN__OUT = 36; 

void setup() {  
 Serial.begin(9600);  // Inicializar comunicación serial
  pinMode(IR_SENSOR_PIN__IN, INPUT);
  pinMode(IR_SENSOR_PIN__OUT, INPUT);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void sendPostRequest(const char* type_register) {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Error en la conexión WiFi");
    return;
  }

  HTTPClient http;
  String postData = "type_register=" + String(type_register);
  String url = serverName;
  //url+= endpoint;
  http.begin(url);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  
  int httpResponseCode = http.POST(postData);
  if (httpResponseCode > 0) {
    String response = http.getString();
    Serial.println("HTTP Response code: " + String(httpResponseCode));
    Serial.println(response);
  } else {
    Serial.println("Error en la solicitud POST");
  }
  http.end();
}

void loop() {
  int sensorValue__IN = digitalRead(IR_SENSOR_PIN__IN);  // Leer el valor analógico del sensor IR
  
  if(sensorValue__IN == LOW){
    sendPostRequest("Entry");    
  }

  int sensorValue__OUT = digitalRead(IR_SENSOR_PIN__OUT);  // Leer el valor analógico del sensor IR
  
  if(sensorValue__OUT == LOW){
    sendPostRequest("Exit");    
  }
  
  delay(500);
}
