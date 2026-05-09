import subprocess
import os
import datetime

WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, cwd=WEBSITE_DIR, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"GIT LOG: {result.stderr}")
        return result.returncode == 0
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        return False

def deploy():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"--- STARTING URGENT DEPLOYMENT SYNC [{timestamp}] ---")
    
    # 0. Create/Update a Heartbeat file to ensure there's ALWAYS a change
    heartbeat_path = os.path.join(WEBSITE_DIR, "HEARTBEAT.md")
    with open(heartbeat_path, "w") as f:
        f.write(f"# Forensic Swarm Heartbeat\nLast Active: {timestamp}\nStatus: Autonomous 24/7 Propagation Active")
    
    # 1. Add all files
    run_command("git add .")
    
    # 2. Commit with timestamp
    msg = f"Live Intelligence Swarm Update: {timestamp}"
    run_command(f'git commit -m "{msg}"')
    
    # 3. Push to main
    success = run_command("git push origin main")
    
    if success:
        print(f"--- DEPLOYMENT SUCCESSFUL [{timestamp}] ---")
        # Update a local status log for the user
        with open(os.path.join(WEBSITE_DIR, "DEPLOYMENT_STATUS.log"), "a") as log:
            log.write(f"[{timestamp}] SUCCESS: Pushed to GitHub\n")
    else:
        print(f"--- DEPLOYMENT FAILED [{timestamp}] ---")
        with open(os.path.join(WEBSITE_DIR, "DEPLOYMENT_STATUS.log"), "a") as log:
            log.write(f"[{timestamp}] FAILED: Push error\n")

if __name__ == "__main__":
    deploy()
