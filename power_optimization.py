import subprocess
import time

def set_high_performance():
    """Sets Windows power plan to High Performance mode."""
    try:
        subprocess.run(["powercfg", "/S", "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"], check=True)
        return "Windows power plan set to High Performance."
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        print(set_high_performance())
        time.sleep(86400)  # Run once a day to ensure it stays in High Performance mode.
