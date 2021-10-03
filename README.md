# Flipkart-Grid-Challenge

## Introduction
This is our submission repository for the Flipkart Grid 3.0 Robotics Challenge. We were asked to create 4 robots, that can autonomously drop cargo at the designated spots. We started off with a lot of brainstorming sessions, worked out different approaches, to finally test out the approach that we found the best. We started off by purchasing the required hardware, and then building the robots on cardboard pieces. The hardware team used their innovative ideas to create the most appropriate bots suited for this role. While the software team, then started off with the coding, that runs the robots on the grid. This was done with OpenCV, Arduino IDE, and various python libraries. We will be detailing all the tools used, further in the documentation.

## Technolgies used
* OpenCV
* Arduino
* ESP
* Communication using HTTP protocol

## OpenCv
* It is a machine learning module, by means of which we perform tasks such as object detection and positioning, and basically everything related to computer vision.
* We used it for object positioning, angle calculation and detection between the robot movement axis, and the grid axis, which helped us to determine the direction of movement for robots.
* OpenCv is basically the soul of our project.

## Tools and Algorithms
* A-Star Algorithm: The A* search algorithm, builds on the principles of Dijkstra’s shortest path algorithm to provide a faster solution when faced with the problem of finding the shortest path between two nodes. It achieves this by introducing a heuristic element to help decide the next node to consider as it moves along the path. 
* Aruco Markers: ArUco marker is a binary square with black background and a white generated pattern. These markers can be generated in whatever size. These markers have unique id ranging from 0 to 999. We have used aruco markers to detect the x, y and z axis of the marker which helps us to know about where the robot is facing. We also use a intelligent way to calculate the angle between the centre of the next cell in out shortest path and the x axis of aruco. The angle helps our robot to know the angle at which it needs to rotate at the various turning points.
** Aruco markers are the individual identifiers which helped us in our robot positioning and individuality. We used  5×5 grid that is black n white in colour which  locates the position in our grid and help in following the #A star Algorithm.  We used the following id’s that is 66, 24, 70, 87 are used to get axis which provides us the angular difference between the grid and aruco.
The main Features of Aruco:
1.	Detect markers with Python code.
2.	Calibrate camera using Aruco ChessBoard 7*9.
3.	Faster than any other library for detection of markers.
4.	Detection of Marker Maps (several markers). 


## Hardware
we've made a Wifi controlled car using NodeMcu esp8266 and L293d Motor Driver to control the wheels. To make this Bot we first connected the whole server to power supply on Bread Board as a proptotype, then created a server using the SSID and the Password in the ESP.
To control the bots using the Central System (to make bots completely automatic ) that's our Open CV, we created a command list to performs different fuctions using IP address and conditionally sends the commands to bots depending upon the requirement of bot to reach at the destination using shortest path. Along with that we've used Servo Motors to create the droping mechanism in Bots.
In the end we connected our Bots with open Cv using http server, where Open Cv scans the whole Arena and create the shortest path and controls the bots accordingly.

### Component Used :

1. NodeMcu esp8266
2. TT Gear Motors
3. L293d Motor Driver
4. Batteries
5. Soldering Iron

### Connections

ESP -> Digital Pins (D5,D6,D7,D8) => L293d Input (M1,M2,M3,M4)
Gear Motors -> L293d Output Terminals 
common ground -> To attach all grounds
Servo Signal Pin -> ESP Digital Pin (D0)
Power Supply (9V) -> ESP (Vin & common ground)

## Software
* Camera Calibration Script: Camera calibration is the process where we detect aruco of different Id’s. Implementing Homography for estimation of intrinsic and extrinsic camera calibration parameters and inclusion of Pose Estimation for the implementation of augmented Reality projects in further future projects. 
* Arucoxyz Script: It detects Aruco Markers and also helps in calculating angle for turning at the intersection points
* Grid Detection: It detects the cells



