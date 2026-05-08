import os
import subprocess

WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"
BLOG_DIR = os.path.join(WEBSITE_DIR, "blog")
INDEX_FILE = os.path.join(BLOG_DIR, "index.html")

def generate_index():
    print("--- GENERATING STUNNING BLOG INDEX ---")
    files = [f for f in os.listdir(BLOG_DIR) if f.endswith('.html') and f != 'index.html']
    files.sort(key=lambda x: os.path.getmtime(os.path.join(BLOG_DIR, x)), reverse=True)
    
    blog_cards = ""
    for f in files:
        title = f.replace(".html", "").replace("-", " ").title()
        blog_cards += f'''
        <a href="{f}" class="blog-card">
            <div class="card-tag">Forensic Intelligence</div>
            <h3>{title}</h3>
            <p>Real-time security analysis and technical breakdown for the 2026 UK market.</p>
            <div class="card-footer">
                <span>Read Full Audit</span>
                <span class="arrow">&rarr;</span>
            </div>
        </a>
        '''

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Security Intelligence | Gary Pearce Forensic SEO</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Montserrat:wght@900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --gold: #f59e0b;
            --gold-glow: rgba(245, 158, 11, 0.4);
            --dark-bg: #020617;
            --card-bg: rgba(15, 23, 42, 0.6);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ 
            font-family: 'Inter', sans-serif; 
            background-color: var(--dark-bg); 
            color: var(--text-main);
            background-image: 
                radial-gradient(circle at 20% 20%, rgba(245, 158, 11, 0.05) 0%, transparent 40%),
                radial-gradient(circle at 80% 80%, rgba(245, 158, 11, 0.05) 0%, transparent 40%);
            min-height: 100vh;
            padding-bottom: 100px;
        }}

        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 2rem; }}

        header {{
            padding: 8rem 0 4rem;
            text-align: center;
        }}

        .back-link {{
            display: inline-block;
            color: var(--gold);
            text-decoration: none;
            font-weight: 700;
            margin-bottom: 2rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-size: 0.8rem;
            transition: 0.3s;
        }}
        .back-link:hover {{ letter-spacing: 4px; }}

        h1 {{
            font-family: 'Montserrat', sans-serif;
            font-size: clamp(2.5rem, 6vw, 4.5rem);
            line-height: 1;
            margin-bottom: 1.5rem;
            background: linear-gradient(to right, #fff, var(--gold), #fff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-transform: uppercase;
        }}

        .subtitle {{
            color: var(--text-muted);
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto 4rem;
        }}

        .blog-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 2rem;
        }}

        .blog-card {{
            background: var(--card-bg);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            padding: 2.5rem;
            text-decoration: none;
            color: inherit;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            backdrop-filter: blur(10px);
            display: flex;
            flex-direction: column;
        }}

        .blog-card:hover {{
            transform: translateY(-10px) scale(1.02);
            border-color: var(--gold);
            box-shadow: 0 20px 40px rgba(0,0,0,0.4), 0 0 20px var(--gold-glow);
            background: rgba(15, 23, 42, 0.8);
        }}

        .card-tag {{
            display: inline-block;
            color: var(--gold);
            font-size: 0.7rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 1rem;
            padding: 4px 10px;
            background: rgba(245, 158, 11, 0.1);
            border-radius: 4px;
        }}

        h3 {{
            font-family: 'Montserrat', sans-serif;
            font-size: 1.5rem;
            margin-bottom: 1rem;
            line-height: 1.3;
        }}

        .blog-card p {{
            color: var(--text-muted);
            font-size: 0.95rem;
            margin-bottom: 2rem;
            flex-grow: 1;
        }}

        .card-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: 700;
            color: var(--gold);
            font-size: 0.9rem;
            text-transform: uppercase;
        }}

        .arrow {{ transition: 0.3s; }}
        .blog-card:hover .arrow {{ transform: translateX(10px); }}

    </style>
</head>
<body>
    <div class="container">
        <header>
            <a href="../index.html" class="back-link">&larr; Return to Core Hub</a>
            <h1>Security Guides</h1>
            <p class="subtitle">Forensic security analysis, technical guides, and real-time connectivity insights for the North's most elite properties.</p>
        </header>

        <div class="blog-grid">
            {blog_cards}
        </div>
    </div>
</body>
</html>
'''
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("DONE: Stunning Blog Index Generated.")

def deploy():
    print("--- PUSHING TO GITHUB/CLOUDFLARE ---")
    try:
        subprocess.run("git add .", shell=True, cwd=WEBSITE_DIR)
        subprocess.run('git commit -m "Live Swarm Intel: Premium Design Upgrade"', shell=True, cwd=WEBSITE_DIR)
        subprocess.run("git push origin main", shell=True, cwd=WEBSITE_DIR)
        print("DONE: DEPLOYED SUCCESSFULLY.")
    except Exception as e:
        print(f"Deployment error: {e}")

if __name__ == "__main__":
    generate_index()
    deploy()
