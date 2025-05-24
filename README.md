# IOT
## Cloning the library  
Use the below command to clome the library 
```bash
git clone https://github.com/AditShah1234/IOT.git
```
If you already have the files you can skip the above step

## OS Installation

Install Raspberry PI OS using [Link](https://www.raspberrypi.com/software/) flow the steps

And the server is made on the ubuntu OS

## Library installation

In the code files there are 3 requirement_*.txt which are to be installed on different devices.

1) If the client is a laptop it have limited functionality to take photo and show as a output. 

```bash
pip3 install requirements_client.txt
```
2) If the client is a Raspberry PI then 

```bash
pip3 install requirements_rpi.txt
```
3) To make a local server you need to open the port then on the ubuntu OS

```bash
pip3 install requiremnts_server.txt
```
## Running the File

To run client if client is laptop use 
```bash
python3 app.py
```

If client is Raspberry PI
```bash
python3 app_rpi.py
```
then open 127.0.0.1:2000 which is a local host

To run server use 
```bash
python3 server.py
```


