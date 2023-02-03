# Idea of the Project

A robotics dog is a type of robot that combines the fields of electrical engineering, mechanical engineering and software engineering to create a realistic and functional canine-like machine. The mechanical section of the dog would involve designing and building the physical structure of the robot, including the body, limbs, and tail. The electrical section would involve the integration of electronic components such as sensors, motors, and power systems to control the robot's movement and behavior. The software section would involve the programming and control of the robot's actions, including movements, speech and vision recognition, and decision-making capabilities. All these sections would work together to create a functional and realistic robotic dog that can perform various tasks, such as assisting with household tasks, providing companionship, or even assisting in search and rescue operations. Where more information will be found over in [LaTeX](https://www.overleaf.com/7552569246fycsxpckjfby).

# More In Depth

- Software
  - Use computer vision to detect color to determine different objects of color
  - Dectect objects such as 2D and/or 3D object 
  - Determine the distance of an object
  - If possible create an algorithm to find the main host and follow the host using computer vision (host must use distinct color or a local node such as a esp32 or pico w)
  - Control all servo motors that will be semi controlled by the camera's
  - Ultrasonic will be used to verify if the dog is near a wall (must be a flat surface and help the camera to detect different levels of surfaces)
  - The master board will either be a raspberry pi 4, PYNQ board, or a nano jetson board. All boards are capable to have slave boards if needed
- Mechanical
  - Determine what type of filament for the final product
  - Determine what type of [infill patterns](https://all3dp.com/2/cura-infill-patterns-all-you-need-to-know/)
  - What type of leg (how many degree of freedom)
  - Limit the weight of the dog between 10 to 25 pounds
  - What happen if all the weight is on three legs or possibly two legs? How will the weak points of the filament or chasis will be maintain or stress free
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

# Reference
- 3D Printer Related
  - [Infill Pattern](https://all3dp.com/2/cura-infill-patterns-all-you-need-to-know/)

