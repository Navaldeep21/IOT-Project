import face_recognition
import pickle
import cv2
import time
import numpy as np
import os
import sys
from config import *
import threading
import csv
import pandas as pd
from time_series import *
# Import Adafruit IO MQTT client.

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
class profile():
    def __init__(self):
        self.user_name= "None"
        self.room_temp = 0
        self.lux = 0
        self.set_temp=0
    def printin(self):
        print( self.user_name, self.room_temp, self.lux, self.set_temp)
    def compare_it(self, point2):
        if self.user_name== point2.user_name and self.room_temp== point2.room_temp and self.lux== point2.lux and  self.set_temp== point2.set_temp :
            return True
        return False
    def copy_it(self, point2):
        self.user_name = point2.user_name 
        self.room_temp = point2.room_temp  
        self.lux= point2.lux
        self.set_temp= point2.set_temp
        
record = profile()
def message(client, feed_id, payload):
    # print(feed_id, payload)
    if feed_id == "iot.name":  
        record.user_name = payload
        try:
            predicted_tmp = predict_output(np.array([record.user_name,record.room_temp,record.lux]))
            client.publish("iot.temp-set",predicted_tmp)
        except:
            pass

    if feed_id == "iot.light-intensity":
        record.lux = payload
    if feed_id == "iot.room-temp":
        record.room_temp = payload
        

    if feed_id == "iot.temp-set":
        record.set_temp = payload   
   


        


def connected(client):
   
    print('Connected to Adafruit IO!  Listening for {0} changes...'.format("k"))
    client.subscribe("iot.light-intensity")
    client.subscribe("iot.name")
    client.subscribe("iot.room-temp")
    client.subscribe("iot.temp-set")

def subscribe(client, userdata, mid, granted_qos):
    pass
    # This method is called when the client subscribes to a new feed.
    # print('Subscribed to {0} with QoS {1}'.format("Temp_set", granted_qos[0]))
    # print('Subscribed to {0} with QoS {1}'.format("iot.name", granted_qos[0]))

def mqtt():
    client.on_connect    = connected
    client.on_message    = message
    client.on_subscribe  = subscribe
    client.connect()
    client.loop_blocking()



encodings_dict = {}
def predict(path):
    predict_enco = pickle.loads(open(path, "rb").read())
  
    print(len(predict_enco))
    max_match_count={}
    
    for i in range(len(predict_enco)):
        for j in encodings_dict.keys():
            print(i,j)
            matches = face_recognition.compare_faces(encodings_dict[j],predict_enco[i])
            total_true=0
            for s in matches:
                if s:
                    total_true+=1
            
            print(total_true,matches)
            if j in max_match_count:
                max_match_count[j]=max_match_count[j]+total_true
            else:
                max_match_count[j] = total_true
    print(max_match_count)
    key = list(max_match_count.keys())
    val = list(max_match_count.values())
    try:
        record.user_name = key[val.index(max(val))]
        client.publish("iot.name",record.user_name)
    except:
        client.publish("iot.name","Unknown")   



def append_pickel(file):
    print("here")
    data = pickle.loads(open(file, "rb").read())
    
    print(file.split('/'))
    encodings_dict[file.split('/')[-1]] = data
    print(encodings_dict)
def csv_write():
    record_writtern = profile()
    count=0
    
    while(1):
        time.sleep(10)
        record_writtern.printin()
        print(count)
        if count%10 == 0:
            df = pd.DataFrame()
            tmp =[]
        if  record_writtern.compare_it(record):
            pass
        else:
        
            data = [record.user_name,record.room_temp,record.lux,record.set_temp]
            record_writtern.copy_it(record)
            tmp.append(data)
            count+=1
        
        if count%10 == 0 and count>0:
            df = pd.DataFrame(tmp)
   
            df.to_csv("store.csv", mode='a', index=False, header=False)
            tmp= []
            train()



def randomizer():
    while(True):
        time.sleep(10)
        t = np.random.random(3)
        client.publish("iot.light-intensity",t[0]*1000)
        client.publish("iot.room-temp",t[1]*100)
        client.publish("iot.temp-set",t[2]*100)
all_pi_dir= os.listdir("asset")
print(all_pi_dir)

for i in all_pi_dir:
   data = pickle.loads(open("asset"+"//"+i, "rb").read()) 
   encodings_dict[i] = data
t1 = threading.Thread(target=mqtt)
t2 = threading.Thread(target=csv_write)
t3 = threading.Thread(target=randomizer)
t1.start()
t2.start()
# t3.start()