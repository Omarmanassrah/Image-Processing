# Image Processing Scripts Collection

This repository contains four Python scripts for various image processing tasks using OpenCV and NumPy.

## Scripts Overview

### 1. OmarManassra(237014).py / OmarManassra(237014) (4).py

- **Purpose**: Image thresholding and morphological operations
- **Features**:
  - Converts image to grayscale
  - Applies binary thresholding
  - Implements custom erosion, dilation, opening, and closing operations
  - Performs multiple iterations of opening and closing
  - Restores original image with white background for non-object areas
- **Techniques**: Thresholding, Morphological operations (erosion, dilation)

### 2. OmarManassra(237014) (3).py

- **Purpose**: Color-based object detection in RoboCup images
- **Features**:
  - Detects green field areas using HSV color space
  - Identifies orange ball using normalized hue and saturation values
  - Creates masks for both field and ball
  - Isolates the ball in a separate image
  - Highlights detected areas in the original image
- **Techniques**: HSV color space analysis, Boolean masking

### 3. OmarManassraImage (2).py

- **Purpose**: Dual-threshold image segmentation
- **Features**:
  - Takes user input for two threshold values
  - Applies band-pass thresholding (pixels between two thresholds are kept)
  - Automatically orders thresholds if entered incorrectly
  - Displays the thresholded image
- **Techniques**: Band-pass thresholding, Interactive input

## Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)

## Usage

1. Clone the repository
2. Install required dependencies
3. Run any script (modify image paths as needed)
4. For OmarManassraImage (2).py, enter threshold values when prompted

## Applications

These scripts demonstrate fundamental image processing techniques useful for:

- Object detection and isolation
- Noise removal
- Color-based segmentation
- Image enhancement
- Computer vision preprocessing

## Note

Some scripts contain hardcoded image paths - you'll need to modify these to point to your own image files or move your images to the specified paths.
