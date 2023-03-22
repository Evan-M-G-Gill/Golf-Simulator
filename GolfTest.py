#required imports
import os
import csv
import math
import matplotlib
import numpy as np
import win32com.client
from matplotlib import pyplot as plt

#setting known values and questing unknown values from the user
ClubHeadWeight = float(0.1) #weight of the club head

ClubFaceAngle = int(input("From vertical 90°, what is the angle of the club face? ")) #the angle that the club face faces

ClubFaceRadian = float((ClubFaceAngle) * ((3.141592654) / (180))) #convirts the angle into a radian for future use

ArmLenght = float(
 input("What is the distance from your hand to your shoulder(In meters)? ")) #finds the length of the players arms

print("That's great, thanks. ") #response

FullLenght = float(
 input(
  "What is the distance from your shoulder to the centre of the club head (Again, im meters please)? "
 )) #finds the length from the club face to the player's shoulder

#opens the data file and converts to list
CURRENT_DIR = os.path.dirname(__file__)
file_path = os.path.join(CURRENT_DIR, 'wrist.csv')

with open(file_path, 'r') as file:
	csvreader = csv.reader(file)
	csvreader = list(csvreader)

	#selects the required data locations
	Time = (csvreader[572][0])  #time

	StAc1 = float(csvreader[1][4])  #velocities. im sure there is an easier way
	StAc10 = float(csvreader[10][4])
	StAc20 = float(csvreader[20][4])
	StAc30 = float(csvreader[30][4])
	StAc40 = float(csvreader[40][4])
	StAc50 = float(csvreader[50][4])
	StAc60 = float(csvreader[60][4])
	StAc70 = float(csvreader[70][4])
	StAc80 = float(csvreader[80][4])
	StAc90 = float(csvreader[90][4])
	StAc100 = float(csvreader[100][4])
	StAc110 = float(csvreader[110][4])
	StAc120 = float(csvreader[120][4])
	StAc130 = float(csvreader[130][4])
	StAc140 = float(csvreader[140][4])
	StAc150 = float(csvreader[150][4])
	StAc160 = float(csvreader[160][4])
	StAc170 = float(csvreader[170][4])
	StAc180 = float(csvreader[180][4])
	StAc190 = float(csvreader[190][4])
	StAc200 = float(csvreader[200][4])
	StAc210 = float(csvreader[210][4])
	StAc220 = float(csvreader[220][4])
	StAc230 = float(csvreader[230][4])
	StAc240 = float(csvreader[240][4])
	StAc250 = float(csvreader[250][4])
	StAc260 = float(csvreader[260][4])
	StAc270 = float(csvreader[270][4])
	StAc280 = float(csvreader[280][4])
	StAc290 = float(csvreader[290][4])
	StAc300 = float(csvreader[300][4])
	StAc310 = float(csvreader[310][4])
	StAc320 = float(csvreader[320][4])
	StAc330 = float(csvreader[330][4])
	StAc340 = float(csvreader[340][4])
	StAc350 = float(csvreader[350][4])
	StAc360 = float(csvreader[360][4])
	StAc370 = float(csvreader[370][4])
	StAc380 = float(csvreader[380][4])
	StAc390 = float(csvreader[390][4])
	StAc400 = float(csvreader[400][4])
	StAc410 = float(csvreader[410][4])
	StAc420 = float(csvreader[420][4])
	StAc430 = float(csvreader[430][4])
	StAc440 = float(csvreader[440][4])
	StAc450 = float(csvreader[450][4])
	StAc460 = float(csvreader[460][4])
	StAc470 = float(csvreader[470][4])
	StAc480 = float(csvreader[480][4])
	StAc490 = float(csvreader[490][4])
	StAc500 = float(csvreader[500][4])
	StAc510 = float(csvreader[510][4])
	StAc520 = float(csvreader[520][4])
	StAc530 = float(csvreader[530][4])
	StAc540 = float(csvreader[540][4])
	StAc550 = float(csvreader[550][4])
	StAc560 = float(csvreader[560][4])
	StAc570 = float(csvreader[570][4])
	StAc572 = float(csvreader[572][4])

#finds the average of the StAc values. Again, im sure there is an easier way.
StAcMean = (StAc1 + StAc10 + StAc20 + StAc30 + StAc40 + StAc50 + StAc60 +
            StAc70 + StAc80 + StAc90 + StAc100 + StAc110 + StAc120 + StAc130 +
            StAc140 + StAc150 + StAc160 + StAc170 + StAc180 + StAc190 +
            StAc200 + StAc210 + StAc220 + StAc230 + StAc240 + StAc250 +
            StAc260 + StAc270 + StAc280 + StAc290 + StAc300 + StAc310 +
            StAc320 + StAc330 + StAc340 + StAc350 + StAc360 + StAc370 +
            StAc380 + StAc390 + StAc400 + StAc410 + StAc420 + StAc430 +
            StAc440 + StAc450 + StAc460 + StAc470 + StAc480 + StAc490 +
            StAc500 + StAc520 + StAc530 + StAc540 + StAc550 + StAc560 +
            StAc570 + StAc572)
#used the StAcMean and Time to find the speed of the wrist. (this is where the speed is read)
WristSpeed = float(StAcMean) / float(Time)
WristSpeed = float(WristSpeed)

HeadSpeed = ((WristSpeed) / (ArmLenght)) * (FullLenght) #calculates how fast the club head goes, using the wrist speed and the the two requested lengths
HeadSpeed = float(HeadSpeed)
#calculate transfer of velocity between club head and ball

BallWeight = float(0.56) #weight of the golf ball

Effic = float(1.9) #efficiency of transfer

BallSpeed = ((HeadSpeed) * ((Effic) / ((BallWeight) / (ClubHeadWeight))))
BallSpeed = float(BallSpeed) #calculates the ball's launch speed using the weight of the ball, the weight ofthe club, the speed of the club and the assumed efficiency

#https://www.tutelman.com/golf/swing/golfSwingPhysics1.php

#breakdown the vector into X and Y components so that we can use them for later calculations

BallSpeedX = float((BallSpeed) * (math.cos(ClubFaceRadian))) #calculates the ball's speed on the X axis

BallSpeedY = float((BallSpeed) * (math.cos(ClubFaceRadian))) #calculates the ball's speed on the Y axis
#calculate air time:Work to be done, air time comes out as a negative

AirTime = float((2) * ((BallSpeedY) / (9.81))) #calculates the total air time

#Create the graph. To do this, calculate the X and Y velocities separately at the same point in time then compare to two speeds of matchinf time as the X and Y axis. this will give you the trajectory

#Idea: Calculate the Y position as if it had no X component every set unit of time, according to the effects of gravity. Then record this data as the Y array for the graph. Then do the same for the X as if it had a flat trajectory (how long would it would take to stop moving). Then put this as the X array for the graph.  Y Axis will probably be easier

#Calculate Y Max
MaxHeight = float((((BallSpeedY) * (BallSpeedY)) / ((2) * (9.8))) / (100)) #calculates the maximum height acheived by the golf ball
MaxHeight = round(MaxHeight, 2)
print("The maximum height reached was ", MaxHeight, " meters")

#calculate X Max
MaxDistance = float((math.sin(float(2.0001) * (ClubFaceRadian)) *
                     ((BallSpeed) * (BallSpeed))) / float(9.8) / (100)) #calculates the maximum distance acheived by the golf ball
MaxDistance = round(MaxDistance, 2)
print("The maximum distance reached was ", MaxDistance, " meters")

#set up loop for gathering X and Y coords
Loopcount = float((AirTime) / (500)) #500 samples
print(Loopcount)
CounterLoop = 0
x = [0]
y = [0]
while CounterLoop <= (500): #stats loop of calculations for X and Y axis positions
	YatTime = float(float(BallSpeedX) * (CounterLoop))
	y.append(YatTime)
	XatTime = float(((ClubFaceAngle) + (float(BallSpeedY) * (CounterLoop))) -
	                ((4.9) * ((AirTime) * (AirTime))))
	x.append(XatTime) #adds the values to to array
	x.append(XatTime) #adds the values to an array
	CounterLoop = (CounterLoop) + (1)
	
#as far as i can find, the correct calculation is "y = h + xtan(α) - gx²/2V₀²cos²(α)". this is the best way I have found to implement it into python.

#x.append(MaxHeight)
#y.append(MaxDistance)
#ym=y.copy()
#ym.reverse()
#y+=ym
#y.pop(0)
#y.remove(YatTime)

#generates the graph
plt.plot(x)#(x, y)
plt.xlabel('Distance')
plt.ylabel('Height')
plt.title('Trajectory')
plt.show()

#Rather than the parabola, I get a straight line.