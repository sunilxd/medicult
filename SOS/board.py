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