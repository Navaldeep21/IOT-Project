import socket
import sys
import time
from face_reco import *
s = socket.socket()
s.bind(("",1234))
s.listen(100) # Accepts up to 10 incoming connections..
while(True):
    sc, address = s.accept()

    print(address)
    i=1
    name = sc.recv(1024).decode()
    print(name)
    
    
    f = open(name,"wb")# Open in binary
    i=i+1
    
    l = sc.recv(1024)
    
    while (l):
        f.write(l)
        l = sc.recv(1024)
    f.close()


    sc.close()
    if "image" in name.split("/"):
        predict(name)
    else:
        append_pickel(name)
    #time.sleep(50)
    print("done")
s.close()
