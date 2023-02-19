import cv2  
from helpers import *

# Change filepaths as needed to test on different images
INPUT_FILEPATH = 'sample_2.jpg'
OUTPUT_FILEPATH = 'output_2.png'

# Load the image
img = cv2.imread(INPUT_FILEPATH,1) 

# Process the image (grayscale, Gaussian blur and Otsu threshold binarization)
processed_image = pre_process(img)

# Detect the lines in the image (Hough transform)
raw_lines = detect_lines(processed_image)

# Find the midline of the detected lines (average of start and end points of the two highest confidence detections)
midline = find_midline(raw_lines)

# Draw the detected lines and midline on the original image
final_image = draw_line(img, midline)

# Save the final image
cv2.imwrite(OUTPUT_FILEPATH, final_image)
