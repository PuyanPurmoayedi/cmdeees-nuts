import subprocess
import time
import tkinter as tk
from tkinter import messagebox
import threading
import random

def fake_hacking_chaos():
    """Launches a massive flurry of CMD windows to create an overwhelming effect."""
    
    commands = [
        "color 0a && title SYSTEM SCANNING && dir /s",
        "color 0a && title DATA LEAK && echo ACCESSING DATABASE... && timeout 2 > nul && dir /s",
        "color 0c && title CRITICAL ERROR && echo SECURITY BREACH DETECTED && timeout 1 > nul && echo IP: 192.168.1.105 && timeout 1 > nul",
        "color 0b && title NETWORK TRACE && echo TRACING ROUTE... && tree",
        "color 0a && title DECRYPTING && echo Key found: 0x8821A && timeout 2 > nul && echo Key found: 0x9912B",
        "color 0c && title WARNING && echo UNAUTHORIZED ACCESS ATTEMPT",
        "color 0a && title FILE_INDEX && dir /s",
        "color 0c && title SYSTEM FAILURE && echo Kernel Panic... && timeout 2",
        "color 0e && title BIOS_OVERRIDE && echo Overriding system protocols...",
    ]

    # --- THE UPGRADE: INCREASED WINDOW COUNT ---
    # We are increasing this from 12 to 25 total windows.
    total_windows = 25 

    print(f"Launching {total_windows} windows...")

    for i in range(total_windows):
        cmd = random.choice(commands)
        
        # Launch the window
        subprocess.Popen(f'start cmd /k "{cmd}"', shell=True)
        
        # --- THE UPGRADE: BURST TIMING ---
        # Instead of a slow steady stream, we use a very small delay 
        # to make them pop up like a "storm".
        # Every 5 windows, we add a tiny "breather" to make it feel like waves.
        if i % 5 == 0 and i != 0:
            time.sleep(0.5) 
        else:
            time.sleep(0.1) # Rapid fire

def show_prank_message():
    """The reveal message."""
    # Increased wait time slightly because 25 windows takes more time to appear
    time.sleep(12) 
    
    root = tk.Tk()
    root.withdraw()
    
    messagebox.showinfo("PRANKED!", "Gotcha! 🤡\n\nEverything is safe. It was just a script running some basic CMD commands.\n\nDon't worry, no files were actually touched!")
    
    root.destroy()

if __name__ == "__main__":
    # Start the chaos in the background
    chaos_thread = threading.Thread(target=fake_hacking_chaos)
    chaos_thread.daemon = True # Ensures the thread stops if you close the main script
    chaos_thread.start()

    # Start the reveal logic
    show_prank_message()
