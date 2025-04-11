import GUI
import HAL
import cv2
import numpy as np
import time

# Enter sequential code!
print("Starting Task 4: Deep Edge Filters with Non-Overlapping Details...")
prev_centroid = None
prev_time = None

while True:
    # Enter iterative code!
    img = GUI.getImage()
    if img is None or img.size == 0:
        continue

    current_time = time.time()

    # Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Sharpen image
    sharpened_img = cv2.filter2D(
        gray_img, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    )

    # Reduce noise
    blurred_img = cv2.GaussianBlur(sharpened_img, (5, 5), 0)

    # Dynamic multi-scale Canny
    mean_brightness = np.mean(blurred_img)
    low_fine = max(30, int(mean_brightness * 0.3))
    high_fine = max(100, int(mean_brightness * 1.0))
    low_coarse = max(80, int(mean_brightness * 0.6))
    high_coarse = max(200, int(mean_brightness * 1.8))

    edges_fine = cv2.Canny(blurred_img, low_fine, high_fine)
    edges_coarse = cv2.Canny(blurred_img, low_coarse, high_coarse)
    edges = cv2.bitwise_or(edges_fine, edges_coarse)

    # Overlay edges
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    output_img = cv2.addWeighted(img, 0.4, edges_bgr, 0.6, 0)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Process contours
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        text_offset = 0  # Track vertical offset for text

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 50:  # Keep small details
                perimeter = cv2.arcLength(contour, True)
                strength = perimeter / area if area > 0 else 0
                label = "Strong" if strength > 0.5 else "Weak"

                hull = cv2.convexHull(contour)
                hull_area = cv2.contourArea(hull)
                convexity = area / hull_area if hull_area > 0 else 1.0
                convexity_label = "Convex" if convexity > 0.9 else "Concave"

                # Draw contours and boxes
                cv2.drawContours(output_img, [contour], -1, (255, 255, 255), 1)
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(output_img, (x, y), (x + w, y + h), (0, 255, 255), 1)

                # Centroid
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    cv2.drawMarker(
                        output_img, (cX, cY), (0, 255, 0), cv2.MARKER_CROSS, 10, 1
                    )

                # Text placement
                if contour is largest_contour:
                    # Full details for largest contour
                    text = (
                        f"A: {int(area)} P: {int(perimeter)} {label} {convexity_label}"
                    )
                    cv2.putText(
                        output_img,
                        text,
                        (cX + 10, cY - 10),
                        cv2.FONT_HERSHEY_TRIPLEX,
                        0.25,
                        (255, 255, 0),
                        1,
                    )

                    # Motion tracking
                    if prev_centroid and prev_time:
                        dx = cX - prev_centroid[0]
                        dt = current_time - prev_time
                        if dt > 0:
                            vel = np.sqrt(dx**2 + (cY - prev_centroid[1]) ** 2) / dt
                            cv2.putText(
                                output_img,
                                f"Vel: {int(vel)} px/s",
                                (cX + 10, cY + 10),
                                cv2.FONT_HERSHEY_TRIPLEX,
                                0.25,
                                (255, 255, 0),
                                1,
                            )
                            if dx > 5:
                                cv2.putText(
                                    output_img,
                                    "->",
                                    (cX + 20, cY),
                                    cv2.FONT_HERSHEY_TRIPLEX,
                                    0.5,
                                    (0, 255, 0),
                                    1,
                                )
                            elif dx < -5:
                                cv2.putText(
                                    output_img,
                                    "<-",
                                    (cX - 40, cY),
                                    cv2.FONT_HERSHEY_TRIPLEX,
                                    0.5,
                                    (0, 255, 0),
                                    1,
                                )
                        prev_centroid = (cX, cY)
                        prev_time = current_time
                else:
                    # Minimal text for smaller contours, offset to avoid overlap
                    text = f"A: {int(area)}"
                    cv2.putText(
                        output_img,
                        text,
                        (x, y - 10 - text_offset),
                        cv2.FONT_HERSHEY_TRIPLEX,
                        0.25,
                        (255, 255, 0),
                        1,
                    )
                    text_offset += 15  # Increment offset for next small contour

    if contours and not prev_centroid:
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            prev_centroid = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            prev_time = current_time

    # Display the result
    GUI.showImage(output_img)
