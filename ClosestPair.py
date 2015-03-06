import random
import math

def randomCoords(numPoints, maxVal):
  """returns a list of <numPoints> random points within the range 0-<maxVal>"""
  points = []
  for i in range(0, numPoints):
    x = random.randint(0, maxVal)
    y = random.randint(0, maxVal)
    points.append((x, y))
  return points

def ClosestPairDC(pointsX, pointsY):
  print("\nRunning Closest Pairs on")
  print("X Sorted: ", pointsX)
  print("Y Sorted: ", pointsY)

  if len(pointsX) <= 3:
    print (pointsX)
    print(pointsY)
    d = pointsX[0][0] - pointsX[1][0]
    return (d, pointsX[0], pointsX[1])

  else:

    # print(len(pointsX))
    # print(len(pointsX) // 2)

    mid = len(pointsX) // 2
    midpt = pointsX[mid]

    # print("mid is: " + str(midpt) )


    # Divide points sorted by x into left a right sets. 
    leftByX = pointsX[0:mid]
    rightByX = pointsX[mid:]


    # Divide points sorted by y into left and right sides of midpoint x.
    rightByY = []
    leftByY = []

    for p in pointsY:
      if p[0] < midpt[0] or ( p[0] == midpt[0] and p[1] <= midpt[1]):
        leftByY.append(p)
      else:
        rightByY.append(p)


    # Recursion step
    # print("LeftByX:", leftByX)
    # print("LeftByY:", leftByY)
    # print("RightByX:", rightByX)
    # print("RightByY:", rightByY)
    leftPair = ClosestPairDC(leftByX, leftByY)
    rightPair = ClosestPairDC(rightByX, rightByY)

    d1 = leftPair[0]
    d2 = rightPair[0]

    if d1 < d2:
      dist = d1
      point1 = leftPair[1]
      point2 = leftPair[2]

    else:
      dist = d2
      point1 = rightPair[1]
      point2 = rightPair[2]


    leftClose = []
    rightClose = []
    # print(dist, point1, point2)
    
    for p in leftByY:
      # print("Dist from",p, "and", midpt, "is", abs(p[0] - midpt[0]) )
      if abs(p[0] - midpt[0]) < dist:
        leftClose.append(p)
    
    for p in rightByY:
      # print("Dist from",p, "and", midpt, "is", abs(p[0] - midpt[0]) )
      if abs(p[0] - midpt[0]) < dist:
        rightClose.append(p)


    print("Left Close",leftClose)
    print("Right Close",rightClose)

    # Part 4
    jLow = 1
    i = 1
    j = 1

    while i < len(leftClose):
      if j > len(rightClose) or leftClose[i][1] + d < rightClose[j][1]:
        i += 1
        j = jLow
      elif leftClose[i][1] > rightClose[j][1] + d:
        jLow += 1
        j = jLow
      else:
        # dist = abs(leftClose[i] - rightClose[j])
        dist = math.hypot(leftClose[i][0] - rightClose[j][0], leftClose[i][1] - rightClose[j][1])
        if dist < d:
          d = dist
          point1 = leftClose[i]
          point2 = rightClose[j]
        j += 1
    print "\nClosest pair:", point1, point2, "distance:", dist
    return (dist, point1, point2)


# def ClosestPairConquor():








# points = [(3,12), (1,9), (4.5,7), (4,9), (8,2), (4.2, 11), (3.9, 3), (4.1, 5), (3.3, 4), (3.8, 4)]
points = randomCoords(10, 30)

# Set of points sorted by x values High to Low.
X = sorted(points, reverse = True)

# Set of points sorted by the key given. In our case 
# the lambda function points[1] gets the y value of each point
# and sorts by that value instead.
Y = sorted(points, key = lambda point: point[1], reverse = True)


ClosestPairDC(X, Y)
