# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [CircuitPython Distance Sensor ](#CircuitPython Distance Sensor )
* [Motor control](#Motor control)
* [NextAssignmentGoesHere](#NextAssignment)
---











## CircuitPython Servo

### Description & Code Snippets
* Get a 180° micro servo to slowly sweep back and forth between 0 and 180°.   
* Spicy part: Now control the servo with 2 buttons. 
The servo only moves if you are pushing a button.

### Code
```python
while True:
    print(button.value)
    if button.value:  # Button is pressed (remember, we're assuming it's pull-down)
        print("btn1 pressed \t")
        print(current_angle)
        current_angle = current_angle + 10
        current_angle = max(0, min(360, current_angle))
        my_servo.angle = current_angle  # Set the new angle
    time.sleep(0.05)  # Small delay to avoid excessive checking

    print(button2.value)
    if button2.value:  # Button is pressed (remember, we're assuming it's pull-down)
        print("btn2 pressed \t")
        print(current_angle)
        current_angle = current_angle - 10
        current_angle = max(0, min(360, current_angle))
        my_servo.angle = current_angle  # Set the new angle
    time.sleep(0.05)  # Small delay to avoid excessive checking

```

[circuitpython servo](Servo.py)
### Evidence
![RealServoMotorGif](https://github.com/JoshBricker30/Engineering3/assets/143528213/35437bbd-0508-41a0-a0ef-7c059317a960)

### Wiring

<img src="images/servowiring.png" size="50%">

[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)
### Reflection











## CircuitPython Distance Sensor 

### Description & Code Snippets
In this assignment we are supposed to combine new knowlage and prior knowlage from last year by making a ultrasonic sensor that controls a RBG LED. We will do this by combining the LED code and saying when a distance is then change the color. THe goal is to get it to change from red up close to blue in the middle and green far way.

#### code
```python
from rainbowio import colorwheel
import neopixel
import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)


NUMPIXELS = 6  # Update this to match the number of LEDs.
BRIGHTNESS = 0.2  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.NEOPIXEL  # This is the default pin on the 5x5 NeoPixel Grid BFF.

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)

print("starting up...")
while True:
    try:
        print((sonar.distance,))
        cm = sonar.distance
        print(cm)
        if cm < 5:
            pixels.fill(RED) 
        elif cm > 35:
            pixels.fill(GREEN)
        else:
          pixels.fill(BLUE)
        pixels.show()
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)    
```

https://github.com/JoshBricker30/Engineering3/blob/main/lib/DistanceSensor.py
### Evidence

#### Reflection
This code was difficult until i understood that the distance sensor is just saying print the value that its picking up anyway. Then to set the colors on the neopixle from my old code to save myself a step. I then figured out that the code was simply saying if the distance is more or less then a certain value activate this color. And now when putting it all together and adding a few tweaks made it work.


### Wiring
<img src="images/distance wiring.jpg" size="50%">












## Motor control

### Description & Code Snippets
The goal of this assignment is to wire a DC motor to a metro board with a 9v battery pack without burning out any of the wires. Then the code was simple all it was is getting the dc motor to simply turn on and to be able to control it through a potentiomotor.

```python
import time 
import board
from analogio import AnalogIn
import pwmio
from digitalio import DigitalInOut

#pins
potentiometerpin = AnalogIn(board.A0)
motorpin = pwmio.PWMOut(board.D7)

#prints the potentiometer value then writes it to the motor
while True:
    print(potentiometerpin.value)
    time.sleep(0.1)
    motorpin.duty_cycle = potentiometerpin.value
```
[circuitpython DistanceSensor](DistanceSensor.py)
**Lastly, please end this section with a link to your code or file.**  

### Evidence
![MotorControlGIF](https://github.com/JoshBricker30/Engineering3/assets/143528213/982b988a-29f7-4c15-a3b9-10a09a2e5666)

### Wiring
<img src="images/Motor Control Wiring.png" size="50%">

  

### Reflection
For this assingment i enjoyed the coding becuase it was very easy. But the wiring on the other hand was not easy at all it reqiured a lot of extra percaution since there was a lot of electricity flowing threw and could have burned something out. What made it so difficultis the placement of all the resisors along with all the extra potentiemotor wiring.











## Onshape_Hanger_Assignment

### Assignment Description

This was our first assigenment being back at onshape and we had to design a simple hanger. This was our first practice part for the onshape exam aswell. This is mostly a warmup assigment that gives us reminders of onshape skills.
### Evidence

<img src="images/hangerfront.png" size="50%">
<img src="images/hangerside.png" size="50%">
<img src="images/hangertop.png" size="50%">



### Part Link 

[Create a link to your Onshape document]
https://cvilleschools.onshape.com/documents/be93d5075161051205e997e4/w/d2c856fb1567cf9c57654302/e/1a54adff2da9b8ab0c5bcce5?renderMode=0&uiState=6529600c9cf7365098a3501e

### Reflection

This assignment was a great reminder For How onshape worked, and a good warm up. It felt good to be back to 3d design and away from code. I liked how this included a lot of the most important onshape tools. It made me think about when to use reflections cause when i did it right i only had to do half the amount of work. And honestly the documentation for onshape makes more sense and is easier.

&nbsp;













## Onshape_Swing_arm

### Assignment Description

For this assigment we were supposed to design a swing arm in 3d design cad workspace. This assigment reqiures more advanced onshape tools along with more thinking reqiured for the order of how to do the assigemnt. we also had to fil;l in some blanks for the deimenisoning of this assigment. We had Mutiple pictures to figure out how to do this but that was about it.

### Evidence

<img src="images/swingfront.png" size="50%">
<img src="images/swingside.png" size="50%">
<img src="images/swingtop.png" size="50%">

### Part Link 

[Create a link to your Onshape document]
https://cvilleschools.onshape.com/documents/1d2a66ba1e76c0ab924b0091/w/d5315b704b182d8b71e56040/e/f8a7ce35703c19fea9b31bc6?renderMode=0&uiState=652d51d6f5617a59bb8d3c34

### Reflection

For this assingment i struggled with the dimensions and putting the parts together. The diminsions were tricky becuase we had to figure them out based on other things for some parts of it, which means if we got one diminsion wrong it couldve messed up the whole project. And putting the parts together was difficult becuase i couldnt figure out wether to put everything in one sketch or two add on to an already extruted part of the swing arm. This was a good learning expeirce for me on how to use new tools like the 3 point arc and tangent. Overall it was easy enough that it was possible for my level of cad but hard enough that I leanred from it.
&nbsp;













## MultipartStudio_part_1

### Assignment Description
The goal of this assingment is to learn how to design mutiple parts in one studio that are all still connected. Then Once done with first part of making it there are questions and challanges we have to complete. We are also getting genreal 3d design practice.

### Evidence

<img src="images/MultipartFront.png" size="50%">
<img src="images/MultipartSide.png" size="50%">
<img src="images/MultipartTop.png" size="50%">
<img src="images/MultipartBottom.png" size="50%">


### Part Link 

[Create a link to your Onshape document]https://cvilleschools.onshape.com/documents/46387862641204135bf95322/w/d70628ab6e2940eb7a2e048c/e/4e490dad8a37880fc56a470a?renderMode=0&uiState=654512817dd338189ff0f485

### Reflection

This assingment was challenging due to THe complexty of adding the new parts on to the already exsisting parts of the design. Since you cant make any mistakes and need all the parts to fit together correctly like a puzzle. I also thought the the whole on the top cap was overcomplicated since you have to figure out dimensions on your own and use the revolve tool.Overall it was good practice and has expanded my understading of onshape.
&nbsp;












## Multipart Part pt 1

### Assignment Description

The goal of this aasignment was to create a one part design in onshape. You are suppsoed to follow the pictures dimentions and create a complicated one part design. 

### Evidence
<img src="images/MultipartFront.png" size="50%">
<img src="images/MultipartSide.png" size="50%">
<img src="images/MultipartTop.png" size="50%">
<img src="images/MultipartBottom.png" size="50%">

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;









## Single

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence

Take several cropped screenshots of your Onshape document from different angles. Try to capture all important aspects of the design. Turn off overlays that obscure the parts, such as planes or mate connectors. Your images should have captions, so the reader knows what they are looking at!  

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;














## NextAssignment

### Description & Code Snippets
Write a couple sentences here, describing this assignment, and make sure that you hit these two points:
* What was the goal of the assignment?
* How did you accomplish that goal?
  How you accomplished the goal is NOT a reflection, it is you telling the reader how to do this assignment, in broad strokes.

  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```
[circuitpython DistanceSensor](DistanceSensor.py)
**Lastly, please end this section with a link to your code or file.**  

### Evidence

### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)
### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**






## Robot Arm Planning And Project

### Planning, Description
The goal of our robot arm is to be able to pick up an object and place it in a diffrent location based on the person controlling it. We plan to make our robot arm open and close with a screw like sytem powered by dc motors and double A batteries. We plan to 3D print our robot arm and make the wiring out of the materials provided by the engineering lab, which include 3 DC motors, male jumper cabels, Ardiuno, breadboard, other wiring related objects and 3d printed part's. The design is relativily simple with the main motion of the arm opening and closing and going up and down working on the screw sytem, and the arm moving right to left on a pully sytem connected to a frame. The code will make it so we have buttons that will control open close, up down, and side to side. Our goal is to make it work like a arcade claw machine but with buttons.
  

```python
import time 
import board
from analogio import AnalogIn
import pwmio
from digitalio import DigitalInOut

#pins
potentiometerpin = AnalogIn(board.A0)
motorpin = pwmio.PWMOut(board.D7)

while True:
    print(button.value)
    if button.value:  # Button is pressed (remember, we're assuming it's pull-down)
        print("btn1 pressed \t")
        print(current_angle)
        current_angle = current_angle + 10
        current_angle = max(0, min(360, current_angle))
    time.sleep(0.05)  # Small delay to avoid excessive checking

    print(button2.value)
    if button2.value:  # Button is pressed (remember, we're assuming it's pull-down)
        print("btn2 pressed \t")
        print(current_angle)
        current_angle = current_angle - 10
        current_angle = max(0, min(360, current_angle))
        print(potentiometerpin.value)
    time.sleep(0.1)
    motorpin.duty_cycle = potentiometerpin.value

    time.sleep(0.05)  # Small delay to avoid excessive checking

### Evidence
<img src="images/DesignPic1.png" size="50%">
<img src="images/DesignPic2.png" size="50%">
<img src="images/DesignPic3.png" size="50%">
### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)
### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**











## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence

Take several cropped screenshots of your Onshape document from different angles. Try to capture all important aspects of the design. Turn off overlays that obscure the parts, such as planes or mate connectors. Your images should have captions, so the reader knows what they are looking at!  

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;
