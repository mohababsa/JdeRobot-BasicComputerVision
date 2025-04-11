# JdeRobot Basic Computer Vision Exercise

This repository contains my solutions for the **Basic Computer Vision** exercise from the [JdeRobot RoboticsAcademy Basic Computer Vision collection](https://jderobot.github.io/RoboticsAcademy/exercises/ComputerVision/basic_computer_vision).

## Set Up RoboticsAcademy

Follow the official [RoboticsAcademy User Guide](https://jderobot.github.io/RoboticsAcademy/user_guide/) for installation instructions.

## Outlines
Below is a table of contents for quick navigation to each task in this repository:

- [Task 1 - Enhanced Grayscale](#task-1---enhanced-grayscale)
- [Task 2 - Advanced Morphological Processing](#task-2---advanced-morphological-processing)
- [Task 3 - Multi-Color Filter with Motion Tracking](#task-3---multi-color-filter-with-motion-tracking)
- [Task 4 - Deep Edge Filters with Fine Details](#task-4---deep-edge-filters-with-fine-details)

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

## Task 4 - Deep Edge Filters with Fine Details

My solution for Task 4 takes edge detection to the next level, extracting fine details and providing rich analysis for robotic applications. It’s built for real-time precision and dynamic scene understanding.

### Overview
The goal of Task 4 is to apply edge filters to a robot’s camera feed and display the result using RoboticsAcademy’s GUI. I’ve enhanced this by:
- **Multi-Scale Edge Detection**: Combines fine and coarse Canny edges for both small details and large boundaries.
- **Edge Enhancement**: Sharpens the image to reveal faint edges.
- **Dynamic Thresholding**: Adapts Canny thresholds to scene brightness.
- **Contour Analysis**: Extracts area, perimeter, strength, and convexity for all edges.
- **Motion Tracking**: Tracks velocity and direction of the largest edge-based object.
- **Non-Overlapping Labels**: Smartly positions text to handle numerous small details.

This solution delivers a detailed edge map with actionable data, ideal for navigation, obstacle detection, or fine-grained feature extraction in robotics.

### Demo Video
Watch my deep edge filter solution in action:

**[Deep Edges: Precision in Motion](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)**  
*Replace `YOUR_VIDEO_ID` with the actual YouTube video ID after uploading.*

### Solution Details
- **File**: `scripts/edge_filters.py`
- **Key Features**:
  - **Grayscale Conversion**: Uses `cv2.cvtColor()` to transform BGR to grayscale.
  - **Sharpening**: Applies a 3x3 kernel (`[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]`) to boost faint edges.
  - **Noise Reduction**: Uses `cv2.GaussianBlur()` for a smoother edge base.
  - **Multi-Scale Canny**: Combines fine (`low=mean*0.3, high=mean*1.0`) and coarse (`low=mean*0.6, high=mean*1.8`) edges with `cv2.bitwise_or()`.
  - **Edge Overlay**: Blends edges (60%) with the original image (40%) using `cv2.addWeighted()`.
  - **Contour Detection**: Finds all edge contours with `cv2.findContours()`, drawn in white.
  - **Detailed Analysis**:
    - **Area**: `cv2.contourArea()` for size.
    - **Perimeter**: `cv2.arcLength()` for edge length.
    - **Strength**: Perimeter/area ratio, labeled “Strong” (>0.5) or “Weak”.
    - **Convexity**: `cv2.convexHull()` ratio, labeled “Convex” (>0.9) or “Concave”.
  - **Centroid Tracking**: Marks centers with green crosses via `cv2.moments()`.
  - **Bounding Boxes**: Draws yellow boxes with `cv2.boundingRect()`.
  - **Motion Tracking**: Calculates velocity (pixels/second) and direction (arrows) for the largest contour.
  - **Smart Text**: Full details for the largest contour, area-only for smaller ones with vertical offset to avoid overlap.
  - **Code Robustness**: Skips invalid frames with `if img is None or img.size == 0`.
- **Parameters**:
  - `area > 50`: Minimum contour area for small details.
  - `strength > 0.5`: Threshold for “Strong” edges.
  - `convexity > 0.9`: Threshold for “Convex” shapes.
  - `dx > 5 / < -5`: Motion direction threshold.
  - `font = cv2.FONT_HERSHEY_TRIPLEX, size = 0.25`: Smaller, professional text.
  - **Colors**: White (contours), Green (centroids/arrows), Cyan (text), Yellow (boxes).

graph TD
    subgraph Browser
        A[User Browser] -->|HTTP: 127.0.0.1:7164| B[Exercise Page]
        B --> C[Code Editor]
        B --> D[Visualization Panels]
        C -->|WebSocket: 127.0.0.1:8765| E[Django Manager]
        D -->|WebRTC: 127.0.0.1:1108, 6080| F[WebRTC Stream]
    end

    subgraph RoboticsAcademy Container
        E[Django Manager] -->|Port 8000| G[Web Server]
        E -->|WebSocket Port 8765| H[WebSocket Server]
        E -->|Sends Code| I[RoboticsBackend Container]
        J[Gazebo Simulator] -->|ROS2 Topics| K[ROS2 Nodes]
        J -->|Camera Feed| L[WebRTC Server]
        L -->|Ports 1108, 6080| F
        J -->|Port 2303| M[Gazebo Internal]
        K -->|ROS2 Bridge: Port 7163| N[Exercise ROS2 Topics]
    end

    subgraph RoboticsBackend Container
        I --> O[User Code: exercise.py]
        O -->|Imports| P[HAL.py]
        O -->|Imports| Q[GUI.py]
        P -->|ROS2 Topics| K
        Q -->|ROS2 Topics| K
        Q -->|Visualization Data| L
    end

    subgraph Robotics-Database Container
        R[PostgreSQL] -->|Port 5432| S[Database]
        E -->|Saves Code| S
    end

    %% Connections between subgraphs
    A -->|Accesses| E
    F -->|Streams To| D
    I -->|Executes| K
    S -->|Persistent Storage| E
