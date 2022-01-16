import conf, json, time
from boltiot import Sms, Bolt

minimum_limit = 300
maximum_limit = 600  

mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)

while True: 
    print ("Reading sensor value...")
    response = mybolt.analogRead('A0') 
    data = json.loads(response) 
    print("Sensor value is: " + str(data['value']))
    try: 
        sensor_value = int(data['value']) 
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Sending SMS through Twilio...")
            temp_value = round((100*sensor_value)/1024,2)
            print("The Current temperature is " +str(temp_value) + chr(176) + "C")
            response = sms.send_sms("The Current temperature is " +str(temp_value) + chr(176) + "C")
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(10)