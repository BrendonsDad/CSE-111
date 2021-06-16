import tkinter as tk
import math
from random import *
import turtle

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    
    # canvas.create_oval(150, 150, 250, 250, fill="#ff0000", width=False)
    
    draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)
    #sky
    canvas.create_rectangle(0, 0, 800, 500, fill="#2D6A4F")
    #water
    canvas.create_rectangle(0, 350, 800, 500, fill="#006d77", width=False)
    #clouds

    #trees

    sun = [
        [280, 60, 2.4, '#40916C'], [290, 70, 2.2, '#52B788'], [300, 80, 2, '#74C69D'], [310, 90, 1.8, '#95D5B2'], [320, 100, 1.6, '#B7E4C7'], [330, 110, 1.4, '#D8F3DC'], [340, 120, 1.2, '#DBF4DF'], [350, 130, 1, '#E0F6E4'], [360, 140, 0.8, '#E6F7E9'], [370, 150, 0.6, '#EBF9EE'], [380, 160, 0.4, 'white']
    ]

    #flying turtle


    for sun_left, sun_top, scale, color in sun:
        draw_sun(canvas, sun_left, sun_top, scale, color)


    #clouds
    draw_clouds(canvas, 450, 120,)
    draw_clouds(canvas, 500, 100, scale=.75)
    draw_clouds(canvas, 550, 150, scale=.75)
    draw_clouds(canvas, -20, -20, scale=.75)
    

    for i in range(0,7):
        x1=randint(0,800)
        y1=randint(10, 75)
        x2=x1
        y2=randint(400,500)
        random_width=randint(25, 75)
        canvas.create_line(x1,y1,x2,y2, fill=random_color_code(), width=random_width)
        canvas.update()

    
    for i in range(0, 20):
        cw = 2
        ch = 2
        bug_left=randint(0,600)
        bug_top=randint(0,600)
        bug_right = bug_left + cw
        bug_bottom = bug_top +ch
        canvas.create_oval(bug_left, bug_top, bug_right, bug_bottom, fill="white", width = False)






def draw_clouds(canvas, cloud_left, cloud_top, scale=1):
    cloud_width = 400 * scale
    cloud_height = 125 * scale
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height
    cloud_center_x = cloud_left + (cloud_width / 2)
    cloud_center_y = cloud_top + (cloud_height / 2)

    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill="#7b9c93", width = False)
    
def random_color_code():
    hex_chars = ['#277D34', '#1F6429', '#174B1F', '#0F3215', '#08190A']
    color_code =  choice(hex_chars)
    return color_code



def draw_sun(canvas, sun_left, sun_top, scale=1, color="#d9ed92", ray_count = 0):



    sun_width = 100 * scale
    sun_height = 100 * scale
    ray_length = 100 * scale
    ray_width = 3 * scale
    

    sun_right = sun_left  + sun_width
    sun_bottom = sun_top + sun_height
    sun_center_x = sun_left + (sun_width / 2)
    sun_center_y = sun_top + (sun_height / 2)



    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill=color, width=False)

    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i 
        ray_x = sun_center_x + math.cos(angle) * ray_length
        ray_y = sun_center_y + math.sin(angle) * ray_length
        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, width=ray_width, fill="#d9ed92")

def draw_grid(canvas, left, top, right, bottom, grid_spacing): 
    #draw horizontal lines
    text_horizontal_margin = 20
    text_vertical_margin = 10

    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")
    
    #Draw verticla lines
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text=f"{i}")


main()








# draw_sun(canvas, 280, 60, scale=2.4, color='#40916C', ray_count=0)
# draw_sun(canvas, 290, 70, scale=2.2, color='#52B788', ray_count=0)
# draw_sun(canvas, 300, 80, scale=2, color='#74C69D', ray_count=0)
# draw_sun(canvas, 310, 90, scale=1.8, color='#95D5B2', ray_count=0)
# draw_sun(canvas, 320, 100, scale=1.6, color='#B7E4C7', ray_count=0)
# draw_sun(canvas, 330, 110, scale=1.4, color='#D8F3DC', ray_count=0)
# draw_sun(canvas, 340, 120, scale=1.2, color='#DBF4DF', ray_count=0)
# draw_sun(canvas, 350, 130, ray_count=0, color='#E0F6E4')
# draw_sun(canvas, 360, 140, ray_count=0, color='#E6F7E9', scale=.8)
# draw_sun(canvas, 370, 150, scale=0.6, color='#EBF9EE', ray_count=0)
# draw_sun(canvas, 380, 160, scale=0.4, color='white', ray_count=0)
