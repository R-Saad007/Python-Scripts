import pyautogui
import time
pyautogui.FAILSAFE = False
# Set the time interval (in seconds) for moving the cursor
interval_minutes = 1
interval_seconds = interval_minutes * 60

try:
    while True:
        # Move the cursor to a new position (you can adjust these coordinates)
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)

        # Sleep for the specified interval
        time.sleep(interval_seconds)

except KeyboardInterrupt:
    # Exit the program gracefully if you press Ctrl+C
    pass