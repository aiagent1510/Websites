import os
import subprocess

WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"
BLOG_DIR = os.path.join(WEBSITE_DIR, "blog")
INDEX_FILE = os.path.join(BLOG_DIR, "index.html")

def update_index():
    print("--- UPDATING BLOG INDEX ---")
    
    files = [f for f in os.listdir(BLOG_DIR) if f.endswith('.html') and f != 'index.html']
    files.sort(key=lambda x: os.path.getmtime(os.path.join(BLOG_DIR, x)), reverse=True)
    
    list_items = []
    for f in files:
        title = f.replace(".html", "").replace("-", " ").title()
        list_items.append(f'<li><a href="{f}">{title}</a></li>')
    
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    header = content.split('<ul>')[0]
    footer = content.split('</ul>')[1]
    
    new_index = f"{header}<ul>\n" + "\n".join(list_items) + f"\n</ul>{footer}"
    
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(new_index)
    
    print("DONE: Blog Index Updated.")

def deploy():
    print("--- PUSHING TO GITHUB/CLOUDFLARE ---")
    try:
        subprocess.run("git add .", shell=True, cwd=WEBSITE_DIR)
        subprocess.run('git commit -m "Live Swarm Intel: Real-time FAQ Update"', shell=True, cwd=WEBSITE_DIR)
        subprocess.run("git push origin main", shell=True, cwd=WEBSITE_DIR)
        print("DONE: DEPLOYED SUCCESSFULLY.")
    except Exception as e:
        print(f"Deployment error: {e}")

if __name__ == "__main__":
    update_index()
    deploy()
