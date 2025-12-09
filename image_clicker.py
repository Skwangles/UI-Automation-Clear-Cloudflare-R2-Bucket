#!/usr/bin/env python3
"""
PyAutoGUI script to find and click on three PNG images in sequence.
Looks for first.png, second.png, and third.png, clicks on them, then loops.
"""

import pyautogui
import time
import sys
from pathlib import Path

# Configure PyAutoGUI settings
pyautogui.FAILSAFE = True  # Move mouse to top-left corner to stop
pyautogui.PAUSE = 0.5  # Small pause between actions

def find_and_click_image(image_path, click_position='center'):
    """
    Find an image on screen and click on it.
    
    Args:
        image_path (str): Path to the image file
        click_position (str): Where to click - 'center', 'leftmost', 'rightmost', 'topmost', 'bottommost'
    
    Returns:
        bool: True if image found and clicked, False otherwise
    """
    try:
        # Check if image file exists
        if not Path(image_path).exists():
            print(f"Error: Image file '{image_path}' not found!")
            return False
        
        # Find the image on screen
        print(f"Looking for {image_path}...")
        location = pyautogui.locateOnScreen(image_path)
        
        if location is None:
            print(f"Could not find {image_path} on screen")
            return False
        
        # Determine click position
        if click_position == 'center':
            click_x, click_y = pyautogui.center(location)
        elif click_position == 'leftmost':
            click_x, click_y = location.left, location.top + location.height // 2
        elif click_position == 'rightmost':
            click_x, click_y = location.left + location.width, location.top + location.height // 2
        elif click_position == 'topmost':
            click_x, click_y = location.left + location.width // 2, location.top
        elif click_position == 'bottommost':
            click_x, click_y = location.left + location.width // 2, location.top + location.height
        else:
            click_x, click_y = pyautogui.center(location)
        
        # Click on the determined position
        print(f"Clicking {image_path} at ({click_x}, {click_y}) - {click_position}")
        pyautogui.click(click_x, click_y)
        return True
        
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return False

def main():
    """Main function to run the image clicking sequence."""
    print("Starting image clicker script...")
    print("Move mouse to top-left corner to stop the script")
    print("Press Ctrl+C to exit")
    
    # Get the directory where the script is located
    script_dir = Path(__file__).parent
    
    # Define image paths relative to script directory
    images = [
        ("first.png", "leftmost"),
        ("second.png", "center"),
        ("third.png", "center")
    ]
    
    try:
        while True:
            print("\n--- Starting new cycle ---")
            
            # Process each image in sequence - keep looking until found
            for image_name, click_pos in images:
                image_path = script_dir / image_name
                found = False
                
                # Keep looking for this image until found
                while not found:
                    if find_and_click_image(str(image_path), click_pos):
                        print(f"Successfully clicked {image_name}")
                        found = True
                    else:
                        print(f"Still looking for {image_name}...")
                        time.sleep(1)  # Wait 1 second before trying again
                
                # Small pause between images
                time.sleep(0.5)
            
            # Wait 2 seconds before next cycle
            print("Waiting 2 seconds before next cycle...")
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nScript stopped by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 