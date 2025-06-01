from machine import Pin
import utime,time
#buz = Pin(14, Pin.OUT)
ms = Pin(5,Pin.IN)
sc=Pin(8,Pin.IN)
motor1=Pin(6,Pin.OUT)
motor2=Pin(3,Pin.OUT)
while True:
   ss=sc.value()
   mv=ms.value()
   print(ss)
   print(mv)
   line1="SC:"+ str(ss) +  "  MC:" + str(ms)
   if(ss==0 and mv==0):
     motor1.low()
     motor2.low()
     #line2="LIFT IN MOTION COND"
     print("LIFT IS STOP")
   #while(1)
   else:
    # print("LIFT IS RUNNING")
     motor1.low()
     motor2.high()
     time.sleep(2)
     motor2.low()
     motor1.high()
     time.sleep(2)
    

