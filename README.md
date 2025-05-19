# Autonomous-Vehicles-And-Robotics-
This Python program simulates an AI-powered delivery robot in a hospital using a GUI built with Tkinter. The robot delivers medications from the Pharmacy to patient rooms, manages a delivery queue, and logs completed tasks.
AI Delivery Robot System

A Python GUI application that simulates an autonomous robot for delivering medications within a hospital. The robot starts from the pharmacy, uses Dijkstra’s algorithm to find the shortest path to patient rooms, and logs each delivery with timestamps.

Features

Add Deliveries to a queue with patient ID, room, and medication

Start Delivery: Simulates navigating through hospital rooms

Shortest Path Calculation using Dijkstra’s algorithm

Delivery Log: Records all completed deliveries with time data

Built using Python standard libraries (no external dependencies)

Demo

A simple simulation for hospital delivery logistics using tkinter:

GUI with buttons for adding deliveries, starting deliveries, and viewing the delivery log.

Logs include delivery start and end times.

Simulated movement output shown in the console.

Requirements

Python 3.x

No external libraries required.

How to Run

Save the script as delivery_robot.py.

Run the script:

python delivery_robot.py 

Hospital Map Structure

The hospital layout is defined as an adjacency list (graph). Example:
hospital_map = { "Pharmacy": ["Room101", "Room102", "Room103"], "Room101": ["Pharmacy", "Room102"], "Room102": ["Pharmacy", "Room101", "Room103"], "Room103": ["Pharmacy", "Room102"] } 
This can be modified to represent more complex hospital layouts.

GUI Overview

Add Delivery: Prompts for patient ID, room number, and medication.

Start Delivery: Begins the delivery process to the next patient.

View Log: Opens a new window showing the history of completed deliveries.

Example Output

Console simulation:
Navigating to Room101... Navigating to Pharmacy... 
GUI will show delivery confirmations and historical logs.

Future Improvements

Add animations to visualize robot movement

Import/export delivery data and map configurations

Priority-based delivery scheduling

Multi-robot simulation

License

MIT License
Let me know if you'd like a version with screenshots or badges (e.g., for Python version, license type, etc.).
