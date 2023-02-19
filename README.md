# Overwatch Application Code Demo - Orion Junkins
February 18, 2023

## Problem: Train Track Midline Detection
Detect railroad tracks in aerial imagery. Read in an image in .jpeg or .png format and output the image with a red line drawn along the track centerline.

## Quickstart
To run this solution, install OpenCV and run main.py.
```
pip install opencv-python
python main.py
```

Input/output filepaths are hard coded into main.py. To experiment with different images, edit the constants at the top of the file.

## Solution Explanation
My solution code performs the following steps:
1. Load the image with OpenCV
2. Pre-process the image to faciliate line detection
  * Convert to Grayscale
  * Apply Gaussian Blur
  * Binarize using Otsu's threshold
3. Detect lines using the Hough transform approach
  * HoughTransformP parameters tuned for best results on provided sample images
4. Take the average of the two highest confidence detections to define a midline
5. Draw the midline on the original image and save the result

## Solution Limitations
This solution works for both of the sample images, however it is very naive. It is worth noting the following limitations:
* No ability to handle multiple tracks. If there are more than one set of tracks in the image, this approach will not handle both, and may fail to handle either.
* Narrowly tuned to the provided sample images. The pre-processing applied is tightly coupled to the given sample images. This approach will likely face issues if the input images are captured from different angles, under different lighting conditions, with different cropping etc.
* No error handling. If detection does not work properly (ie if the number of detections is <2), there is no error handling for graceful failure.
* No sanity checks. The current approach averages the absolute end points of the detected lines. If the lines are different lengths or false positive detections, unreasonable results can occur. Some of these cases could be easily identified and flagged with appropriate checks (ie verify that midline is roughly parallel to both original lines).
