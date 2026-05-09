import os
import datetime

WEBSITE_DIR = r"C:\Users\Gary\Desktop\Websites" # FALLBACK to original if needed
# But wait, I should use the path I've been using:
WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"

BASE_URL = "https://aiagent1510.github.io/Websites"

def generate_sitemap():
    print("--- REGENERATING SITEMAP.XML ---")
    files = []
    
    # Scan root
    for f in os.listdir(WEBSITE_DIR):
        if f.endswith(".html"):
            files.append(f)
            
    # Scan blog
    blog_dir = os.path.join(WEBSITE_DIR, "blog")
    if os.path.exists(blog_dir):
        for f in os.listdir(blog_dir):
            if f.endswith(".html"):
                files.append(f"blog/{f}")
                
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for f in files:
        loc = f"{BASE_URL}/{f}"
        priority = "1.0" if f == "index.html" else "0.8"
        sitemap_content += f'  <url><loc>{loc}</loc><priority>{priority}</priority></url>\n'
        
    sitemap_content += '</urlset>'
    
    with open(os.path.join(WEBSITE_DIR, "sitemap.xml"), "w", encoding='utf-8') as f:
        f.write(sitemap_content)
        
    print(f"DONE: sitemap.xml updated with {len(files)} URLs.")

if __name__ == "__main__":
    generate_sitemap()
