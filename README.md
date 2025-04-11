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

## Task 2 - Advanced Morphological Processing

My solution for Task 2 enhances morphological processing with real-time object tracking and analysis, tailored for robotics applications. It builds on basic morphological operations to provide actionable insights for navigation and perception.

### Overview
The goal of Task 2 is to apply morphological processing to a robot’s camera feed and display the result using RoboticsAcademy’s GUI. I’ve extended this by:
- **Adaptive Thresholding**: Creates a clean binary image from the grayscale feed.
- **Morphological Opening**: Removes noise while preserving object shapes.
- **Contour Detection**: Outlines objects for shape recognition.
- **Centroid Tracking**: Marks the center of the largest object with a green cross.
- **Size Estimation**: Displays the object’s area in pixels.
- **Motion Direction**: Indicates left/right movement with green arrows.
- **Velocity Estimation**: Calculates the object’s speed in pixels per second.
- **Region of Interest (ROI)**: Highlights the largest object with a yellow bounding box.

This solution runs in real-time, offering a detailed view that could guide a robot in obstacle avoidance, path following, or target tracking.

### Demo Video
Watch my advanced morphological processing solution in action:

**[Morphological Precision: Tracking Everything](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)**  
*Replace `YOUR_VIDEO_ID` with the actual YouTube video ID after uploading.*

### Solution Details
- **File**: `scripts/morphological_processing.py`
- **Key Features**:
  - **Grayscale Conversion**: Uses `cv2.cvtColor()` to transform BGR to grayscale.
  - **Contrast Enhancement**: Applies `cv2.equalizeHist()` for better visibility.
  - **Adaptive Thresholding**: Converts to binary with `cv2.adaptiveThreshold()` (Gaussian, block size 11, constant 2).
  - **Morphological Opening**: Uses `cv2.morphologyEx()` with a 5x5 kernel to clean noise.
  - **Contour Detection**: Finds external contours with `cv2.findContours()` and draws them in white.
  - **Centroid Tracking**: Computes the center of the largest contour using `cv2.moments()`, marked with a green cross.
  - **Size & Classification**: Estimates area with `cv2.contourArea()` and classifies as "Obstacle" (area > 1000), "Path" (aspect ratio > 2), or "Object".
  - **Motion Direction**: Detects left/right motion of the centroid (threshold ±5 pixels), shown with green arrows.
  - **Velocity Estimation**: Calculates speed (pixels/second) using centroid displacement and time delta.
  - **ROI**: Draws a yellow bounding box with `cv2.boundingRect()` around the largest object.
  - **Code Robustness**: Skips invalid frames with `if img is None or img.size == 0`.
- **Parameters**:
  - `kernel = np.ones((5, 5))`: 5x5 kernel for morphological operations.
  - `adaptiveThreshold(..., 11, 2)`: Block size 11, constant 2 for thresholding.
  - `area > 50`: Minimum contour area to filter noise.
  - `dx > 5 / < -5`: Motion direction threshold.
  - `font = cv2.FONT_HERSHEY_TRIPLEX, size = 0.3`: Professional font, smaller size for text overlays.
  - `colors`: White (contours), Green (centroid/arrows), Cyan (text), Yellow (ROI).

## Task 3 - ...
