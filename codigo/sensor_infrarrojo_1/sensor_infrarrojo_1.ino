/*
 * Ejemplo leer temperatura y humedad
 * Sensor DHT11 y ESP32s
 */
#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

#include <DHT.h>//https://github.com/adafruit/DHT-sensor-library
#define DHTPIN 0

#define DHTTYPE DHT11   // DHT 11

const char* ssid = "NETLIFE-ONTIVEROS";
const char* password = "ontiveros.2023";
const char* serverName = "http://192.168.100.33:8000/api/";  // URL del servidor al que enviarás los datos


DHT dht(DHTPIN, DHTTYPE);

void setup() {  
  Serial.begin(9600);
  Serial.println(F("DHTxx test!"));
  
  dht.begin();

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void sendPostRequest(float value, const char* endpoint) {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Error en la conexión WiFi");
    return;
  }

  HTTPClient http;
  String postData = "value=" + String(value);
  String url = serverName;
  url+= endpoint;
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
  delay(10000);
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  
  if (isnan(h) || isnan(t)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  
  Serial.print(F("Humedad: "));
  Serial.print(h);
  Serial.print(F("% Temperatura: "));
  Serial.print(t);
  Serial.println(F("°C "));
  
  sendPostRequest(h, "humidity/");
  sendPostRequest(t, "temperature/");
}
