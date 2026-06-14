# 🚗 IoT Vehicle Tracking & Theft Prevention System using ESP32

## 📌 Overview

The IoT Vehicle Tracking & Theft Prevention System is a real-time smart vehicle monitoring solution developed using ESP32 and GPS technology. The system continuously tracks a vehicle's location, stores GPS coordinates, visualizes routes on an interactive dashboard, and detects unauthorized vehicle movement through geofencing.

This project demonstrates the practical application of Internet of Things (IoT), real-time data monitoring, location tracking, and theft prevention techniques for smart transportation systems.

---

## 🎯 Objectives

* Monitor vehicle location in real time
* Track and visualize vehicle routes
* Detect vehicle movement outside a predefined safe zone
* Improve vehicle security using geofencing
* Provide a user-friendly dashboard for monitoring

---

## 🚀 Features

* 📍 Real-Time GPS Tracking
* 🚗 Live Vehicle Location Monitoring
* 🗺️ Interactive Route Visualization
* 🚨 Theft Detection using Geofencing
* 📊 Real-Time Dashboard Analytics
* 💾 GPS Data Logging
* 🌍 Google Maps Integration
* 📥 Downloadable Tracking Reports
* 🔄 Auto-Updating Dashboard
* 📡 ESP32-Based IoT Connectivity

---

## 🛠️ Technology Stack

### Hardware

* ESP32 Development Board
* USB Power Supply

### Software

* Python
* Streamlit
* Pandas
* Folium
* Streamlit-Folium
* Streamlit-Autorefresh

---

## 🏗️ System Architecture

ESP32 + GPS Module → Location Data Collection → CSV Data Logging → Streamlit Dashboard → Route Visualization & Theft Detection

---

## 📂 Project Structure

```text
IoT Vehicle Tracking & Theft Prevention System/
│
├── app.py
├── simulator.py
├── data.csv
├── requirements.txt
├── README.md
└── screenshots/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/IoT-Vehicle-Tracking-Theft-Prevention-System.git
cd IoT-Vehicle-Tracking-Theft-Prevention-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Dashboard

```bash
streamlit run app.py
```

---

## 🚨 Geofence Security

The system defines a secure geographical boundary around a predefined safe location.

If the vehicle moves outside the allowed radius:

* Theft Alert is triggered
* Dashboard displays warning messages
* Vehicle location remains visible for tracking

---

## 📈 Dashboard Features

* Live GPS Coordinates
* Vehicle Status Monitoring
* Distance from Safe Zone
* Route History Visualization
* Interactive Maps
* Tracking Data Table
* Download GPS Reports

---

## 📸 Project Screenshots

Add screenshots of:

* ESP32 Hardware Setup
* GPS Data Collection
* Live Dashboard
* Route Tracking Map
* Theft Alert Notification

---

## 🎓 Learning Outcomes

* Internet of Things (IoT)
* ESP32 Programming
* GPS Integration
* Real-Time Data Processing
* Streamlit Dashboard Development
* Geofencing Concepts
* Data Visualization
* Smart Transportation Systems

---

## 🔮 Future Enhancements

* SMS Theft Alerts
* Email Notifications
* Cloud Database Integration
* Mobile Application
* AI-Based Route Prediction
* Driver Behavior Analysis
* Vehicle Health Monitoring
* Firebase Integration

---

## 👩‍💻 Author

Aarthi Kole

Second-Year Electrical & Electronics Engineering (EEE)

SDMCET, Dharwad

---

## 🙏 Acknowledgements

Special thanks to Umesh Yadav Sir for guidance and mentorship.

Project completed as part of learning initiatives under IIP and EDC-IIT Delhi.
