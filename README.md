# Gesture Based Screen Brightness Control

A lightweight Python script that adjusts your computer's screen brightness in real-time using hand gestures captured by your webcam.

This project uses OpenCV for image processing, `cvzone` (powered by MediaPipe) for fast and accurate hand tracking, and `screen_brightness_control` to interface directly with your system's display settings.

## Features

- **Real-Time Tracking:** Captures live video feed from the default webcam to monitor hand movements continuously.
- **Gesture Recognition:** Calculates the distance between your thumb and index finger to determine the desired brightness intensity.
- **Dynamic Adjustment:** Automatically maps the physical distance between your fingers to a 0-100% scale and instantly updates the system screen brightness.
- **Visual Feedback:** Renders a dynamic, graphical brightness bar and a live percentage readout directly on the video feed window.
- **Graceful Exit:** Safely closes the application, releases camera resources, and destroys UI windows with a simple keystroke.

## Prerequisites

Before running the script, ensure Python is installed on your system. You also need the following libraries:

### Required Libraries

- `opencv-python` (`cv2`)
- `numpy`
- `screen-brightness-control`
- `cvzone`
- `mediapipe` (backend required by `cvzone`'s `HandTrackingModule`)

## Installation

1. Clone this repository:
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
   cd your-repo-name
   ```

2. Install dependencies:
   ```bash
   pip install opencv-python numpy screen-brightness-control cvzone mediapipe
   ```

## Usage

Run the script from your terminal:

```bash
python main.py
```

> Replace `main.py` with the actual name of your Python file.

A window named **Gesture Brightness Control** will open displaying your webcam feed. Pinch your thumb and index finger together to lower the brightness, and spread them apart to increase it. 

To exit the application, press **`q`** while the video window is active. The script will safely release the webcam and close all OpenCV windows.

## How It Works

1. **Initialization:** Starts the webcam feed using `cv.VideoCapture(0)` and initializes the `HandDetector`.
2. **Frame Extraction:** Reads the video feed frame by frame in a continuous loop.
3. **Hand Localization:** `hd.findHands` scans the frame for hands and extracts the 21 anatomical landmark coordinates (`lmList`).
4. **Distance Measurement:** Identifies the tips of the thumb (landmark `4`) and index finger (landmark `8`), then calculates the distance between them using `hd.findDistance`.
5. **Mapping & Control:** - Uses `numpy.interp` to translate the raw pixel distance (roughly 15 to 230 pixels) into a percentage (0 to 100).
   - Passes this calculated percentage to `scrbr.set_brightness()` to change the actual monitor brightness.
6. **UI Rendering & Exit:** - Uses `numpy.interp` again to map the brightness percentage to coordinates for drawing a dynamic visual rectangle (brightness bar) using `cv.rectangle`.
   - Displays the modified frame continuously and checks for the `q` key press to break the loop, release `cap`, and destroy OpenCV windows.
