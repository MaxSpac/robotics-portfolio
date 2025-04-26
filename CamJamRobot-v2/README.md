# CamJam Robot with Obstacle Avoidance (v2)

## Overview
This project demonstrates an autonomous robot built using the CamJam EduKit 3, capable of detecting and avoiding obstacles with two ultrasonic sensors. Controlled via Python scripts on a Raspberry Pi, the robot showcases a modular, object-oriented design with a focus on test-driven development (TDD). This version (`CamJamRobot_v2`) separates hardware access from control logic, improving maintainability, testability, and reusability for future robot projects.

The project reflects my growing expertise in robotics, Python programming, and software engineering principles like OOD and TDD.

## Technologies
### Hardware
- Raspberry Pi 4 Model B
- 2x HC-SR04 Ultrasonic Sensors (high and low for obstacle detection)
- CamJam EduKit3 Motors
- CamJam EduKit3 Motor Control
- LEDs (red, white, yellow left, yellow right) for visual feedback

### Software
- Python 3
- `gpiozero` for hardware control (LEDs, motors, sensors)
- Threading for concurrent LED blinking and motor control
- `unittest` and `unittest.mock` for TDD

## Objective
The robot autonomously navigates by detecting obstacles with two ultrasonic sensors and adjusting its path using a state-based control logic. It uses LEDs for visual feedback (e.g., red for obstacle detection, blinking yellow for turning) and supports modular design to enable reuse with other robots.

## Project Structure
The `CamJamRobot-v2` version introduces a modular architecture:
- `hardware.py`: Contains the `HardwareInterface` class, encapsulating access to LEDs, motors, and sensors. This isolates hardware-specific details (e.g., GPIO pins) for easy adaptation to other robots.
- `robot_controller.py`: Implements the `RobotController` class, handling navigation logic, obstacle avoidance, and motor control. It uses a configuration dictionary for customizable parameters (e.g., motor speeds, obstacle threshold).
- The separation enables object-oriented design, simplifies unit testing with mocks, and supports future extensions (e.g., new sensors or control algorithms).

## Progress
This project builds on my initial robotics experience, incorporating advanced software engineering practices. Key milestones include:

- **Setup** (Completed: 2025-04-19): Configured Raspberry Pi via SSH and integrated two HC-SR04 sensors.
- **Basic Control** (Completed: 2025-04-20): Implemented motor control and sensor reading with `gpiozero`.
- **Obstacle Avoidance**: (Completed: 2025-04-20) Developed state machine for autonomous navigation .
- **Threading** (Completed: 2025-04-21): Added concurrent LED blinking during turns using Python threading.
- **Modular Architecture** (Expected Completion: 2025-04-27): Refactored code into `HardwareInterface` and `RobotController` classes, enabling OOD and TDD.


### Future Goals
- Port the project to ROS for simulation in Gazebo and integration with advanced sensors (e.g., LIDAR).
- Enable smartphone connectivity to trigger scripts or control the robot remotely.
- Expand unit tests to cover more edge cases and improve code coverage.
- Integrate additional sensors (e.g., line sensors) for enhanced navigation.

## Status
- **Current**: Fully functional obstacle avoidance with two sensors, LED feedback, and threaded LED blinking. Unit tests in work.
- **Next Steps**: 
   - Refracture code modular, testable, and ready for extensions.
   - Write unit tests for `RobotController`, explore ROS integration, and test smartphone connectivity.

## Demo
Video and screenshots of the robot in action will be added upon completion of the next milestones. Currently, the robot successfully navigates a test environment, avoiding obstacles and providing visual feedback via LEDs.

## Getting Started
1. **Hardware Setup**:
   - Connect the CamJam EduKit 3 motors, the motor control, two HC-SR04 sensors (in front direction, one at a high position, one at a relative lower position) and LEDs to the Raspberry Pi as per the pin configuration in `hardware.py`.
   - Ensure the Raspberry Pi is powered and accessible via SSH.

2. **Software Setup**:
   - Clone the repository: `git clone https://github.com/SpaceDevMax/robotics-portfolio.git` to the Pi
   - Navigate to `CamJamRobot_v2`: `cd CamJamRobot_v2`
   - Install dependencies: `pip install -r requirements.txt`

3. **Running the Robot**:
   - Run the main script: `python robot_controller.py`
   - The robot will start navigating, detecting obstacles, and controlling LEDs.

4. **Running Tests**:
   - Execute unit tests: `python -m unittest discover`
   - Tests use mocks to simulate hardware, ensuring robust validation of control logic.

## Contact
For questions or feedback, feel free to reach out via max@blackhead-metaverse.com.