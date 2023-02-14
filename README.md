# Idea of the Project

The purpose of this project is to create a tour bot that will guide Cal State LA guests to locations on campus. The tour bot will be given a dataset of the school building’s floor plans and a predetermined path to follow. The bot will be a mobile platform that will incorporate computer vision to identify obstacles and facilitate localization. The collection of sensors used to navigate the environment may also incorporate LiDAR, ultrasonics, cameras, IR proximity, and a GPS module that will focus on gathering data of the surrounding environment. While the internal sensors will consist of IMUs, position sensors, load sensors, and current sensors. The sensors will report to slaved microcontrollers that will feed into the microprocessor. Ubuntu is currently the planned operating system to control high level algorithms. The control software will dictate commands to the tour bot actuators consisting of servo, stepper, and brushless motors. Electronic subsystems will be used to power the motors and to regulate the power supply. The majority of the tour bot chassis will be a 3D printed, built around a load bearing internal frame. 

# More In Depth

x means to specific

- Software
  - Dog must be set in interior setting
  - Dog must avoid objects on the floor
    - Determine if the object is not the wall, floor, or any flat surfaces
        - Identify the shadows/color of an object
        - Identify an object from 2D or 3D
    - Determine the distance of an object
        - Ultrasonic will be used to verify if the dog is near a wall (must be a flat surface and help the camera to detect different levels of surfaces)
    - Dog must make sure won't hit the object 
        - Use kinematic model to identify walking motion and computer vision to avoid obstacles
  - Dog must be able to follow owner
    - x If possible create an algorithm to find the main host and follow the host using computer vision or [beacon](https://kontakt.io/what-is-a-beacon/)
  - Dog must use a microprocessor to control all communications for the system
    - Once have all the requirements and specifications, then technology mapping
        - Find the technology that will help us solve the problem (meets specification) 
- Mechanical
  - Dog must weigh 25 pounds at most
  - Dog must be stable while in movement using all four legs (creep like a donkey)
    - What happen if all the weight is on three legs or possibly two legs? 
    - How will the weak points of the filament or chasis will be maintain or stress free    
    -  x Determine what type of filament for the final product
    -  x Determine what type of [infill patterns](https://all3dp.com/2/cura-infill-patterns-all-you-need-to-know/)
    -  x What type of leg (how many degree of freedom)
  - Determine the environment the dog will be in
    - Terrain
    - Environment weather, temperature, and humidity
  - Traction for the feet
    - What material
  - Plastic casing for outside environment or possibly falling down 
    - weight
    - Density
  - Dimension of the dog
- Electrical
  - Dog may contain the following components:
    - Microprocessor
      - Nano Jetson
      - Raspberry Pi
      - PYNQ V2
    - Microcontrollers
      - Teensy 4.1
      - Raspberry Pi Pico
      - Arduino Nano 
      - Seeed Studio XIAO
    - Batteries
    - Voltage Regulator
    - Servo Motors
    - Brushless Motors
    - Ultrasonic Sensor
    - Hall Effect Sensor
    - Stereo Sensor
    - Speaker
    - Bluetooth Module
    - WiFi Module
    - Temperature management sensor
    - LiDAR
    - LCD 
    - Perf Boards
 
  

### Electrical Point of View

One of the main issues will be the servo motors due to how much power to drive, weight, and the load it can load. If each leg has 2 servo motors then powering the servos will be a problematic. Not only that, the weight of the servos and the battery will be greatly impact the weight and depending on the size of the dog will limit what type of servo's can be used. 



### Hardware Point of View

One mechanical concern lies with the design of the dogs legs. Any engineering project aims to be efficient with resources given certain goals and parameters. The design for structure of the dog’s legs will determine how much material is used, how much weight they can support, the material’s performance in different environments, and the tasks it can assist in accomplishing. We have a few parameters in mind to guide certain design choices, but we will likely elaborate more on these design choices throughout the project. 

# Goals

- Eletrical
  - 
- Software
  - 
- Mechanical

# Reference
- 3D Printer Related
  - [Infill Pattern](https://all3dp.com/2/cura-infill-patterns-all-you-need-to-know/)

