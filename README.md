📌 Overview

This project is an IoT-based system that collects data from sensors and processes it through a client-server architecture. The system supports both Laptop and Raspberry Pi clients and runs a server on Ubuntu OS.

🚀 Cloning the Repository

Clone the repository using:

git clone https://github.com/Navaldeep21/IOT-Project.git
cd IOT-Project

If you already have the files, you can skip this step.

🖥️ Operating System Setup

Install Raspberry Pi OS from:
https://www.raspberrypi.com/software/

The server is configured to run on Ubuntu OS.

📦 Installing Dependencies

The project contains three requirements_*.txt files for different environments.

1️⃣ Laptop Client
  pip install -r requirements_client.txt
2️⃣ Raspberry Pi Client
  pip install -r requirements_rpi.txt
3️⃣ Ubuntu Server
  pip install -r requirements_server.txt
▶️ Running the Application
  Run Laptop Client
  python3 app.py
  Run Raspberry Pi Client
  python3 app_rpi.py

Then open:

http://127.0.0.1:2000

in your browser.

Run Server (Ubuntu)
python3 server.py
🛠 Tech Stack

Python

Raspberry Pi

Ubuntu Server

Client-Server Architecture
