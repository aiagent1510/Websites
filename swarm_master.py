import os
import time
import subprocess
from swarm_execute import generate_post, BLOG_POSTS

WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"

def run_scout():
    print("--- [PHASE 1] RUNNING HERMES INTELLIGENCE SCOUT ---")
    subprocess.run("node hermes_scout.js", shell=True, cwd=WEBSITE_DIR)

def run_generation():
    print("--- [PHASE 2] GENERATING RICH FORENSIC CLUSTERS ---")
    # For a real 24/7 loop, we would parse the fresh output from hermes_scout.js
    # For now, we process our authoritative BLOG_POSTS list
    for p in BLOG_POSTS:
        generate_post(p)

def run_push():
    print("--- [PHASE 3] DEPLOYING LIVE TO GITHUB/CLOUDFLARE ---")
    subprocess.run("python swarm_push.py", shell=True, cwd=WEBSITE_DIR)

def eternal_loop():
    print("--- INITIALIZING ETERNAL SWARM LOOP (24/7 AUTONOMOUS MODE) ---")
    iteration = 1
    while True:
        print(f"\n=== SWARM ITERATION #{iteration} | {time.ctime()} ===")
        
        run_scout()
        run_generation()
        run_push()
        
        print(f"\n--- ITERATION #{iteration} COMPLETE. GOING INTO STEALTH SCOUTING MODE ---")
        iteration += 1
        
        # Wait for 1 hour before the next scout/deploy cycle
        # (Reduced to 30 seconds for the initial verification run)
        time.sleep(30)

if __name__ == "__main__":
    eternal_loop()
