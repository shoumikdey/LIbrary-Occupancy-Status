import serial
import sqlite3
import time


dbname = 'sensorsData.db'
def getData():
        ser = serial.Serial('/dev/ttyACM0', 9600)
        s = [0, 1]
        #while True:
                #read_serial=str(int(ser.readline().strip()))
        read_serial=str(ser.readline().strip())
        read_serial_str_len = len(read_serial)
        read_serial_str =  read_serial[2:read_serial_str_len-1]
                #print(str(int(ser.readline().strip(), 16)))
                #print(read_serial)
                #print(read_serial_str)

        ser1 = serial.Serial('/dev/ttyACM1', 9600)
        s1 = [0, 1]
        #while True:
                #read_serial=str(int(ser.readline().strip()))
        read_serial1=str(ser1.readline().strip())
        read_serial_str_len1 = len(read_serial1)
        read_serial_str1 =  read_serial1[2:read_serial_str_len1-1]
                #print(str(int(ser.readline().strip(), 16)))
                #print(read_serial)
                #print(read_serial_str)
        logData(read_serial_str, 'A1')
        logData(read_serial_str1, 'A2')



#currStatus=''
#currStatus1=''
def logData(dist, port):
        conn = sqlite3.connect(dbname)
        curs = conn.cursor()
        status=''
        global currStatus
        try:
                if(int(dist) > 10):
                        status = 'Vacant'
                else:
                        status = 'Occupied'
        except:
                pass
        #if(currStatus != status):
        curs.execute("UPDATE stat_data SET timestamp = datetime('now'),status = ? WHERE table_id = ?", (status, port))
        conn.commit()
        conn.close()
        print(int(dist), status)
        #currStatus = status

        
        
#getData()
