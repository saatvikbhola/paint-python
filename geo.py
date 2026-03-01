import math
import random

def distance(x1,y1,x2,y2):
    
    d = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)
    return d

def calc_tri_angle(a,b,c): 
    
    numerator = a**2 + b**2 - c**2
    denominator = 2*a*b 
    
    cos_c = numerator/denominator

    angle_radians = math.acos(cos_c)
    
    return math.degrees(angle_radians)

def slope(x1,y1,x2,y2):
    """
    finds the slope for a line when points are given 
    
    :param x1: point x
    :param y1: point y
    :param x2: point x
    :param y2: point y
    """

    if x2-x1 == 0:
        return "parallel lines"

    return (y2-y1) / (x2-x1)

def intercept(x1,y1,x2,y2):
    """
    finds the intercept for a line when points are given 
    
    :param x1: point x
    :param y1: point y
    :param x2: point x
    :param y2: point y
    """
    if x2-x1 == 0:
        return "parallel lines"
    m = slope(x1,y1,x2,y2)

    return y1-(m*x1)


def find_point_on_line(x1,y1,x2,y2):
    """
    finds the points on the 80% of the line leaves 10% on both sides i.e AB is now A'B'

    :param x1: point x
    :param y1: point y
    :param x2: point x
    :param y2: point y
    """
    # Directly pick a t between 0.1 (10%) and 0.9 (90%)
    t = random.uniform(0.1, 0.5)
    
    rnd_x = x1 + t * (x2 - x1)
    rnd_y = y1 + t * (y2 - y1)
    
    return rnd_x,rnd_y


def find_intersection(D, A, B, C):
    """
    Finds where line DA intersects line BC.
    Points are tuples: (x, y)
    """
    x1, y1 = D
    x2, y2 = A
    x3, y3 = B
    x4, y4 = C
    
    # Calculate the denominator (determinant)
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    
    # If denominator is 0, lines are parallel and will never intersect
    if denom == 0:
        return None 
    
    # Calculate the intersection point
    px = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
    py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom
    
    return px, py

# --- Example Usage with Dummy Coordinates ---
# Replace these with your actual coordinate values
pt_D = (-60, 0)
pt_A = (0, 20)
pt_B = (0, 40)
pt_C = (60, 0)

intersection = find_intersection(pt_D, pt_A, pt_B, pt_C)

if intersection:
    print(f"The intersection is at: {intersection}")
else:
    print("The lines are parallel.")


"""
res1 = distance(0,2,0,6)
print("0,2 and 0,6 : ", res1)

res2 = distance(0,6,6,4)
print("0,2 and 0,6 : ", res2)

res3 = distance(0,2,6,4)
print("0,2 and 0,6 : ", res3)

angle1 = calc_tri_angle(res1,res2,res3)
print("angle between 0,2 and 0,6 : ",angle1)

print()
res4 = distance(60,0,20,-26.6)
print("c and e ", res4)
res5 = distance(60,0,0,-40)
print("c and b ", res5)

ratio = res4/res5
print(ratio)

fx = 60 + ratio * (0-60)
fy = 0 + ratio * (20-0)
print(fx)
print(fy)
"""


"""

#point A (-350,cy)
    #point B (350,cy)

    pyautogui.moveTo(cx-450,cy)# A
    xA,yA = pyautogui.position()
    print("point A x,y : ",xA,yA)
    pyautogui.moveTo(cx-450,cy-1)
    pyautogui.dragTo(cx-450,cy+1,duration=speed,button='left')
    
    pyautogui.moveTo(cx+450,cy)# B
    xB,yB = pyautogui.position()
    print("point B x,y : ",xB,yB)
    pyautogui.moveTo(cx+450,cy-1)
    pyautogui.dragTo(cx+450,cy+1,duration=speed,button='left')

    # 1
    pyautogui.moveTo(cx-70,cy+320) # point 1
    x1,y1 = pyautogui.position()
    print("point 1 x,y : ",x1,y1)
    pyautogui.dragTo(cx-70,cy+120,duration=speed,button='left') # point 2
    x2,y2 = pyautogui.position()
    print("point 2 x,y : ",x2,y2)

    # 1 = x1,y1
    # 2 = x2,y2


    
      A *                                   * B
                        7

              5~                ~6
                |               |              
                |       2       |
                |       |       |
              4~        |       ~3
                        |    
                        1

    # for finding the intersection point 3 that forms from A2 and 1B line 
    # cramers rule to be used

    #point 3
    point_A = (xA,yA)
    point_2 = (x2,y2)
    point_1 = (x1,y1)
    point_B = (xB,yB)

    x3,y3 = find_intersection(point_A, point_2, point_1, point_B)
    print("point 3 x,y : ",x3,y3)
    # point 3 is x3,y3

    #will do the same for finding 4 
    #point 4
    x4,y4 = find_intersection(point_B, point_2, point_1, point_A)
    print("point 4 x,y : ",x4,y4)

    # point 5
    # for this point we will use similarity of triangles ratio as 45 and 12 will be parallel
    # so need the ratio of distances for A4 and A1

    dist_A4 = distance(xA,yA,x4,y4)
    dist_A1 = distance(xA,yA,x1,y1)

    ratio = dist_A4/dist_A1

    # for finding point 5 use formula
    x5 = xA + ratio * (x2 - xA)
    y5 = yA + ratio * (y2 - yA)

    # point 6
    # same as point 5
    
    dist_B3 = distance(xB,yB,x3,y3)
    dist_B1 = distance(xB,yB,x1,y1)

    ratio = dist_B3/dist_B1

    # for finding point 6 use formula
    x6 = xB + ratio * (x2 - xB)
    y6 = yB + ratio * (y2 - yB)

    # point 7
    point_6 = (x6,y6)
    point_5 = (x5,y5)
    # intersection b/w line A6 and line B5
    x7,y7 = find_intersection(point_A, point_6, point_B, point_5)
    print(x7,y7)
    print(x6,y6)


    # drag to 6
    pyautogui.dragTo(x6,y6,duration=speed,button='left')
    # drag to 3
    pyautogui.dragTo(x3,y3,duration=speed,button='left')
    # drag to 1
    pyautogui.dragTo(x1,y1,duration=speed,button='left')
    # drag to 4
    pyautogui.dragTo(x4,y4,duration=speed,button='left')
    # drag to 5
    pyautogui.dragTo(x5,y5,duration=speed,button='left')
    # drag to 2 
    pyautogui.dragTo(x2,y2,duration=speed,button='left')
    # move to 6
    pyautogui.moveTo(x6,y6)
    # drag to 7
    pyautogui.dragTo(x7,y7,duration=speed,button='left')
    # drag to 5
    pyautogui.dragTo(x5,y5,duration=speed,button='left')




"""


"""

      A *                                   * B
                        7

              4~                ~6
                |               |              
                |       2       |
                |       | 8     |
              3~        |       ~5
                        |    
                        1    

                        
                        * C


"""