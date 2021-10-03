# Python3 program for the above approach
import math

# Function to find the angle
# between the two lines

# x1, y1, z1 = centre pt of next state
# x2, y2, z2 = centre pt of aruco on the current cell/ intersection pt of x,y,z axis
# x3, y3, z3 = any other pt on x axis
def calculateAngle(x1, y1, z1,
				x2, y2, z2,
				x3, y3, z3):
						
	# Find direction ratio of line AB
	ABx = x1 - x2;
	ABy = y1 - y2;
	ABz = z1 - z2;

	# Find direction ratio of line BC
	BCx = x3 - x2;
	BCy = y3 - y2;
	BCz = z3 - z2;

	# Find the dotProduct
	# of lines AB & BC
	dotProduct = (ABx * BCx +
				ABy * BCy +
				ABz * BCz);

	# Find magnitude of
	# line AB and BC
	magnitudeAB = (ABx * ABx +
				ABy * ABy +
				ABz * ABz);
	magnitudeBC = (BCx * BCx +
				BCy * BCy +
				BCz * BCz);

	# Find the cosine of
	# the angle formed
	# by line AB and BC
	angle = dotProduct;
	angle /= math.sqrt(magnitudeAB *
					magnitudeBC);

	# Find angle in radian
	angle = (angle * 180) / 3.14;

	# Print angle
	print(round(abs(angle), 4))

# x1, y1, z1 = centre pt of next state
# x2, y2, z2 = centre pt of aruco on the current cell/ intersection pt of x,y,z axis
# BCx, BCy, BCz = coeff of x axis/line
def calculateAngleLinePt(x1, y1, z1, x2, y2, z2,
				BCx, BCy, BCz):
						
	# Find direction ratio of line AB
	ABx = x1 - x2;
	ABy = y1 - y2;
	ABz = z1 - z2;

	# Find the dotProduct
	# of lines AB & BC
	dotProduct = (ABx * BCx +
				ABy * BCy +
				ABz * BCz);

	# Find magnitude of
	# line AB and BC
	magnitudeAB = (ABx * ABx +
				ABy * ABy +
				ABz * ABz);
	magnitudeBC = (BCx * BCx +
				BCy * BCy +
				BCz * BCz);

	# Find the cosine of
	# the angle formed
	# by line AB and BC
	angle = dotProduct;
	angle /= math.sqrt(magnitudeAB *
					magnitudeBC);

	# Find angle in radian
	angle = (angle * 180) / 3.14;

	# Print angle
	print(round(abs(angle), 4))

# Driver Code
if __name__=='__main__':

	# Given coordinates
	# Points A
	x1, y1, z1 = 1, 3, 3;

	# Points B
	x2, y2, z2 = 3, 4, 5;

	# Points C
	x3, y3, z3 = 5, 6, 9;

	# Function Call
	calculateAngle(x1, y1, z1,
				x2, y2, z2,
				x3, y3, z3);


