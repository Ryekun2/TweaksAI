import time
import random

def tweak_10():
    return "Clear temp files and cache regularly to maintain system speed."

if __name__ == "__main__":
    while True:
        print(tweak_10())
        time.sleep(random.randint(60, 300))