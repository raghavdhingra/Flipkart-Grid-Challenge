# Flipkart-Grid-Challenge

**#Introduction**

This is our submission repository for the Flipkart Grid 3.0 Robotics Challenge. We were asked to create 4 robots, that can autonomously drop cargo at the designated spots. We started off with a lot of brainstorming sessions, worked out different approaches, to finally test out the approach that we found the best. 
We started off by purchasing the required hardware, and then building the robots on cardboard pieces. The hardware team used their innovative ideas to create the most appropriate bots suited for this role.
While the software team, then started off with the coding, that runs the robots on the grid. This was done with OpenCV, Arduino IDE, and various python libraries. We will be detailing all the tools used, further in the documentation.

Camera Calibration
	Camera calibration is the process where we detect aruco of different Id’s. Implementing Homography for estimation of intrinsic and extrinsic camera calibration parameters and inclusion of Pose Estimation for the implementation of augmented Reality projects in further future projects. 
Aruco Codes – AugmentedReality uco Codes
Aruco markers are the individual identifiers which helped us in our robot positioning and individuality. We used  5×5 grid that is black n white in colour which  locates the position in our grid and help in following the #A star Algorithm.  We used the following id’s that is 66, 24, 70, 87 are used to get axis which provides us the angular difference between the grid and aruco.
The main Features of Aruco:
1.	Detect markers with Python code.
2.	Calibrate camera using Aruco ChessBoard 7*9.
3.	Faster than any other library for detection of markers.
4.	Detection of Marker Maps (several markers). 
Running code name and path:
Camera calibration:
Flipkart-grid-challenge>Testing>poco_cameraCalibration.py
Angel Calculation:
Flipkart-grid-challenge>Testing>angleCalc.py
Aruco Axis:
Flipkart-grid-challenge>Testing>arucoAxis.py

