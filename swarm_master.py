import time
import subprocess
import os

SCRIPTS = [
    "swarm_execute.py",      # Generate the blog posts
    "blog_index_generator.py", # Build the blog/index.html hub
    "sitemap_generator.py",  # Update sitemap.xml
    "swarm_push.py"         # Push to GitHub
]

WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"

def run_master():
    print("=== STARTING AUTONOMOUS FORENSIC SWARM MASTER ===")
    
    while True:
        for script in SCRIPTS:
            print(f"\n>>> RUNNING: {script}")
            try:
                # Use absolute path for safety
                script_path = os.path.join(WEBSITE_DIR, script)
                subprocess.run(["python", script_path], check=True)
            except Exception as e:
                print(f"FAILED TO RUN {script}: {e}")
        
        print("\n=== SWARM CYCLE COMPLETE. SLEEPING FOR 30 MINUTES ===")
        # Sleeping for 30 mins to avoid GitHub push limits but keep it fresh
        time.sleep(1800)

if __name__ == "__main__":
    run_master()
