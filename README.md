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

## Task 3 - Multi-Color Filter with Motion Tracking

My solution for Task 3 enhances color filtering to detect and track red and blue objects in real-time, optimized for robotics applications. It combines precise color isolation with motion analysis for dynamic scene understanding.

### Overview
The goal of Task 3 is to filter a robot’s camera feed for a specific color and display it using RoboticsAcademy’s GUI. I’ve extended this by:
- **Multi-Color Detection**: Simultaneously tracks red and blue objects with distinct overlays.
- **Precise HSV Filtering**: Uses tight HSV ranges for accurate color isolation.
- **Morphological Cleaning**: Removes noise and refines object shapes.
- **Contour Tracking**: Outlines and boxes the largest red and blue objects.
- **Centroid Marking**: Highlights object centers for targeting.
- **Motion Analysis**: Estimates velocity and direction of moving objects.
- **Area Display**: Shows object sizes for scale estimation.

This solution runs in real-time, enabling a robot to detect, track, and respond to colored targets or obstacles efficiently.

### Demo Video
Watch my multi-color filter with motion tracking in action:

**[Multi-Color Tracking: Red & Blue in Motion](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)**  
*Replace `YOUR_VIDEO_ID` with the actual YouTube video ID after uploading.*

### Solution Details
- **File**: `scripts/color_filter.py`
- **Key Features**:
  - **Color Conversion**: Uses `cv2.cvtColor()` to transform BGR to HSV for robust filtering.
  - **Noise Reduction**: Applies `cv2.GaussianBlur()` to smooth the input image.
  - **Multi-Color Masks**: 
    - Red: Combines two HSV ranges with `cv2.inRange()` and `cv2.bitwise_or()`.
    - Blue: Single HSV range for detection.
  - **Morphological Processing**: Uses `cv2.morphologyEx()` (opening and closing) and `cv2.dilate()` to clean and refine masks.
  - **Contour Detection**: Finds largest contours for red and blue with `cv2.findContours()`, drawn in white.
  - **Centroid Tracking**: Computes centers with `cv2.moments()`, marked with green crosses.
  - **Bounding Boxes**: Draws yellow boxes for red and blue boxes for blue using `cv2.boundingRect()`.
  - **Motion Tracking**: Calculates velocity (pixels/second) and direction (left/right arrows) using centroid history and time deltas.
  - **Area Display**: Shows object areas with a professional font near centroids.
  - **Code Robustness**: Skips invalid frames with `if img is None or img.size == 0`.
- **Parameters**:
  - **Red HSV**: `[0, 140, 90]` to `[8, 255, 255]` and `[168, 140, 90]` to `[180, 255, 255]`.
  - **Blue HSV**: `[100, 150, 50]` to `[140, 255, 255]`.
  - `kernel = np.ones((5, 5))`: For closing and dilation.
  - `small_kernel = np.ones((3, 3))`: For opening.
  - `area > 150`: Minimum contour area for detection.
  - `red_ratio/blue_ratio > 0.3`: Confidence threshold for color presence.
  - `dx > 5 / < -5`: Motion direction threshold.
  - `font = cv2.FONT_HERSHEY_TRIPLEX, size = 0.3`: Professional text for labels.
  - **Colors**: White (contours), Green (centroids/arrows), Cyan (text), Yellow (red boxes), Blue (blue boxes).
