# JdeRobot Basic Computer Vision Exercise

This repository contains my solutions for the **Basic Computer Vision** exercise from the [JdeRobot RoboticsAcademy Basic Computer Vision collection](https://jderobot.github.io/RoboticsAcademy/exercises/ComputerVision/basic_computer_vision).

## Set Up RoboticsAcademy

Follow the official [RoboticsAcademy User Guide](https://jderobot.github.io/RoboticsAcademy/user_guide/) for installation instructions.

## Task 1 - Enhanced Grayscale

My solution for Task 1 enhances the basic grayscale task with real-time motion trails and intensity highlights, making it a dynamic and useful tool for robotic vision.

### Overview
The goal of Task 1 is to convert a robot’s camera feed to grayscale and display it using RoboticsAcademy’s GUI. I’ve extended this by:
- **Histogram Equalization**: Boosting contrast for better detail.
- **Motion Trails**: Highlighting movement with fading white trails.
- **Intensity Highlights**: Marking bright spots with a subtle blue tint.

This solution runs in real-time, providing visual cues that could assist a robot in navigation or object tracking.

### Demo Video
Watch my enhanced grayscale solution in action:

**[Enhanced Grayscale: Motion Trails & Highlights](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)**  
*Replace `YOUR_VIDEO_ID` with the actual YouTube video ID after uploading.*

### Solution Details
- **File**: `scripts/grayscale_enhanced.py`
- **Key Features**:
  - **Grayscale Conversion**: Uses `cv2.cvtColor()` to transform BGR to grayscale.
  - **Contrast Enhancement**: Applies `cv2.equalizeHist()` for better visibility.
  - **Motion Detection**: Computes frame differences with `cv2.absdiff()` and thresholds at `15` for sensitivity.
  - **Motion Trails**: Accumulates motion with a decay factor (`alpha = 0.85`), shown where `motion_accumulator > 50`.
  - **Intensity Highlights**: Tints pixels above `240` with `[75, 75, 175]` (soft blue).
  - **Code Robustness**: Skips invalid frames with `if img is None or img.size == 0`.
- **Parameters**:
  - `alpha = 0.85`: Controls trail persistence (lower = shorter trails).
  - `diff threshold = 15`: Motion detection sensitivity.
  - `motion_accumulator > 50`: Trail visibility threshold.
  - `bright_mask > 240`: Brightness threshold for highlights.
  - `[75, 75, 175]`: Subtle blue tint for bright spots.

## Task 2 - ...

## Task 3 - ...