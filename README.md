# 🚁 Drone Control and Operations

This repository contains various **Python scripts and code snippets** related to the **control, movement, and operation** of drones using the **Tello library**.  
These programs are primarily developed for **learning and experimentation** while exploring **drone programming concepts** such as movement control, image capture, keyboard operation, mapping, and surveillance.

---

## 🧠 Overview

This project demonstrates how to interact with and control a **DJI Tello drone** programmatically using Python.

Through this repository, you will learn to:

- ✈️ **Control the drone’s basic movements** — including takeoff, landing, rotation, and directional navigation.  
- 📸 **Capture images and video** using the drone’s built-in camera.  
- ⌨️ **Implement keyboard control** for real-time drone flying.  
- 🗺️ **Map drone movement** in a simulated 2D environment using **odometry principles** (velocity, angle, and displacement).  
- 🕵️ **Conduct basic surveillance tasks** by integrating live camera feeds with autonomous movement scripts.  

Each script is modular, easy to understand, and designed to build a **progressive understanding** of drone programming.

---

## ⚙️ Prerequisites

Before running the code, ensure you have the following:

### 🛰️ Hardware
- **DJI Tello drone** (or **Tello simulator** for virtual testing)

### 💻 Software
- **Python 3.7+**
- **OpenCV** → for image and video processing  
- **djitellopy** → to communicate with the Tello drone  
- **NumPy** → for numerical and odometry calculations  

---

## 🧩 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/drone-control-operations.git
   cd drone-control-operations
2. **Install dependencies**
   ```bash
   pip install opencv-python djitellopy numpy

3. **Connect your Tello drone**
   - Turn on the drone and connect your computer to the Tello Wi-Fi network.
   - Verify connection before running the scripts.
     
## 🚀 Features Implemented
| Feature                | Description                                                                                        |
| ---------------------- | -------------------------------------------------------------------------------------------------- |
| **Basic Movement**     | Control takeoff, landing, and directional motion (forward, back, left, right, up, down, rotation). |
| **Image Capturing**    | Capture and save images using Tello’s camera feed.                                                 |
| **Keyboard Control**   | Real-time drone navigation using key inputs (e.g., W, A, S, D).                                    |
| **Mapping & Odometry** | Estimate drone’s position based on velocity and angular displacement.                              |
| **Surveillance Mode**  | Combine live video feed with movement for basic autonomous or semi-autonomous surveillance.        |
