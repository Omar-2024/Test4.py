import Adafruit_PCA9685
import time
class servo_Class:
    def __init__(self, Channel, ZeroOffset):
        self.Channel = Channel
        self.ZeroOffset = ZeroOffset
        self.pwn = Adafruit_PCA9685.PCA9685(address=0x40)
        self.pwn.set_pwn_freq(int(60))
        
    def SetPos(self,pos):
        pulse = int((650-150)/180*pos+150+self.ZeroOffset)
        self.pwn.set_pwn(self.Channel, 0, pulse)
        
    def Cleanup(self):
        self.SetPos(int(90))
        print('90')
        
if __name__ == '__main__':
    Servo0 = servo_Class(Channel=0,ZeroOffset=0)
    
    try:
        while True:
            for deg in range(180) :
                Servo0.SetPos(int(deg))
                print(deg)
                time.sleep(0.05)
    except KeyboardInterrupt:
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        Servo0.Cleanup()
        print("\nexit program")