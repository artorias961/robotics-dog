# Idea of the Project

A robotics dog is a type of robot that combines the fields of electrical engineering, mechanical engineering and software engineering to create a realistic and functional canine-like machine. The mechanical section of the dog would involve designing and building the physical structure of the robot, including the body, limbs, and tail. The electrical section would involve the integration of electronic components such as sensors, motors, and power systems to control the robot's movement and behavior. The software section would involve the programming and control of the robot's actions, including movements, speech and vision recognition, and decision-making capabilities. All these sections would work together to create a functional and realistic robotic dog that can perform various tasks, such as assisting with household tasks, providing companionship, or even assisting in search and rescue operations. Where more information will be found over in [LaTeX](https://www.overleaf.com/7552569246fycsxpckjfby).

The purpose of this project is to create a tour bot that will guide Cal State LA guests to locations on campus. The tour bot will be given a dataset of the school building’s floor plans and a predetermined path to follow. The bot will be a mobile platform that will incorporate computer vision to identify obstacles and facilitate localization. The collection of sensors used to navigate the environment may also incorporate LiDAR, ultrasonics, cameras, IR proximity, and a GPS module that will focus on gathering data of the surrounding environment. While the internal sensors will consist of IMUs, position sensors, load sensors, and current sensors. The sensors will report to slaved microcontrollers that will feed into the microprocessor. Ubuntu is currently the planned operating system to control high level algorithms. The control software will dictate commands to the tour bot actuators consisting of servo, stepper, and brushless motors. Electronic subsystems will be used to power the motors and to regulate the power supply. The majority of the tour bot chassis will be a 3D printed, built around a load bearing internal frame. 

# More In Depth

x means to specific

- Software
  - Dog must be set in interior setting
  - Dog must avoid objects on the floor
    - Determine if the object is not the wall, floor, or any flat surfaces
        - x Use computer vision to detect color to determine different objects of color
        - x Dectect objects such as 2D and/or 3D object
    - Determine the distance of an object
        - Ultrasonic will be used to verify if the dog is near a wall (must be a flat surface and help the camera to detect different levels of surfaces)
    - Dog must make sure won't hit the object 
        - x Control all servo motors that will be semi controlled by the camera's
  - Dog must be able to follow owner
    - x If possible create an algorithm to find the main host and follow the host using computer vision or [beacon](https://kontakt.io/what-is-a-beacon/)
  - x The master board will either be a raspberry pi 4, PYNQ board, or a nano jetson board. All boards are capable to have slave boards if needed
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
  - Electrical components for the dog
    - Batteries
    - Voltage regulator
    - servo's or brushless motors
    - camera
    - wiring
  - Must have a port to connect an LCD with a few buttons to read live data from the dog if wireless communication fails
  - Temperature management
  - Airflow
  - Simple and Unique design
  - May use a raspberry pi board, pynq board, or nano jetson
  - How to save enough power 
  

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

