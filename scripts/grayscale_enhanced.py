import GUI
import HAL
import cv2
import numpy as np

# Enter sequential code!
prev_gray = None
motion_accumulator = None
alpha = 0.85  # Decay factor for trails
print("Starting Enhanced Grayscale: Motion Trails & Intensity Highlights...")

while True:
    # Enter iterative code!
    img = GUI.getImage()
    if img is None or img.size == 0:
        continue

    # Convert to grayscale and enhance contrast
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equalized_img = cv2.equalizeHist(gray_img)

    # Initialize on first frame
    if prev_gray is None:
        prev_gray = equalized_img.copy()
        motion_accumulator = np.zeros_like(equalized_img, dtype=np.float32)
        continue

    # Detect motion
    diff = cv2.absdiff(equalized_img, prev_gray)
    _, motion_mask = cv2.threshold(diff, 15, 255, cv2.THRESH_BINARY)

    # Update motion accumulator (trails)
    motion_accumulator = alpha * motion_accumulator + (1 - alpha) * motion_mask.astype(
        np.float32
    )
    motion_accumulator = np.clip(motion_accumulator, 0, 255)

    # Base output: equalized grayscale
    output_img = equalized_img.copy()

    # Highlight motion trails (white)
    output_img[motion_accumulator > 50] = 255

    # Convert to BGR for highlights
    output_img_bgr = cv2.cvtColor(output_img, cv2.COLOR_GRAY2BGR)

    # Highlight high-intensity areas with a subtler blue tint
    bright_mask = equalized_img > 240  # Raised threshold for brighter spots only
    output_img_bgr[bright_mask] = [75, 75, 175]  # Softer blue tint

    # Update previous frame
    prev_gray = equalized_img.copy()

    # Display the result
    GUI.showImage(output_img_bgr)
