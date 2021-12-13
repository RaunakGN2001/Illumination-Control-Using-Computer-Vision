# Basic Info

#### Project Title
Illumination Control 🔆 Using Computer Vision 👁
#### Team Members 
- [Kaustav Saha](https://github.com/Kaustav-45)
- [Subhadeep Das](https://github.com/subhadeep01)
- [Soham Patra](https://github.com/Sohampatra1)
- [Raunak Gayen](https://github.com/RaunakGN2001)
#### Broad Areas our project focuses on
- Computer Vision
- Hand Gesture Recognition System
- Arduino
#### Hardware we used
- Arduino Nano V3
- Jumper Wires
- Breadboard
- LED
- 220Ω Resistor
- Cable for Arduino Nano
#### Software we used
- Arduino IDE
- PyCharm
- Jupyter Notebook
#### Python Libraries we used
- OpenCV-Python
- Mediapipe
- Pyserial
- Numpy
- Python-Math



# Introduction

### What is Computer Vision 
Computer vision is a field of Artificial Intelligence (AI) that enables computers and systems to derive meaningful information from digital images, videos, and other visual inputs and take actions or make recommendations based on that information. If AI enables computers to think, computer vision enables them to see, observe and understand. Computer Vision is indeed is a broad area of study with many specialised tasks and techniques, and also specialisations to target application domains.

### What is Hand Gesture Recognition System
A Hand Gesture Recognition System recognises the Shapes and orientation depending on implementation to task the system into performing some job. Gesture is a form of non-verbal information. As humans through vision perceive human gestures and for computer we need a camera, it is a subject of great interest for computervision researchers such as performing an action based on gestures of the person.

### How does Hand Gesture Recognition work?

<br>

<img align="center" height = "500" src = "./Images/HGR_FlowChart.jpg">

<br>
<br>

The Hand Gesture Recognition Algorithm involves the following steps:

- **Data Obtaining**: It's the process where image is captured from camera or in terms of frames per second via a webcam and a region of interest (ROI) is defined in the frame. The procured image is in RGB format.
- **Data Pre-Processing**: Pre-Processing is carried out in 2 steps - Segmentation and Morphological filtering. Segmentation is performed to change over grey-scale picture into binary picture in ordet to have 2 Areas of Interest in picture. Segmentation itself has 2 processes - 
  - Pixel based or Local methods like Edge Detection and Boundary Detection
  - Region based approach like Region Merging, Region Splitting, and Threshold Method

  Morphological Filtering involves some techniques as mentioned below - 
  - Contours
  - Finding and correcting Convex Hulls
  - Mathematical Operations

  <br>

  <img src = "./Images/HandModel.png">


