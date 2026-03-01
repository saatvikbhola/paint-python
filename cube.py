import pyautogui

def draw_cube(x,y,size,duration=0):

    if size%2!=0:
        size+=1
        d=size/2
    else:
        d=size/2

    # 1. Front Face (Square)
    # Start at bottom-right of front face (x,y)
    pyautogui.moveTo(x,y)
    pyautogui.dragTo(x-size, y, duration=duration, button='left')           #bottom edge
    pyautogui.dragTo(x - size, y - size, duration=duration, button='left') # Left edge
    pyautogui.dragTo(x, y - size, duration=duration, button='left')       # Top edge
    pyautogui.dragTo(x, y, duration=duration, button='left')             # Right edge (Back to start)

    # 2. Back Face (Offset Square)
    # Move to Back-Right-Bottom
    pyautogui.dragTo(x + d, y - d, duration=duration, button='left')      # Connector Bottom-Right
    pyautogui.dragTo(x + d, y - d - size, duration=duration, button='left') # Back Right edge
    pyautogui.dragTo(x - size + d, y - d - size, duration=duration, button='left') # Back Top edge
    pyautogui.dragTo(x - size + d, y - d, duration=duration, button='left') # Back Left edge
    pyautogui.dragTo(x + d, y - d, duration=duration, button='left')      # Back Bottom edge (Close back face)

    # 3. Connect remaining corners
    # We are currently at Back-Right-Bottom (x+d, y-d). 
    # Let's go to Top-Right-Back and connect to Top-Right-Front
    pyautogui.moveTo(x + d, y - d - size, duration=duration)
    pyautogui.dragTo(x, y - size, duration=duration, button='left')       # Connector Top-Right

    # Move to Top-Left-Back and connect to Top-Left-Front
    pyautogui.moveTo(x - size + d, y - d - size, duration=duration)
    pyautogui.dragTo(x - size, y - size, duration=duration, button='left') # Connector Top-Left

    # Move to Bottom-Left-Back and connect to Bottom-Left-Front
    pyautogui.moveTo(x - size + d, y - d, duration=duration)
    pyautogui.dragTo(x - size, y, duration=duration, button='left')       # Connector Bottom-Left


def recursive_draw_logic(x, y, size, n):
    """
    The actual recursive function.
    n: The number of cubes left to draw (depth)
    """
    # BASE CASE: Stop if n reaches 0
    if n <= 0:
        return

    print(f"Drawing cube level {n} at {x}, {y}")
    
    # 1. Draw the current cube
    draw_cube(x, y, size)
    
    # 2. RECURSIVE STEP
    # Calculate new position and size for the next cube.
    # Example: Shift Up-Right and make it 80% smaller
    
    if n%2==0: # 1st quadrant
        new_size =size*0.6
        new_x = x + 75
        new_y = y + 75
    elif n%3==0:  # 2nd quadrant
        new_size =size*0.9
        new_x = x - 75
        new_y = y + 75
    elif n%5==0:
        new_size =size*0.7
        new_x = x + 75
        new_y = y - 75
    else:
        new_size =size*1
        new_x = x - 75
        new_y = y - 75
    
    recursive_draw_logic(new_x, new_y, new_size, n - 1)


def start_drawing_sequence(bounds):
    """
    Wrapper to handle the SHIFT key safely.
    """
    # Calculate Center only once at the start
    start_x = (bounds['min_x'] + bounds['max_x']) / 2
    start_y = (bounds['min_y'] + bounds['max_y']) / 2
    
    initial_size = 150
    depth = 5  # How many cubes to draw

    try:
        # Start the recursion
        recursive_draw_logic(start_x, start_y, initial_size, depth)
        
    except KeyboardInterrupt:
        print("Stopped by user.")
