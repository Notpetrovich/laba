from random import randrange as rnd, choice
import tkinter as tk
import math
import time


class GameObject:
    def __init__(self, coords, velocity, canv):
        self.crd = [coords[0], coords[1]]
        self.vlc = [velocity[0], velocity[1]]
        self.cnv = canv
        
    def move(self, time):
        self.crd[0] += time*self.vlc[0]
        self.crd[1] -= time*self.vlc[1]

    def redraw(self):
        pass


class Ball(GameObject):
    def __init__(self, coords, velocity, radius, canv):
        super().__init__(coords, velocity, canv)
        self.r = radius
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = self.cnv.create_oval(
                self.crd[0] - self.r,
                self.crd[1] - self.r,
                self.crd[0] + self.r,
                self.crd[1] + self.r,
                fill=self.color
        )
        self.live = 100

    def redraw(self):
        self.cnv.coords(
                self.id,
                self.crd[0] - self.r,
                self.crd[1] - self.r,
                self.crd[0] + self.r,
                self.crd[1] + self.r,
        )

    def move(self, time):
        super().move(time)
        self.vlc[1] -= 1
        
        if self.crd[0] + self.r >= 800:
            self.crd[0] = 799 - self.r
            self.vlc[0] *= -1

        if self.crd[1] + self.r >= 520:
            self.crd[1] = 520 - self.r
            self.vlc[1] *= -0.5
            self.vlc[0] *= 0.5

        self.redraw()
        self.live -= 1

    def hittest(self, obj):
        s = math.sqrt((self.crd[0] - obj.x)**2 + (self.crd[1] - obj.y)**2)
        return s <= self.r + obj.r
       
