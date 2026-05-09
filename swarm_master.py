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
                # 1. Special Sync for Cloudflare (Root to Public)
                if script == "swarm_push.py":
                    print("--- SYNCING ROOT TO PUBLIC FOR CLOUDFLARE ---")
                    subprocess.run(["cmd", "/c", "xcopy /Y index.html public\\"], cwd=WEBSITE_DIR)
                    subprocess.run(["cmd", "/c", "xcopy /S /E /Y blog public\\blog\\"], cwd=WEBSITE_DIR)
                    subprocess.run(["cmd", "/c", "xcopy /Y sitemap.xml public\\"], cwd=WEBSITE_DIR)
                
                # 2. Run the script
                script_path = os.path.join(WEBSITE_DIR, script)
                subprocess.run(["python", script_path], check=True)
            except Exception as e:
                print(f"FAILED TO RUN {script}: {e}")
        
        print("\n=== SWARM CYCLE COMPLETE. SLEEPING FOR 30 MINUTES ===")
        # Sleeping for 30 mins to avoid GitHub push limits but keep it fresh
        time.sleep(1800)

if __name__ == "__main__":
    run_master()
