import tkinter as tk
import random
import time
import os
import win32com.client  # We need this to create the shortcut
from PIL import Image, ImageTk

# Suggestions
hardware_suggestions = [
    "In your bios settings, enable XMP and increase your frequency to 6000 MHZ",
    "Manually set DRAM voltage to 1.35V for stable overclocking.",
    "Boost GPU core clock by +150 MHz using MSI Afterburner.",
    "Set up a custom fan curve to keep GPU temperature below 70°C."
]

software_suggestions = [
    "Disable unnecessary startup programs in Task Manager (You have programs with startup enabled).",
    "Install MSI Afterburner for real-time GPU monitoring and tweaks.",
    "Use Process Lasso to optimize CPU usage and improve responsiveness.",
    "Clear Browser Cache"
]

settings_suggestions = [
    "Set the power plan to High Performance in Control Panel > Power Options.",
    "Turn Off Windows Defender’s Real-time Protection temporarily.",
    "Disable Large Send Offload in Network Settings to reduce latency.",
    "Disable Windows Auto-Tuning with: netsh interface tcp set global autotuninglevel=disabled"
]

def slow_type(text, output_widget):
    for char in text:
        output_widget.insert(tk.END, char)
        output_widget.update()
        time.sleep(0.05)
    output_widget.insert(tk.END, "\n")

def scan_hardware():
    results = "Scanning Hardware...\nCPU: Intel i9\nRAM: 16GB\nGPU: RTX 3090\n\nSuggested Tweaks:\n"
    results += "\n".join(random.sample(hardware_suggestions, 3))
    display_results(results)

def scan_software():
    results = "Scanning Software...\nOS: Windows 11\nAntivirus: McAfee\nBrowser: Chrome\n\nSuggested Tweaks:\n"
    results += "\n".join(random.sample(software_suggestions, 3))
    display_results(results)

def scan_settings():
    results = "Scanning Settings...\nResolution: 1920x1080\nMouse: Default\nTheme: Light\n\nSuggested Tweaks:\n"
    results += "\n".join(random.sample(settings_suggestions, 3))
    display_results(results)

def display_results(results):
    terminal_output.delete(1.0, tk.END)
    slow_type(results, terminal_output)

def welcome_message():
    text = (
        "Welcome to TweaksAI!\n"
        "Try scanning your system's hardware, software, or applications to debloat your PC and receive suggestions to optimize performance.\n\n"
        "Scan Hardware | Scan Software | Scan Settings\n\n"
        "For more information, visit our X account: https://x.com/TweaksAI"
    )
    slow_type(text, terminal_output)

# Create a desktop shortcut
def create_shortcut():
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory of the script
    shortcut_name = "TweaksAI Desktop Shortcut"  # Name for the shortcut
    shortcut_target = os.path.join(current_dir, "tweaks_ai_app.py")  # Path to the main Python script
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # Path to the Desktop folder
    shortcut_location = os.path.join(desktop, f"{shortcut_name}.lnk")  # Where the shortcut will be created

    shell = win32com.client.Dispatch("WScript.Shell")  # Get the Windows Script Host shell
    shortcut = shell.CreateShortCut(shortcut_location)  # Create the shortcut at the specified location
    shortcut.TargetPath = shortcut_target  # Set the target of the shortcut to your Python script
    shortcut.WorkingDirectory = current_dir  # Set the working directory to your script’s folder
    shortcut.IconLocation = os.path.join(current_dir, "tweaks_icon.ico")  # Icon for the shortcut
    shortcut.save()  # Save the shortcut

# Main window
window = tk.Tk()
window.title("TweaksAI")
window.geometry("1920x1080")

# Background image (replace with your new image)
bg_image = Image.open("TweaksAI background.jpg")  # Make sure this file is 1920x1080
bg_image = bg_image.resize((1920, 1080), Image.Resampling.LANCZOS)  # Ensure resizing is done to match the window size
bg_image = bg_image.convert("RGBA")  # Ensure it's in RGBA mode (supports transparency)
bg_image_tk = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(window, width=1920, height=1080, highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.create_image(0, 0, image=bg_image_tk, anchor=tk.NW)

# Terminal top right
terminal_frame = tk.Frame(window, bg='SystemButtonFace', highlightthickness=0)
terminal_frame.place(x=950, y=3)

terminal_title = tk.Label(terminal_frame, text="== TWEAKER AGENT ==", bg="black", fg="lightgray", font=("Courier", 14, "bold"))
terminal_title.pack(side=tk.TOP, anchor="w")

terminal_output = tk.Text(terminal_frame, height=30, width=100, wrap=tk.WORD, bg="black", fg="lightgray", font=("Courier", 12), bd=0, highlightthickness=0)
terminal_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Buttons & descriptions BELOW terminal, centered under the terminal
button_frame = tk.Frame(window, bg='lightgray', highlightthickness=0)  # Changed the background of the frame to light gray
button_frame.place(x=1290 - 225, y=573)  # Centering the button panel below the terminal (taking button width into account)

button_font = ("Courier", 13, "bold")
desc_font = ("Courier", 11)

# Buttons with original colors
btn_hardware = tk.Button(button_frame, text="SCAN HARDWARE", command=scan_hardware, width=25, height=2,
                         bg="#4682B4", fg="white", font=button_font, bd=0, highlightthickness=0)
btn_hardware.grid(row=0, column=0, pady=12, padx=10)

btn_software = tk.Button(button_frame, text="SCAN SOFTWARE", command=scan_software, width=25, height=2,
                         bg="#5F9EA0", fg="white", font=button_font, bd=0, highlightthickness=0)
btn_software.grid(row=1, column=0, pady=12, padx=10)

btn_settings = tk.Button(button_frame, text="SCAN SETTINGS", command=scan_settings, width=25, height=2,
                         bg="#6495ED", fg="white", font=button_font, bd=0, highlightthickness=0)
btn_settings.grid(row=2, column=0, pady=12, padx=10)

# Descriptions with light gray background
tk.Label(button_frame, text="Analyzes hardware for optimization.", font=desc_font,
         fg="black", bg="lightgray").grid(row=0, column=1, sticky="w", padx=10)
tk.Label(button_frame, text="Scans installed software for performance tweaks.", font=desc_font,
         fg="black", bg="lightgray").grid(row=1, column=1, sticky="w", padx=10)
tk.Label(button_frame, text="Checks system settings for performance tips.", font=desc_font,
         fg="black", bg="lightgray").grid(row=2, column=1, sticky="w", padx=10)

# Welcome message
welcome_message()

# Close handler
def on_close():
    window.quit()

window.protocol("WM_DELETE_WINDOW", on_close)

# Create the desktop shortcut when the app is launched
create_shortcut()

window.mainloop()
