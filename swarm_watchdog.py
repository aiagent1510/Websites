import time
import os
import datetime

LOG_FILE = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites\DEPLOYMENT_STATUS.log"
MASTER_SCRIPT = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites\swarm_master.py"

def check_pulse():
    print("=== SWARM WATCHDOG ACTIVE ===")
    while True:
        if os.path.exists(LOG_FILE):
            last_mod = os.path.getmtime(LOG_FILE)
            elapsed = time.time() - last_mod
            
            if elapsed > 3600: # 1 hour
                print(f"[{datetime.datetime.now()}] ALERT: Swarm Master seems stuck! No log update for {elapsed/60:.1f} mins.")
                # We could try to restart it here if we had the PID, 
                # but for now, we'll just log the alert.
            else:
                print(f"[{datetime.datetime.now()}] PULSE OK: Last deployment was {elapsed/60:.1f} mins ago.")
        else:
            print(f"[{datetime.datetime.now()}] WARNING: No log file found yet.")
            
        time.sleep(600) # Check every 10 mins

if __name__ == "__main__":
    check_pulse()
