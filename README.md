# Medicult

<img src="https://github.com/sunilxd/medicult/blob/main/app/src/main/res/mipmap-mdpi/ic_launcher_foreground.jpeg?raw=true" align="right" width="120" height="120">

## About this repo
This project is devloped on 2 day hackfeast on PSG itech, Coimbatore (26 Aug 2022 to 27 Aug 2022).

**Sustainable Development Theme**

An ambulance tracker app. Developed to save people's life on time by using the gps location to get the nearest ambulance to rescue.

## Working Demo

#### Patient side
<img width=400 src="Demo/patient.gif">

#### Driver side
<img width=400 src="Demo/driver.gif">

### Google map api error :warning:
Since the original Google map api needs credit card details we used a duplicate api key which has some problem while redirecting to the Google maps while clicking "PICK PATIENT". We tried to fix it but the only solution we found in online is to buy the original api key.

### Automatic Ambulance request based on heart rate
Using the data from the Smart watch (in our case from arduino) to monitor the person heart rate. We stored the patient's heart rate for the past one minute and trigger a signal into the cloud if the patient's heart rate is abnormal for the past five minute.

<img width=600 src="Demo/hardware.gif">
<br>

#### Python code snippet for trigger
```python
import serial
from time import sleep
# To clear print lines
from IPython.display import clear_output

serialcomm = serial.Serial('COM8', timeout=0.05)
serialcomm.reset_input_buffer()

heart_rate = []
cond = 'Safe'
count = 12

def change(new):
    global cond
    if cond!=new:
        cond = new
        # access bot
        print(cond)
        

while True:
    serialcomm.write(bytes(str(x), 'utf_8'))
    inVar = str(serialcomm.read_until().decode())
    if inVar!='':
        try:
            heart_rate.append(int(inVar))
        except Exception as e:
            print(e)
    if len(heart_rate)>count:
            heart_rate.pop(0)
    boollis = [ele>50 and ele<120 for ele in heart_rate]
    print(heart_rate)
    print(boollis)
    if len(heart_rate)>count-1 and not(all(boollis)):
        change('Danger')
    else:
        change('Safe')
    sleep(1.5)
    clear_output()
    
serialcomm.close()
```

[![Blood pressure output](https://img.youtube.com/vi/j-MuaBVzJQo/0.jpg)](https://youtu.be/j-MuaBVzJQo)

we used google sheet api to store the status of the patient which can be easily accessed by mobile app through

```java
import java.io.IOException;
import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
public class JsoupExample {
   public static void main(String args[]) throws IOException {
      String page = "google_sheet_url";

      Connection conn = Jsoup.connect(page);

      Document doc = conn.get();

      String result = doc.body().text();
      if result.contains('Danger'){
        ## call the ambulance
      }
   }
}
```
we still not yet completely merged the trigger fucntion into our app but we are confident that extra 5 hour of work is more than enough to complete it.

### Screen shots
### Flow chart