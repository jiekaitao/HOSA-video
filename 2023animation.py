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
        ##draw a triangle on the upper left corner of the  image and place text next to it
        triangle1 = Triangle(color=RED).scale(0.2).shift(RIGHT*4.8+UP*3)
        triangle1.set_fill(RED, opacity=1)
        self.play(Create(triangle1), run_time=0.1)
        text1 = Text("= Adrenaline", font="Serif", color=RED).scale(0.4).shift(RIGHT*6+UP*3.2)
        self.play(Write(text1))
        
        circle1 = Circle(color=GREEN, fill_opacity=0.5).scale(0.2).shift(RIGHT*3.4+UP*2.7)
        circle1.set_fill(GREEN, opacity=0.5)
        self.play(Create(circle1), run_time=0.1)
        text2 = Text("= Monoamine Oxidase", font="Serif", color=GREEN).scale(0.4).shift(RIGHT*5.4+UP*2.7)
        self.play(Write(text2))
        ##draw 10 red triangles in two columms of 5 on each side of the image and store the trianles in a np array
        triangles = []
        for i in range(5):
            triangles.append(Triangle(color=RED).scale(0.05).shift(LEFT*3.5+UP*(i-2)))
            triangles.append(Triangle(color=RED).scale(0.05).shift(RIGHT*3.5+UP*(i-2)))
        ##draw the triangles to the screen
        for triangle in triangles:
            triangle.set_fill(RED, opacity=1)
            self.play(Create(triangle), run_time=0.1)
        ##create text on the upper right corener of the screen
        text = Text("During a panic attack feelings of nausea\nare caused by a sudden rush of adrenaline\nto the stomach", font="Serif", color=WHITE).scale(0.4).shift(LEFT*4+UP*3)
        self.play(Write(text))
        self.wait(1)
        ##move the triangles towards the center of the screen
        self.play(triangles[0].animate.shift(RIGHT*5, UP*1.5),
                  triangles[1].animate.shift(LEFT*3.3, UP*0.5), 
                  triangles[2].animate.shift(RIGHT*6, UP*1.4), 
                  triangles[3].animate.shift(LEFT*2.4, UP*1.1), 
                  triangles[4].animate.shift(RIGHT*3.4, DOWN*2), 
                  triangles[5].animate.shift(LEFT*1.3, UP*1.3), 
                  triangles[6].animate.shift(RIGHT*4.6, DOWN*3), 
                  triangles[7].animate.shift(LEFT*1.4, DOWN*2.5), 
                  triangles[8].animate.shift(RIGHT*5.6, DOWN*2.7), 
                  triangles[9].animate.shift(LEFT*2.5, DOWN*3), run_time=0.5)
        self.play(Unwrite(text), run_time=0.5)
        ##create 10 circles with a missing section and store them in an array
        
        text = Text("The enzyme Monoamine Oxidase is\ncapable of breaking down adrenaline", font="Serif", color=WHITE).scale(0.4).shift(LEFT*4+UP*3)
        self.play(Write(text))
        self.wait(1)
        circles = []
        for i in range(5):
            circles.append(Circle(color=GREEN, radius=0.1, fill_opacity=0.5).shift(LEFT*3.5+UP*(i-2)))
            circles.append(Circle(color=GREEN, radius=0.1, fill_opacity=0.5).shift(RIGHT*3.5+UP*(i-2)))
        ##draw the circles to the screen
        for circle in circles:
            self.play(Create(circle), run_time=0.1)
        self.play(circles[0].animate.shift(RIGHT*5, UP*1.5),
                  circles[1].animate.shift(LEFT*3.3, UP*0.5), 
                  circles[2].animate.shift(RIGHT*6, UP*1.4), 
                  circles[3].animate.shift(LEFT*2.4, UP*1.1), 
                  circles[4].animate.shift(RIGHT*3.4, DOWN*2), 
                  circles[5].animate.shift(LEFT*1.3, UP*1.3), 
                  circles[6].animate.shift(RIGHT*4.6, DOWN*3), 
                  circles[7].animate.shift(LEFT*1.4, DOWN*2.5), 
                  circles[8].animate.shift(RIGHT*5.6, DOWN*2.7), 
                  circles[9].animate.shift(LEFT*2.5, DOWN*3), run_time=0.5)
        self.wait(0.5)
        self.play(Unwrite(text), run_time=0.5)
        text = Text("Our innotavtion, the PanX pill,\nwill deliver the Monoamine Oxidase.\nThen the enzyme in the pill will\nbreakdown the adrenaline in the stomach", font="Serif", color=WHITE).scale(0.4).shift(LEFT*3.8+UP*3)
        self.play(Write(text))
        self.wait(1)
        self.play(circles[0].animate.shift(UP*0.2),
                  circles[1].animate.shift(UP*0.2), 
                  circles[2].animate.shift(UP*0.2), 
                  circles[3].animate.shift(UP*0.2), 
                  circles[4].animate.shift(UP*0.2), 
                  circles[5].animate.shift(UP*0.2), 
                  circles[6].animate.shift(UP*0.2), 
                  circles[7].animate.shift(UP*0.2), 
                  circles[8].animate.shift(UP*0.2), 
                  circles[9].animate.shift(UP*0.2), run_time=0.5)
        
        self.play(Uncreate(triangles[0]),
                  Uncreate(triangles[1]), 
                  Uncreate(triangles[2]), 
                  Uncreate(triangles[3]), 
                  Uncreate(triangles[4]), 
                  Uncreate(triangles[5]), 
                  Uncreate(triangles[6]), 
                  Uncreate(triangles[7]), 
                  Uncreate(triangles[8]), 
                  Uncreate(triangles[9]), run_time=0.5)
        self.wait(1)
        self.play(Unwrite(text), run_time=0.5)
        text = Text("The enzyme will then be denatured\nby the acidic environment in the stomach", font="Serif", color=WHITE).scale(0.4).shift(LEFT*3.8+UP*3)
        self.play(Write(text))
        self.wait(1)
        self.play(Uncreate(circles[0]),
                  Uncreate(circles[1]), 
                  Uncreate(circles[2]), 
                  Uncreate(circles[3]), 
                  Uncreate(circles[4]), 
                  Uncreate(circles[5]), 
                  Uncreate(circles[6]), 
                  Uncreate(circles[7]), 
                  Uncreate(circles[8]), 
                  Uncreate(circles[9]), run_time=0.5)
        self.wait(3)
        self.play(Unwrite(text), Unwrite(text1), Unwrite(text2), Uncreate(triangle1), Uncreate(circle1), FadeOut(img))
        self.wait(1)