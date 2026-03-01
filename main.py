import pygetwindow as gw
import pyautogui
import time
import math
import keyboard
import random

pyautogui.FAILSAFE = True

from cube import start_drawing_sequence
from geo import distance,find_intersection,find_point_on_line

def get_paint_canvas():
    """
    Finds the MS Paint window and calculates the 'Safe Drawing Zone'.
    """
    try:
        # 1. Find the window by its title (usually 'Untitled - Paint' or just 'Paint')
        # We grab the first one that matches
        paint_window = gw.getWindowsWithTitle('Paint')[0]
        
        # 2. Activate it (bring to front)
        if not paint_window.isActive:
            paint_window.activate()
            
        # 3. Define the Safe Zone
        # We add offsets to avoid drawing over the Ribbon/Toolbars at the top
        # and the scrollbars at the right/bottom.
        safe_zone = {
                'min_x': paint_window.left + 15,           # Skip left toolbar area
            'max_x': paint_window.left + paint_window.width - 27, 
            'min_y': paint_window.top + 190,           # Skip the top Ribbon (Home/View tabs)
            'max_y': paint_window.top + paint_window.height - 65
        }
        
        return safe_zone
        
    except IndexError:
        print("Error: Could not find MS Paint! Is it open?")
        return None

def clamp(value, min_val, max_val):
    """
    The 'Invisible Fence'.
    If value is 1000 but max is 800, it returns 800.
    """
    return max(min_val, min(value, max_val))

def draw_circle_with_brush(bounds, radius=100, step=20):
    """
    bounds: The Safe Zone dictionary
    radius: Size of the circle
    step: Roughness (Lower = smoother circle, Higher = faster drawing)
    """
    
    # 1. Calculate the Center of the Safe Zone
    center_x = (bounds['min_x'] + bounds['max_x']) / 2
    center_y = (bounds['min_y'] + bounds['max_y']) / 2
    
    print(f"Drawing circle at Center: {center_x}, {center_y}")

    # 2. Move to the starting position (0 degrees, right side of circle)
    # math.cos(0) is 1, math.sin(0) is 0
    start_x = center_x + radius
    start_y = center_y
    
    pyautogui.moveTo(start_x, start_y)
    
    # 3. Start Drawing (Press Mouse Down)
    # We do NOT use Shift here, or Paint will force a straight line.
    pyautogui.mouseDown(button='left')

    # 4. Loop through angles (0 to 360 degrees)
    # We use a 'step' to skip points. Step 1 is very slow. Step 5 is good.
    for angle_deg in range(0, 361, step):
        # Convert degrees to radians (Python math requires radians)
        angle_rad = math.radians(angle_deg)
        
        # --- THE COORDINATE GENERATION ---
        x = center_x + radius * math.cos(angle_rad)
        y = center_y + radius * math.sin(angle_rad)
        # ---------------------------------
        
        # Move the mouse to the new coordinate
        # duration=0 makes it move instantly for a smooth stroke
        pyautogui.moveTo(x, y, duration=0)

    # 5. Release Mouse
    pyautogui.mouseUp(button='left')
    print("Circle Complete.")

def draw_cube(bounds, s=0):
    
    c_x = (bounds['min_x'] + bounds['max_x']) / 2
    c_y = (bounds['min_y'] + bounds['max_y']) / 2



    pyautogui.moveTo(c_x, c_y, duration=s)
    pyautogui.dragTo(c_x-150, c_y, duration=s, button='left')#b1
    pyautogui.dragTo(c_x-150, c_y-150, duration=s, button='left')#b2
    pyautogui.dragTo(c_x, c_y-150, duration=s, button='left')#b3
    pyautogui.dragTo(c_x, c_y, duration=s, button='left')#b4
    pyautogui.dragTo(c_x+75, c_y+75, duration=s, button='left')#t1
    pyautogui.dragTo(c_x-75, c_y+75, duration=s, button='left')#t2
    pyautogui.dragTo(c_x-75, c_y-75, duration=s, button='left')#t3
    pyautogui.dragTo(c_x+75, c_y-75, duration=s, button='left')#t4
    pyautogui.dragTo(c_x+75, c_y+75, duration=s, button='left')#t1
    pyautogui.moveTo(c_x-75, c_y+75, duration=s)#move to t2
        #drag to b2
    pyautogui.dragTo(c_x-150, c_y, duration=s, button='left')
    pyautogui.moveTo(c_x-150, c_y-150, duration=s)#move to b2
        #drag to t3
    pyautogui.dragTo(c_x-75, c_y-75, duration=s, button='left')
    pyautogui.moveTo(c_x+75, c_y-75, duration=s)
    pyautogui.dragTo(c_x, c_y-150, duration=s, button='left')




choice = int(input("number of times to run ?"))

try:
    while choice > 0:
        # 1. Setup Phase
        bounds = get_paint_canvas()

        if bounds:
            print(f"Locked to area: {bounds}")
            
            # Define speed for the demo
            speed = 0

            print("Moving to Safe Zone corners...")

            # Center (Calculate average of min and max)
            cx = (bounds['min_x'] + bounds['max_x']) / 2
            cy = (bounds['min_y'] + bounds['max_y']) / 2
            #pyautogui.moveTo(cx, cy, duration=speed)
            print("Center: ",cx,cy)

            """
            
            A *                                   * B
                                7

                    4~                ~6
                        |               |              
                        |       2       |
                        |       |       |
                    3~        |       ~5
                                |    
                                1    

                                
                                * C
            
            
            """    

            print("move the mouse to position A and press a")
            keyboard.wait("a")
            xa,ya = pyautogui.position()
            print("A : ",xa,ya)
            time.sleep(0.5)

            print("move the mouse to position B and press b")
            keyboard.wait("b")
            xb,yb = pyautogui.position()
            print("B : ",xb,yb)
            time.sleep(0.5)

            """
            print("move the mouse to position C and press c")
            keyboard.wait("c")
            xc,yc = pyautogui.position()
            print("C : ",xc,yc)
            time.sleep(0.5)
            """
            
            pyautogui.moveTo(cx,cy+250)
            xc,yc = pyautogui.position()
            print("C : ",xc,yc)

            pnt_A = (xa,ya)
            pnt_B = (xb,yb)
            pnt_C = (xc,yc)

            pyautogui.moveTo(xa,ya)
            pyautogui.dragTo(xa,ya+2)

            pyautogui.moveTo(xb,yb)
            pyautogui.dragTo(xb,yb+2)

            pyautogui.moveTo(xc,yc)
            pyautogui.dragTo(xc,yc+2)
        

            pyautogui.moveTo(cx,cy+150)
            x1,y1 = pyautogui.position()
            
            pyautogui.moveTo(cx,cy-150)
            x2,y2 = pyautogui.position()

            # randomizing height
            y_t = random.uniform(0.5,1.0)
            x_t = random.uniform(0.5,0.8)

            y2 = y1 + y_t * (y2-y1)
            x = x1 + x_t * (x2-x1)

            print("y2",y2)
            print("x",x)
            print("2",x2,y2)
            print("1",x1,y1)

            x1 = x
            x2 = x
            pyautogui.moveTo(x1,y1)     
            print("1 : ",x1,y1)       
            pyautogui.dragTo(x2,y2)
            print("2 : ",x2,y2)
            pnt_2 = x2,y2

            pyautogui.moveTo(x1,y1)
            x5,y5 = find_point_on_line(x1,y1,xb,yb)
            print("5 : ",x5,y5)
            pnt_5 = (x5,y5)
            pyautogui.dragTo(x5,y5)

            x6,y6 = find_intersection(pnt_C,pnt_5,pnt_2,pnt_B)
            print("6 : ",x6,y6)
            pnt_6 = (x6,y6)
            pyautogui.dragTo(x6,y6)    

            pyautogui.dragTo(x2,y2)
            pyautogui.moveTo(x1,y1)
            x3,y3 = find_point_on_line(x1,y1,xa,ya)
            print("5 : ",x3,y3)
            pnt_3 = (x3,y3)
            pyautogui.dragTo(x3,y3)

            x4,y4 = find_intersection(pnt_C,pnt_3,pnt_2,pnt_A)
            print("4 : ",x4,y4)
            pnt_4 = (x4,y4)
            pyautogui.dragTo(x4,y4)

            pyautogui.dragTo(x2,y2)
            x7,y7 = find_intersection(pnt_6,pnt_A,pnt_4,pnt_B)
            print("7 : ",x7,y7)
            pnt_7 = (x7,y7)

            pyautogui.moveTo(x6,y6)
            pyautogui.dragTo(x7,y7)
            pyautogui.dragTo(x4,y4)

            x8,y8 = find_intersection(pnt_A,pnt_5,pnt_B,pnt_3)
            print("8 : ",x8,y8)
            pnt_8 = (x8,y8)

            pyautogui.moveTo(x3,y3)
            pyautogui.dragTo(x8,y8)
            pyautogui.dragTo(x7,y7)
            pyautogui.moveTo(x5,y5)
            pyautogui.dragTo(x8,y8)

            shadow_choice = input("draw shadow? [y or n]: ").lower()

            if shadow_choice in ["y","yes"]:
                print("move the mouse and press 'o' to capture the up position")
                keyboard.wait("o")
                xsu1,ysu1 = pyautogui.position()
                print("source up : ",xsu1,ysu1)

            else:
                pass



        





            #draw_cube(bounds)
            #pyautogui.dragTo(cx+1,cy+1, duration=speed,button='left')

            #start_drawing_sequence(bounds)
            #draw_circle_with_brush(bounds, radius=150)
                
            
            #draw_cube_recurse(bounds,0,4)
            
        else:
            print("Could not find Paint to determine corners.")

        choice -= 1
except KeyboardInterrupt:
    print("\nstopped by user")