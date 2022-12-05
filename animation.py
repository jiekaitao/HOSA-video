from manim import *

#creata a class caller DynamicTV
class DynamicTV(Scene):
    #create a length and with for the screen
    length = 0
    width = 0
    volume = 100
    #create a variable called patientAwake and set it to true
    patientAwake = True

    #create a function called updatePatient
    def updatePatient(self, stateText, patientText):
        #create a if statement that checks if the patient is awake
        if self.patientAwake:
            #if the patient is awake then set the stateText to "awake"
            stateText = Text("awake").scale(0.5).set_x(patientText.get_x() + 1.8).set_y(patientText.get_y())
        else:
            #if the patient is not awake change the stateText to "asleep"
            #erase the stateText
            self.play(FadeOut(stateText))
            stateText = Text("asleep").scale(0.5).set_x(patientText.get_x() + 1.8).set_y(patientText.get_y())
            stateText.color = BLUE
        return stateText

    #create a function called construct
    def construct(self):
        #draw a rectangle with the length and width
        rect = Rectangle(width = self.length, height = self.width)
        #create a variable called tvOn that is a text object
        tvOn = Text("TV On")
        #write the word "Patient state: awake" on the upper corner of the rect
        patientText = Text("Patient state: ").scale(0.5).set_x(rect.get_x() - ((self.length / 2) - 1.5)).set_y(rect.get_y() + ((self.width / 2) - 0.5))
        patientText.color = RED
        #create a text object called stateText and set it to "awake"
        #and put it next to the patientText object
        stateText = Text("awake").scale(0.5).set_x(patientText.get_x() + 1.8).set_y(patientText.get_y())
        stateText.color = RED
        #write the volume on the bottom left corner of the rect
        volume = Text("Volume: " + str(self.volume)).scale(0.5).set_x(rect.get_x() - ((self.length / 2) - 1.25)).set_y(rect.get_y() - ((self.width / 2) - 0.3))
        volume.color = BLUE

        #play all the animations
        self.play(Create(rect), Create(tvOn), Create(patientText), Create(volume), Create(stateText))
        self.wait(2)
        self.patientAwake = False
        stateText = self.updatePatient(stateText, patientText)
        self.play(Create(stateText))




def main():
    #create and instance of DynamicTV
    tv = DynamicTV()
    #set the length and width of the screen
    tv.length = 10
    tv.width = 5
    #render the screen
    tv.render()

if __name__ == '__main__':
    main()
