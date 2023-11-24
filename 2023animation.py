from manim import *
from numpy import *

##draw a circle to a screen
class DrawImage(Scene):
    def construct(self):
        ##create an image object from stomach.png
        img = ImageMobject("stomach.png")
        img.scale(3)
        self.play(FadeIn(img))
        self.wait(1)
        ##draw 10 red triangles in two columms of 5 on each side of the image
        for i in range(5):
            triangle = Triangle(color=RED)
            #fill the triangles with red
            triangle.set_fill(RED, opacity=1)
            triangle.scale(0.2)
            triangle.shift(LEFT*5.5 + UP*2.5 + DOWN*i)
            self.play(Create(triangle), run_time=0.1)
            triangle2 = Triangle(color=RED)
            triangle2.set_fill(RED, opacity=1)
            triangle2.scale(0.2)
            triangle2.shift(RIGHT*5.5 + UP*2.5 + DOWN*i)
            self.play(Create(triangle2), run_time=0.1)
        self.wait(1)
        ##draw a box around the stomach
        