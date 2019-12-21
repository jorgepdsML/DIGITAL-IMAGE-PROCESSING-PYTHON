#include <DHT.h>
//realizar 2 definiciones
#define DHTTYPE DHT11
#define DHTPIN 11
//CREAR UN OBJETO CON UN NOMBRE ADECUADO PARA EL DHT
DHT sensordht(DHTTYPE,DHTPIN);
//DEFINIR 2 VARIABLE DEL TIPO FLOTANTE
//TIPO NOMBRE=VALOR_INICIAL;
int temperatura;
int humedad;
//MENSAJE PARA TEMPERATURA
char temp_char[6];
char hum_char[6];
void setup()
{//iniciar funcionamiento del sensor DHT11
sensordht.begin();
//INICIAR COMUNICACIÓN SERIAL
Serial.begin(9600);
}
void loop()
{
  //LEER TEMPERATURA Y HUMEDAD
 temperatura=(int)sensordht.readTemperature();
 humedad=(int)sensordht.readHumidity();
 delay(2000);
 //si se encuentra un valor nan de temperatura , no enviarlo a la laptop
if (isnan(temperatura)==false && isnan(humedad)==false)
{
    sprintf(temp_char,"%c%d%c",'t',20,'*');
    sprintf(hum_char,"%c%d%c",'h',25,'-');
    //ENVIAR DATOS DE TEMPERATURA Y HUMEDAD HACIA PYTHON
Serial.write(temp_char);
Serial.write(hum_char);
}
}
