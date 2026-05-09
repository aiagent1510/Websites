import os
import re

WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"
BLOG_DIR = os.path.join(WEBSITE_DIR, "blog")

def get_title(file_path):
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'<title>(.*?) \| Forensic Security Audit 2026</title>', content)
            if match:
                return match.group(1)
            # Try plain title
            match = re.search(r'<title>(.*?)</title>', content)
            if match:
                return match.group(1)
    except:
        pass
    return os.path.basename(file_path).replace("-", " ").replace(".html", "").title()

def generate_blog_index():
    print("--- REBUILDING BLOG HUB: blog/index.html ---")
    posts = []
    for f in os.listdir(BLOG_DIR):
        if f.endswith(".html") and f != "index.html":
            title = get_title(os.path.join(BLOG_DIR, f))
            posts.append({"title": title, "slug": f})
            
    # Sort posts alphabetically or by newest (we don't have date easily yet, so alpha)
    posts.sort(key=lambda x: x["title"])
    
    post_cards = ""
    for p in posts:
        post_cards += f'''
        <a href="{p['slug']}" class="blog-card" style="display: block; background: rgba(30, 41, 59, 0.5); padding: 2rem; border-radius: 16px; border: 1px solid rgba(245, 158, 11, 0.2); text-decoration: none; transition: 0.3s; margin-bottom: 1.5rem;">
            <div style="color: #f59e0b; font-weight: 900; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 0.5rem;">Verified Audit</div>
            <h3 style="color: #fff; margin: 0; font-size: 1.4rem;">{p['title']}</h3>
            <p style="color: #94a3b8; margin-top: 1rem; font-size: 0.9rem;">Master-level forensic analysis and implementation strategy for 2026 security standards.</p>
            <div style="color: #f59e0b; font-weight: 800; margin-top: 1.5rem; display: flex; align-items: center; gap: 0.5rem;">Read Audit &rarr;</div>
        </a>
        '''
        
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Security Intelligence Hub | Gary Pearce Forensic SEO</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Montserrat:wght@900&display=swap" rel="stylesheet">
    <style>
        :root {{ --gold: #f59e0b; --dark: #0f172a; --text: #f8fafc; }}
        body {{ font-family: 'Inter', sans-serif; background: var(--dark); color: var(--text); line-height: 1.6; margin: 0; padding: 0; }}
        .container {{ max-width: 1000px; margin: 0 auto; padding: 6rem 2rem; }}
        .header {{ text-align: center; margin-bottom: 6rem; }}
        h1 {{ font-family: 'Montserrat', sans-serif; font-size: 4rem; color: var(--gold); text-transform: uppercase; margin: 0; }}
        .tagline {{ font-size: 1.2rem; color: #94a3b8; margin-top: 1rem; }}
        .blog-grid {{ display: grid; grid-template-columns: 1fr; gap: 2rem; }}
        .blog-card:hover {{ transform: translateY(-10px); border-color: var(--gold); box-shadow: 0 20px 40px rgba(0,0,0,0.4); }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../index.html" style="color: #94a3b8; text-decoration: none; font-weight: 800; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 2px;">&larr; Back to Main Site</a>
        <div class="header">
            <h1>Intelligence Hub</h1>
            <p class="tagline">Forensic Analysis of 2026 Security Infrastructure</p>
        </div>
        <div class="blog-grid">
            {post_cards}
        </div>
    </div>
</body>
</html>
'''
    
    with open(os.path.join(BLOG_DIR, "index.html"), "w", encoding='utf-8') as f:
        f.write(html)
    print("DONE: blog/index.html updated.")

if __name__ == "__main__":
    generate_blog_index()
