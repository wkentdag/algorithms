import random

def generateRandomCoords(numPoints, maxVal):
	points = []
	for i in range(0, numPoints):
		x = random.randint(0, maxVal)
		y = random.randint(0, maxVal)
		points.append((x, y))
	return points

points = generateRandomCoords(50, 100)

pointsByX = sorted(points, reverse = True)
pointsByY = sorted(points, key=lambda point: point[1], reverse = True)
print pointsByX, "\n"
print pointsByY