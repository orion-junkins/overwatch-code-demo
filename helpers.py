import cv2
import numpy as np
from statistics import mean

def pre_process(img):
  """Pre-process the image to make it easier to detect lines.

  Args:
      img numpy.ndarray: Unprocessed image.

  Returns:
      numpy.ndarray: Processed image
  """
  dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  dst = cv2.GaussianBlur(dst,(5, 5),0)
  _, dst = cv2.threshold(dst, 128, 192, cv2.THRESH_OTSU)
  return dst


def detect_lines(img):
  """Detect lines in the image. Note that these parameters are tuned for the provided sample images and may not function for other input images.

  Args:
      img (numpy.ndarray): Preprocessed image.

  Returns:
      numpy.ndarray: A 3D array of detected lines. Each line is represented by a 2D array of the form [[x1, y1, x2, y2]].
  """
  # Define hyperparameters (tuned for sample images)
  rho = 15 
  theta = np.pi / 360  
  threshold = 500 
  min_line_length = int(min(img.shape)/2)

  # Detect lines
  lines = cv2.HoughLinesP(img, rho, theta, threshold, None, min_line_length)
  return lines


def find_midline(lines):
  """Find the midline of the detected lines. This is done by finding the average x and y coordinates of the start and end points of the two highest confidence lines (the first two in the list).

  Args:
      lines (numpy.ndarray): A 3D array of detected lines. Each line is represented by a 2D array of the form [[x1, y1, x2, y2]].

  Returns:
      numpy.ndarray: Identified midline represented as a 2D array of the form [[x1, y1, x2, y2]].
  """
  (x1s, x2s, y1s, y2s) = [], [], [], []
  for line in lines[:2]:
    for x1, y1, x2, y2 in line:
      x1s.append(x1)
      x2s.append(x2)
      y1s.append(y1)
      y2s.append(y2)

  midline = np.array([[mean(x1s), mean(y1s), mean(x2s), mean(y2s)]])
  return midline


def draw_line(img, midline):
  """Draw the identified midline on the original image. The midline is drawn in red.

  Args:
      img (numpy.ndarray): Original image.
      numpy.ndarray: Identified midline represented as a 2D array of the form [[x1, y1, x2, y2]].

  Returns:
      numpy.ndarray: Image with detected lines and midline drawn on it.
  """
  # Create an image containing only the midline
  line_image = np.copy(img) * 0
  for x1, y1, x2, y2 in midline:
    cv2.line(line_image,(x1,y1),(x2,y2),(0,0,255),15)

  # Combine the original image with the line image
  final_img = cv2.addWeighted(img, 0.8, line_image, 1, 0)
  return final_img
