import RPi.GPIO as GPIO  #GPIOにアクセスするライブラリをimportします。                                          
import time


# GPIO.setmode(GPIO.BCM)  #GPIOへアクセスする番号をBCMの番号で指定することを宣言します。                        
# GPIO.setup(15,GPIO.OUT) #BCMの15番ピン、物理的には10番ピンを出力に設定します。                                
# GPIO.setup(2,GPIO.IN)   #BCM 2番ピンを入力に設定します。                                                      

# try:
#     while True:
#         if GPIO.input(2) == GPIO.LOW:
#             GPIO.output(15,GPIO.HIGH)
#         else:
#             GPIO.output(15,GPIO.LOW)

#         time.sleep(2.0)

# except KeyboardInterrupt:
#     GPIO.cleanup()

GPIO.setmode(GPIO.BCM)  #GPIOへアクセスする番号をBCMの番号で指定することを宣言します。                        
GPIO.setup(4, GPIO.OUT) #BCMの15番ピン、物理的には10番ピンを出力に設定します。                                

relay_ioports = [4, 17, 27, 22, 18, 23, 24, 25]

for i in relay_ioports:
    GPIO.setup(i, GPIO.OUT) #OPポートを出力に設定

try:
    while True:        
        for i in relay_ioports:
            GPIO.output(i, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(i, GPIO.LOW)
            time.sleep(0.1)

        # GPIO.output(4, GPIO.HIGH)
        # time.sleep(2.0)
        # GPIO.output(4, GPIO.LOW)
        # time.sleep(2.0)

except KeyboardInterrupt:
    for i in relay_ioports:
        GPIO.output(i, GPIO.LOW)
    GPIO.cleanup()