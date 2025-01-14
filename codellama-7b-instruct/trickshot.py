import math
def pool_shot(w, l, h, x1, y1, x2, y2, x3, y3):
    if w < 1 or l < 1 or h < 1 or r < 0:
        return "impossible"
    
    # determine if the shot is possible
    # if it is not then return 'impossible'
    
    # calculate the distance to place the ball on the dashed line
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if d > h:
        return "impossible"
    
    # calculate the angle to shoot the ball
    # and round it to two decimal places
    theta = math.degrees(math.atan((x3 - x2)/(y3 - y2)))
    return "%.2f %.2f" % (d, theta)
# Generator time: 7.4595 seconds