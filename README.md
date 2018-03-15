# The2018Thing

Our robot code for the FIRST Robotics *FIRST Power Up* competition.

![alt-text](img/botpic.png)

![Scrutinizer Build](https://img.shields.io/badge/build-passing-green.svg?style=flat-square) ![license](https://img.shields.io/badge/License-GNU%20GPL%20v3.0-blue.svg?style=flat-square)

## Getting Started
### Prequisites
Our repo requires on the following Python libraries:
* [RobotPy](https://robotpy.readthedocs.io)
* [OpenCV](https://opencv.org/)
* [NumPy](www.numpy.org)

### Installation
#### Linux/MacOS

> run `pip3 install -r requirements.txt`

> May require `sudo`, but `--user` can be passed in if need be.


#### Windows
> `pip3 install -r requirements.txt`

#### Test Modules
Run the following commands in your local Python terminal (Run `python3` or `python` to access it):
```
    >>> import cv2
    >>> import wpilib
    >>> import numpy
```
These should return no errors. If they did, review previous instructions.

### Test Code
To test this robot project, simply pass in the following command into your command prompt or Windows.
```
$ python3 path/to/robot.py sim
```
or, if you use Windows, 
```
$ python path\to\robot.py sim
```
This should bring up a separate window to display a test bench on. 

### Deploy Code

To deploy this code, you will need to make sure of the following:
* Your code tests correctly and will not break the robot. 
* Your computer is connected to the Robot's WiFi Network. (To configure this, see [here](http://wpilib.screenstepslive.com/s/currentCS/m/troubleshooting/l/442032-programming-radios-for-fms-offseason))

If you fill these requirements, run the following code:
> For Mac OSX/Linux:
> ```
> python3 path/to/robot.py deploy
> ```

> For Windows:
> ```
> python path\to\robot.py deploy
> ```
In addition to this, you can run some of the following commands:
* `-n` or `--no-version-check` to ignore the version of RobotPy that is on the robot. 
* `--skip-tests` to skip the tests on the robot (Not recommended)
To see the rest of the commands available to you, use the command `python3 path/to/robot.py deploy -h`