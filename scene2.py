from tkinter import Tk, Canvas, Frame, BOTH
import random

def main():
    root = Tk()
    # Scene()
    root.geometry("800x600")
    root.mainloop()

def initUI(self):
    self.master.title("Scene")


def draw_scene(canvas, left, top, right, bottom):
    drawSky(canvas)
    drawGround(canvas)
    drawCloud(canvas, 5, 50)
    drawGrass(canvas)

def drawSky(canvas):
    canvas.create_rectangle(0, 0, 799, 599, fill="#99ccff")

def drawGround(canvas):
    canvas.create_rectangle(0, 474, 799, 599, fill="70483c", width=0)

def drawCloud(canvas, cloudGroups, cloudsPerGroup):
    if cloudGroups > 56:
        cloudGroups = 56
    
    tryCent = []

    xRange = int(1000 / cloudGroups) if cloudGroups < 20 else 50
    yRange = int(500 / cloudGroups ) if cloudGroups < 20 else 25

    for _ in range(cloudGroups):
        while True:
            xCent = random.randint(0, 799)
            yCent = random.randint(0, 349)


def drawGrass(canvas):
    for _ in range(2250):
        x1 = random.randint(0, 799)
        y1 = random.randint(499, 599)

        fullCol = ['4', '', 'A', '', '1', '']
        fullCol[1], fullCol[3], fullCol[5], 




        