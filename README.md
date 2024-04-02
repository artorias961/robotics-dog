# Idea of the Project

This project aims to develop a guided tour robot designed to assist individuals with disabilities in navigating the California State University, Los Angeles campus. The robot will utilize detailed floor plans of campus buildings and follow a pre-set route. It will be equipped with advanced computer vision technology to detect and avoid obstacles, enhancing safe navigation. Key features include:

1. Diverse Sensor Array: The robot will employ a variety of sensors like LiDAR, ultrasonic sensors, cameras, IR proximity sensors, and a GPS module. These tools will gather essential data about the environment, aiding in the robot's localization and obstacle detection.

2. Internal Monitoring Sensors: Internally, the robot will have Inertial Measurement Units (IMUs), position sensors, load sensors, and current sensors. These will monitor the robot's status and ensure smooth operation.

3. Microcontroller and Processor Integration: The gathered sensor data will be processed by microcontrollers, which in turn feed into a central microprocessor. This setup allows for efficient data handling and control.

4. Operating System and Control Software: Ubuntu will be the operating system to manage high-level algorithms. The control software programmed into the system will execute precise commands, directing the robot's movements.

5. Actuation System: The robot's movement will be controlled by various motors, including servo, stepper, and brushless motors. This setup ensures a wide range of motion and adaptability to different terrains.

6. Power Management: Electronic subsystems will be implemented to power the motors and regulate the overall power supply, ensuring consistent and efficient energy usage.

7. Structural Design: The robot's exterior will primarily consist of 3D-printed components, supported by a robust, load-bearing internal frame. This design ensures durability while remaining lightweight for ease of maneuverability.

This tour robot is specially designed to make the Cal State LA campus more accessible to people with disabilities, offering a reliable and safe way to explore and navigate the university's facilities.

# More In Depth

x means to specific

- Electronics
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
    - Dog may use the possible algorithm called [beacon](https://kontakt.io/what-is-a-beacon/)
  - Dog must use a microprocessor to control all communications for the system
    - Once have all the requirements and specifications, then technology mapping
        - Find the technology that will help us solve the problem (meets specification) 
  - Dog battery life must idle must at least 45 minutes of battery life and in motion Dog must maintain 15 minutes
  - Dog eletrical components must be rated at IP66
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
- Mechanical
  - Dog must weigh 25 pounds at most
    - Dimensions will depend on maximum load (dog's weight)
  - Dog must be able to travel indoors on flat surfaces
    - Dog must be stable while in movement
    - Dog must be able to support itself while 1 or 2 legs are off the ground, depending on gait (crawl gait for now)
    - Body's casing will be light and will offer minimal protection from the elements
      - The dog will not be waterproof and will be rated IP66  
    - Limbs must be able to resist failure under load (dog's weight)
      - [Infill patterns](https://all3dp.com/2/cura-infill-patterns-all-you-need-to-know/) and density will vary depending on load at a given point
      - Limbs with "feet" will contain plastic or rubber material for friction
    - Legs will work with 3 DOF
      - 2 servos at the shoulders will be responsible 2 DOF while 1 at the knees will provide the third
  
 
  

### Electrical Point of View

One of the main issues will be the servo motors due to how much power to drive, weight, and the load it can load. If each leg has 2 servo motors then powering the servos will be a problematic. Not only that, the weight of the servos and the battery will be greatly impact the weight and depending on the size of the dog will limit what type of servo's can be used. 



### Hardware Point of View

One mechanical concern lies with the design of the dogs legs. Any engineering project aims to be efficient with resources given certain goals and parameters. The design for structure of the dog’s legs will determine how much material is used, how much weight they can support, the material’s performance in different environments, and the tasks it can assist in accomplishing. We have a few parameters in mind to guide certain design choices, but we will likely elaborate more on these design choices throughout the project. 



# Reference
- 3D Printer Related
  - [Infill Pattern](https://all3dp.com/2/cura-infill-patterns-all-you-need-to-know/)

