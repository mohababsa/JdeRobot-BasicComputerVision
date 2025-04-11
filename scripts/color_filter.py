import GUI
import HAL
import cv2
import numpy as np
import time

# Enter sequential code!
print("Starting Task 3: Multi-Color Filter with Motion Tracking...")
# Red HSV ranges
lower_red1 = np.array([0, 140, 90])
upper_red1 = np.array([8, 255, 255])
lower_red2 = np.array([168, 140, 90])
upper_red2 = np.array([180, 255, 255])
# Blue HSV range
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])
kernel = np.ones((5, 5), np.uint8)
small_kernel = np.ones((3, 3), np.uint8)
prev_red_centroid = None  # Track red object motion
prev_blue_centroid = None
prev_time = None

while True:
    # Enter iterative code!
    img = GUI.getImage()
    if img is None or img.size == 0:
        continue

    current_time = time.time()
    blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
    hsv_img = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2HSV)

    # Red mask
    mask_red1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask_red1, mask_red2)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, small_kernel, iterations=2)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel, iterations=1)
    red_mask = cv2.dilate(red_mask, kernel, iterations=1)

    # Blue mask
    blue_mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
    blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, small_kernel, iterations=2)
    blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_CLOSE, kernel, iterations=1)
    blue_mask = cv2.dilate(blue_mask, kernel, iterations=1)

    # Contours
    red_contours, _ = cv2.findContours(
        red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    blue_contours, _ = cv2.findContours(
        blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    output_img = img.copy()

    # Process red contours
    if red_contours:
        largest_red = max(red_contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_red)
        if area > 150:
            x, y, w, h = cv2.boundingRect(largest_red)
            M = cv2.moments(largest_red)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                roi = red_mask[
                    int(max(0, cY - h / 2)) : int(min(img.shape[0], cY + h / 2)),
                    int(max(0, cX - w / 2)) : int(min(img.shape[1], cX + w / 2)),
                ]
                red_ratio = np.sum(roi) / (255 * roi.size) if roi.size > 0 else 0
                if red_ratio > 0.3:
                    cv2.drawContours(output_img, [largest_red], -1, (255, 255, 255), 2)
                    cv2.drawMarker(
                        output_img, (cX, cY), (0, 255, 0), cv2.MARKER_CROSS, 15, 2
                    )
                    cv2.rectangle(
                        output_img, (x, y), (x + w, y + h), (0, 255, 255), 2
                    )  # Yellow box
                    cv2.putText(
                        output_img,
                        f"R Area: {int(area)}",
                        (cX + 10, cY - 10),
                        cv2.FONT_HERSHEY_TRIPLEX,
                        0.3,
                        (255, 255, 0),
                        1,
                    )

                    # Motion tracking for red
                    if prev_red_centroid and prev_time:
                        dx = cX - prev_red_centroid[0]
                        dt = current_time - prev_time
                        if dt > 0:
                            vel = np.sqrt(dx**2 + (cY - prev_red_centroid[1]) ** 2) / dt
                            cv2.putText(
                                output_img,
                                f"Vel: {int(vel)} px/s",
                                (cX + 10, cY + 10),
                                cv2.FONT_HERSHEY_TRIPLEX,
                                0.3,
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
                    prev_red_centroid = (cX, cY)

    # Process blue contours
    if blue_contours:
        largest_blue = max(blue_contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_blue)
        if area > 150:
            x, y, w, h = cv2.boundingRect(largest_blue)
            M = cv2.moments(largest_blue)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                roi = blue_mask[
                    int(max(0, cY - h / 2)) : int(min(img.shape[0], cY + h / 2)),
                    int(max(0, cX - w / 2)) : int(min(img.shape[1], cX + w / 2)),
                ]
                blue_ratio = np.sum(roi) / (255 * roi.size) if roi.size > 0 else 0
                if blue_ratio > 0.3:
                    cv2.drawContours(output_img, [largest_blue], -1, (255, 255, 255), 2)
                    cv2.drawMarker(
                        output_img, (cX, cY), (0, 255, 0), cv2.MARKER_CROSS, 15, 2
                    )
                    cv2.rectangle(
                        output_img, (x, y), (x + w, y + h), (255, 0, 0), 2
                    )  # Blue box
                    cv2.putText(
                        output_img,
                        f"B Area: {int(area)}",
                        (cX + 10, cY - 10),
                        cv2.FONT_HERSHEY_TRIPLEX,
                        0.3,
                        (255, 255, 0),
                        1,
                    )

                    # Motion tracking for blue
                    if prev_blue_centroid and prev_time:
                        dx = cX - prev_blue_centroid[0]
                        dt = current_time - prev_time
                        if dt > 0:
                            vel = (
                                np.sqrt(dx**2 + (cY - prev_blue_centroid[1]) ** 2) / dt
                            )
                            cv2.putText(
                                output_img,
                                f"Vel: {int(vel)} px/s",
                                (cX + 10, cY + 10),
                                cv2.FONT_HERSHEY_TRIPLEX,
                                0.3,
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
                    prev_blue_centroid = (cX, cY)

    prev_time = current_time
    GUI.showImage(output_img)
