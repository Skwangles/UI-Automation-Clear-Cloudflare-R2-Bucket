# UI Automation: Clear Cloudflare R2 Bucket

Small Python UI-automation script that repeatedly finds three reference images on screen and clicks them in sequence. The repository appears intended for automating repetitive Cloudflare R2 bucket cleanup actions in a browser UI.

## Current Features

- Continuously loops through a 3-step click sequence:
  1. `first.png` (clicked at leftmost point)
  2. `second.png` (clicked at center)
  3. `third.png` (clicked at center)
- Retries each step until the image is found on screen.
- Uses PyAutoGUI fail-safe (`move mouse to top-left`) and supports `Ctrl+C` exit.
- Uses local PNG templates stored in the repository root.

## Technology Stack

- Python 3
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [Pillow](https://pypi.org/project/Pillow/)
- Optional (commented in `requirements.txt`): OpenCV for confidence-based image matching

## Repository Structure

```text
.
├── image_clicker.py    # Main automation script
├── first.png           # Step 1 template image
├── second.png          # Step 2 template image
├── third.png           # Step 3 template image
├── requirements.txt    # Python dependencies
└── README.md
```

## Prerequisites

- Python 3 installed
- A desktop session where mouse/keyboard control and screenshots are allowed
- The target application/window visible on screen, matching the provided PNG templates

## Installation

Optional virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run from the repository root:

```bash
python image_clicker.py
```

During execution:

- The script keeps cycling forever until stopped.
- Move mouse to the top-left corner to trigger PyAutoGUI fail-safe.
- Or press `Ctrl+C` to exit.

## Configuration

Configuration is currently done directly in `image_clicker.py`:

- Image sequence and click positions are defined in `images` in `main()`.
- Supported click positions in `find_and_click_image(...)`:
  - `center`
  - `leftmost`
  - `rightmost`
  - `topmost`
  - `bottommost`
- Retry interval for missing images: 1 second.
- Delay between images: 0.5 seconds.
- Delay between full cycles: 2 seconds.

## Testing / Validation

No automated test suite is currently included in this repository.  
Recommended validation is manual:

1. Start the target UI.
2. Ensure `first.png`, `second.png`, and `third.png` match visible UI elements.
3. Run `python image_clicker.py`.
4. Confirm clicks happen in expected order and position.
5. Confirm fail-safe (`top-left`) and `Ctrl+C` stop behavior.

## Limitations / Current Status

- Image-based automation is sensitive to UI/theme/scale/resolution changes.
- Uses exact template matching via `pyautogui.locateOnScreen(...)` (no confidence threshold configured).
- Runs indefinitely until manually stopped.
- No command-line flags or external config file at this time.

## License / Attribution

No `LICENSE` file is currently present in this repository.
