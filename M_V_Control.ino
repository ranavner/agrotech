#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "your_SSID";  // Replace with your network credentials
const char* password = "your_PASSWORD";
const char* server = "api.thingspeak.com";
const String apiKey = "your_THINGSPEAK_API_KEY";

const int moisturePin1 = 34;  // Pin for moisture sensor 1
const int moisturePin2 = 35;  // Pin for moisture sensor 2
const int moisturePin3 = 36;  // Pin for moisture sensor 3
const int moisturePin4 = 39;  // Pin for moisture sensor 4
const int relayPin1 = 26;      // Pin for relay control
const int relayPin2 = 27;      // Pin for relay control
const int relayPin3 = 28;      // Pin for relay control
const int relayPin4 = 29;      // Pin for relay control

int MOISTURE_VALUE = 40;

void setup() {
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, HIGH);  // Turn off relay initially

  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
}

void loop() {
  int moistureValue1 = analogRead(moisturePin1);  // Read moisture sensor 1
  int moistureValue2 = analogRead(moisturePin2);  // Read moisture sensor 2
  int moistureValue3 = analogRead(moisturePin3);  // Read moisture sensor 3
  int moistureValue4 = analogRead(moisturePin4);  // Read moisture sensor 4

  if (moistureValue1 < MOISTURE_VALUE) {
    digitalWrite(relayPin1, LOW);  // Turn on relay
  } else {
    digitalWrite(relayPin1, HIGH);  // Turn off relay
  }

  if (moistureValue2 < MOISTURE_VALUE) {
    digitalWrite(relayPin2, LOW);  // Turn on relay
  } else {
    digitalWrite(relayPin2, HIGH);  // Turn off relay
  }

  if (moistureValue3 < MOISTURE_VALUE) {
    digitalWrite(relayPin3, LOW);  // Turn on relay
  } else {
    digitalWrite(relayPin3, HIGH);  // Turn off relay
  }

  if (moistureValue4 < MOISTURE_VALUE) {
    digitalWrite(relayPin4, LOW);  // Turn on relay
  } else {
    digitalWrite(relayPin4, HIGH);  // Turn off relay
  }



  if (WiFi.status() == WL_CONNECTED) {
    String url = "http://";
    url += server;
    url += "/update?api_key=";
    url += apiKey;
    url += "&field1=";
    url += String(moistureValue1);
    url += "&field2=";
    url += String(moistureValue2);
    url += "&field3=";
    url += String(moistureValue3);
    url += "&field4=";
    url += String(moistureValue4);

    HTTPClient http;
    http.begin(url);

    int httpResponseCode = http.GET();
    if (httpResponseCode > 0) {
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
    } else {
      Serial.print("Error sending data to ThingSpeak. HTTP Response code: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  }

  delay(10000);  // Wait for 10 seconds before next reading
}
