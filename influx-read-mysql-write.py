from influxdb import InfluxDBClient
import mysql.connector
import time
import sys

client = InfluxDBClient(host='192.168.219.107',port=8086,username='iotuser',password='iot12345')
client.switch_database('homeassistant')

connection  = mysql.connector.connect(host='142.93.75.207',user='iotuser',password="iot12345", database='iot')
mycursor = connection.cursor()

sql = "create table if not exists aqara_thTable(id mediumint not null auto_increment,temperature double not null, humidity double not null,timestamp timestamp default current_timestamp on update current_timestamp not null ,primary key(id))"

mycursor.execute(sql)
connection.commit()

while (True):
    
    try:
        hum = client.query ('select value from "sensor.aqara_humidity" order by time desc limit 1')
        tem = client.query ('select value from "sensor.aqara_temperature" order by time desc limit 1')

        for hum_temp in hum.get_points():
                hum = hum_temp['value']
        for tem_temp in tem.get_points():
                tem = tem_temp['value']
        sql = "insert into aqara_thTable (temperature,humidity) values (%s,%s)"
        val = (tem,hum)
        mycursor.execute(sql,val)
        connection.commit() 
        print ("A new temperature and humidity data {}C,{}% have been saved successfully.".format(tem,hum))
        time.sleep(300)
    except KeyboardInterrupt:
        print ("System has been interrupted by Ctrl+C")
        sys.exit(0)


