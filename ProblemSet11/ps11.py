# Problem Set 11: Simulating robots
# Name: Chaitra Kothari
# Collaborators: None
# Description: Create simple simulation for roomba like cleaner

import math
import random
import pylab
import ps11_visualize

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        # TODO: Your code goes here
        self.width = width
        self.height = height
        self.totTiles = width * height
        self.tilePos = {}

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # TODO: Your code goes here
        w = pos.getX()
        h = pos.getY()
        self.tilePos[(w, h)] = 'clean'
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # TODO: Your code goes here
        return (m, n) in self.tilePos
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return self.totTiles
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return len(self.tilePos)
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        # TODO: Your code goes here
        rand_x = random.randint(0, self.width)
        rand_y = random.randint(0, self.height)
        rand_pos = Position(rand_x, rand_y)
        return rand_pos
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        # TODO: Your code goes here
        w = pos.getX()
        h = pos.getY()
        return (w >= 0 and w <= self.width and h >= 0 and h <= self.height)



class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # TODO: Your code goes here
        self.room = room
        self.speed = speed
        self.d = random.randint(0, 359)
        self.p = room.getRandomPosition()

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        # TODO: Your code goes here
        return self.p

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # TODO: Your code goes here
        return self.d
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        # TODO: Your code goes here
        self.p = position
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        # TODO: Your code goes here
        self.d = direction


class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # TODO: Your code goes here
        curDirection = self.getRobotDirection()
        curSpeed = self.speed
        curRoom = self.room

        #move robot to a new position 
        newPosition = self.getRobotPosition().getNewPosition(curDirection, curSpeed)                
        #if new position not in the room, choose a new direction which is not same as current direction
        if not curRoom.isPositionInRoom(newPosition):
            #print 'hit wall, change direction'
               newDirectionList = list(range(0, curDirection)) + list(range(curDirection+1, 359))
               newDirection = random.choice(newDirectionList)
            #set self.direction to newdirection
               self.setRobotDirection(newDirection)
        #get new position based on this new direction
        newPosition = self.getRobotPosition().getNewPosition(self.getRobotDirection(), curSpeed)
        #mark tile at this position as clean
        self.setRobotPosition(newPosition)
        curRoom.cleanTileAtPosition(self.getRobotPosition())
        
# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """
    # TODO: Your code goes here
    cleanList = []
    for trial in range(num_trials):
        if visualize: anim = ps11_visualize.RobotVisualization(num_robots, width, height)
        cleanListPerBot = []
        
        robots = []

        #create a room
        room = RectangularRoom(width, height)

        #create a list of robots
        for robotNum in range(num_robots):
            robots.append(robot_type(room, speed))

        percentClean = 0.0
        
        #for each trial, compute list of percentage of room it cleans at each clock tick
        while percentClean <= min_coverage:
            if visualize: anim.update(room, robots)
            for robot in robots:
                robot.updatePositionAndClean()
                percentClean = float(room.getNumCleanedTiles()) / float(room.getNumTiles())
                if percentClean > min_coverage:
                    break;
                cleanListPerBot.append(percentClean)
        cleanList.append(cleanListPerBot)
        if visualize: anim.done()
    return cleanList
    
        

# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means

def avgLenListOfLists(list_of_lists):
    lengthOfLists = []
    avgLen = []
    for lst in list_of_lists:
        lengthOfLists.append(len(lst))
    avgLen = sum(lengthOfLists) / len(lengthOfLists)
    return avgLen

# === Problem 4
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    # TODO: Your code goes here

    #assume square room where length and width of room are the same
    possibleRoomDimensions = [5, 10, 15, 20, 25] 
    roomSize = []
    simResult = []
    meanTime = []
    for dim in possibleRoomDimensions:
        roomSize.append(dim ** 2)
        simResult = runSimulation(1, 1.0, dim, dim, 0.75, 100, Robot, False)
        meanTime.append(avgLenListOfLists(simResult))
    pylab.plot(roomSize, meanTime)
    pylab.xlabel('Room area')
    pylab.ylabel('Timesteps')
    pylab.title('Time to clean 75percent of square room with 1 robot, for various room sizes')
    pylab.show()

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # TODO: Your code goes here
    roomDim = 25
    numOfRobots = 10
    simResult = []
    meanTime = []
    for robotNum in range(1, numOfRobots + 1):
        simResult = runSimulation(robotNum, 1.0, roomDim, roomDim, 0.75, 100, Robot, False)
        meanTime.append(avgLenListOfLists(simResult))
    pylab.plot([num for num in range(1, numOfRobots + 1)], meanTime)
    pylab.xlabel('Number of robots')
    pylab.ylabel('Timesteps')
    pylab.title('Time to clean 75percent of square room of sie 25 X 25, for various number of robots')
    pylab.show()


def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # TODO: Your code goes here
    meanTime = []
    roomWidth = [20, 25, 40, 50, 80, 100]
    roomHeight = [20, 16, 10, 8, 5, 4]
    roomShape = [str(a) + ' X ' + str(b) for a, b in zip(roomWidth, roomHeight)]
    roomDim = [(a, b) for a, b in zip(roomWidth, roomHeight)]
    for dimension in roomDim:
        w = dimension[0]
        h = dimension[1]
        simResult = runSimulation(1, 1.0, w, h, 0.75, 100, Robot, False)
        meanTime.append(avgLenListOfLists(simResult))
    pylab.plot(roomShape, meanTime)
    pylab.xlabel('Shape of room')
    pylab.ylabel('Timesteps')
    pylab.title('Time to clean 75percent of room of various sizes by one robot')
    pylab.show()


def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # TODO: Your code goes here
    roomDim = 25
    numOfRobots = 5
    posMinCoverage = [0, 0.25, 0.5, 0.75, 1.0]
    simResult = []
    meanTime = []
    for minCoverage in posMinCoverage:
        for robotNum in range(1, numOfRobots + 1):
            simResult = runSimulation(robotNum, 1.0, roomDim, roomDim, minCoverage, 1, Robot, False)
            meanTime.append(avgLenListOfLists(simResult))
    pylab.plot(robotCoverage, meanTime)
    pylab.xlabel('Minimum area to be cleaned')
    pylab.ylabel('Timesteps')
    pylab.title('Time to clean a square room of size 25 X 25, for various number of robots and various minimum coverage areas')
    pylab.show()

# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    # TODO: Your code goes here
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new random position and mark the tile it is on as having
        been cleaned.
        """
        # TODO: Your code goes here
        
        curSpeed = self.speed
        curRoom = self.room
        #move robot to a new position 
        newPosition = curRoom.getRandomPosition()
        print 'newPosition:', newPosition.getX(), newPosition.getY()

        #mark tile at this random position as cleaned
        self.setRobotPosition(newPosition)
        curRoom.cleanTileAtPosition(self.getRobotPosition())


# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    # TODO: Your code goes here
    #compare performance of two robots in room of size 10 X 10 with 1 robot of speed 1.0
    robot_performance = runSimulation(1, 1.0, 10, 10, 0.75, 100, Robot, False)
    randomWalkRobot_performance = runSimulation(1, 1.0, 10, 10, 0.75, 100, RandomWalkRobot, False)

    robot_means = computeMeans(robot_performance)
    randomWalkRobot_means = computeMeans(randomWalkRobot_performance)

    
    pylab.plot(robot_means, randomWalkRobot_means)
    pylab.xlabel('Mean time for regular robot')
    pylab.ylabel('Mean time for random walk robot')
    pylab.title('Comparison of performance between Robot and Random Walk Robot')
    pylab.show()

