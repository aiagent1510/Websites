import subprocess
import os

WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, cwd=WEBSITE_DIR, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"ERROR: {result.stderr}")
        return result.returncode == 0
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        return False

def deploy():
    print("--- STARTING URGENT DEPLOYMENT SYNC ---")
    
    # 1. Add all files
    run_command("git add .")
    
    # 2. Commit (even if empty to be safe, but git commit -m is fine)
    run_command('git commit -m "Live Intelligence Swarm Update: Forensic Blog Hub + Sitemap Update"')
    
    # 3. Push to main
    success = run_command("git push origin main")
    
    if success:
        print("--- DEPLOYMENT SUCCESSFUL: PUSHED TO GITHUB ---")
    else:
        print("--- DEPLOYMENT FAILED: CHECK GIT STATUS ---")

if __name__ == "__main__":
    deploy()
