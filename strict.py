import os
import time

def restrict(seconds):
    print(f"Restricting this in {seconds} seconds...")
    time.sleep(seconds)
    print("Restricting now....")
    os.system("shutdown /r /t 1")

if __name__ == "__main__":
    # Time in seconds before the computer restarts
    seconds = 1000

    restrict(seconds)