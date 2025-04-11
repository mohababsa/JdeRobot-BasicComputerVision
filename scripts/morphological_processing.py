import GUI
import HAL
import cv2
import numpy as np
import time

# Enter sequential code!
print("Starting Task 2: Advanced Morphological Processing with Tracking...")
kernel = np.ones((5, 5), np.uint8)  # Kernel for morph ops
prev_centroid = None  # Track previous centroid
prev_time = None  # Track time for velocity
centroid_history = []  # Store recent centroids for smoothing

while True:
    # Enter iterative code!
    img = GUI.getImage()
    if img is None or img.size == 0:
        continue

    current_time = time.time()  # For velocity calculation

    # Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Enhance contrast
    equalized_img = cv2.equalizeHist(gray_img)

    # Adaptive thresholding
    binary_img = cv2.adaptiveThreshold(
        equalized_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )

    # Morphological opening
    morphed_img = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel)

    # Find contours
    contours, _ = cv2.findContours(
        morphed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # Convert to BGR for overlays
    output_img = cv2.cvtColor(morphed_img, cv2.COLOR_GRAY2BGR)

    # Process contours if any
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)

        if area > 50:
            # Draw contours
            cv2.drawContours(output_img, contours, -1, (255, 255, 255), 2)

            # Calculate centroid
            M = cv2.moments(largest_contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.drawMarker(
                    output_img, (cX, cY), (0, 255, 0), cv2.MARKER_CROSS, 20, 2
                )

                # Motion direction
                if prev_centroid is not None:
                    dx = cX - prev_centroid[0]
                    if dx > 5:
                        cv2.putText(
                            output_img,
                            "->",
                            (cX + 20, cY),
                            cv2.FONT_HERSHEY_DUPLEX,
                            0.5,
                            (0, 255, 0),
                            1,
                        )
                    elif dx < -5:
                        cv2.putText(
                            output_img,
                            "<-",
                            (cX - 40, cY),
                            cv2.FONT_HERSHEY_DUPLEX,
                            0.5,
                            (0, 255, 0),
                            1,
                        )

                # Velocity estimation
                if prev_centroid is not None and prev_time is not None:
                    dt = current_time - prev_time
                    if dt > 0:
                        distance = np.sqrt(
                            (cX - prev_centroid[0]) ** 2 + (cY - prev_centroid[1]) ** 2
                        )
                        velocity = distance / dt  # Pixels per second
                        cv2.putText(
                            output_img,
                            f"Vel: {int(velocity)} px/s",
                            (10, 60),
                            cv2.FONT_HERSHEY_TRIPLEX,
                            0.3,
                            (255, 255, 0),
                            1,
                        )

                # Update history
                prev_centroid = (cX, cY)
                prev_time = current_time

            # Size and classification
            aspect_ratio = cv2.minAreaRect(largest_contour)[1]  # Width, height
            if len(aspect_ratio) == 2:
                w, h = aspect_ratio
                ar = w / h if w > h else h / w
                label = "Obstacle" if area > 1000 else "Path" if ar > 2 else "Object"
            else:
                label = "Object"

            cv2.putText(
                output_img,
                f"Area: {int(area)} - {label}",
                (10, 30),
                cv2.FONT_HERSHEY_TRIPLEX,
                0.3,
                (255, 255, 0),
                1,
            )

            # ROI bounding box
            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(output_img, (x, y), (x + w, y + h), (0, 255, 255), 2)

    # Display the result
    GUI.showImage(output_img)