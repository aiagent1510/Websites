import os

WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"
BLOG_DIR = os.path.join(WEBSITE_DIR, "blog")

REGIONS = {
    "North East": ["Newcastle", "Sunderland", "Durham", "Gateshead", "Middlesbrough", "South Shields", "North Shields", "Washington", "Hartlepool", "Darlington", "Alnwick", "Morpeth", "Blyth", "Ashington", "Peterlee", "Bishop Auckland", "Consett", "Hexham"],
    "Yorkshire": ["Leeds", "York", "Sheffield", "Hull", "Bradford", "Huddersfield", "Harrogate", "Wakefield", "Doncaster", "Halifax", "Scarborough", "Ripon", "Beverley", "Whitby"],
    "North West": ["Manchester", "Liverpool", "Preston", "Blackpool", "Bolton", "Oldham", "Stockport", "Warrington", "Rochdale", "Salford", "Bury", "Wigan", "Crewe", "Lancaster", "Carlisle"],
    "Midlands": ["Nottingham", "Lincoln"]
}

def generate_index():
    print("--- REBUILDING BLOG HUB: blog/index.html ---")
    
    files = [f for f in os.listdir(BLOG_DIR) if f.endswith(".html") and f != "index.html"]
    
    # Sort files into categories
    categorized = {r: [] for r in REGIONS}
    categorized["Technical Guides"] = []
    
    for f in files:
        matched = False
        for region, cities in REGIONS.items():
            for city in cities:
                if city.lower().replace(" ", "-") in f:
                    categorized[region].append(f)
                    matched = True
                    break
            if matched: break
        
        if not matched:
            categorized["Technical Guides"].append(f)

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Security Intelligence Hub | Gary Pearce Forensic SEO</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Montserrat:wght@900&display=swap" rel="stylesheet">
    <style>
        :root {{ --gold: #f59e0b; --dark: #0f172a; --text: #f8fafc; --muted: #94a3b8; }}
        body {{ font-family: 'Inter', sans-serif; background: var(--dark); color: var(--text); line-height: 1.6; margin: 0; padding: 0; }}
        .container {{ max-width: 1100px; margin: 0 auto; padding: 4rem 2rem; }}
        h1 {{ font-family: 'Montserrat', sans-serif; color: var(--gold); font-size: 3.5rem; text-transform: uppercase; margin-bottom: 2rem; border-left: 8px solid var(--gold); padding-left: 1.5rem; }}
        h2 {{ color: var(--gold); font-size: 1.5rem; margin-top: 4rem; border-bottom: 1px solid rgba(245,158,11,0.2); padding-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 2px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1.5rem; margin-top: 1.5rem; }}
        .card {{ background: rgba(30, 41, 59, 0.5); border: 1px solid rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 12px; transition: 0.3s; text-decoration: none; color: inherit; display: flex; flex-direction: column; }}
        .card:hover {{ transform: translateY(-5px); border-color: var(--gold); background: rgba(245, 158, 11, 0.05); }}
        .card h3 {{ margin: 0 0 1rem 0; color: #fff; font-size: 1.1rem; line-height: 1.3; }}
        .card p {{ color: var(--muted); font-size: 0.9rem; margin: 0; flex-grow: 1; }}
        .tag {{ display: inline-block; background: var(--gold); color: var(--dark); padding: 2px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: 900; text-transform: uppercase; margin-bottom: 0.5rem; width: fit-content; }}
        .nav-back {{ margin-bottom: 2rem; display: block; color: var(--muted); text-decoration: none; font-weight: 600; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; }}
        .nav-back:hover {{ color: var(--gold); }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../index.html" class="nav-back">← Back to Main Site</a>
        <h1>Forensic Analysis of 2026 Security Infrastructure</h1>
        <p style="font-size: 1.2rem; color: var(--muted); max-width: 800px;">A comprehensive repository of technical audits, implementation strategies, and forensic security evaluations across the UK.</p>
'''

    for category, category_files in categorized.items():
        if not category_files: continue
        
        html_content += f'<h2>{category}</h2><div class="grid">'
        for f in category_files:
            title = f.replace(".html", "").replace("-", " ").title()
            if "2026 Audit" in title:
                tag = "Forensic Audit"
            else:
                tag = "Technical Guide"
            
            html_content += f'''
            <a href="{f}" class="card">
                <div class="tag">{tag}</div>
                <h3>{title}</h3>
                <p>Master-level forensic analysis and implementation strategy for 2026 security standards.</p>
            </a>
            '''
        html_content += '</div>'

    html_content += '''
    </div>
</body>
</html>
'''

    with open(os.path.join(BLOG_DIR, "index.html"), "w", encoding='utf-8') as f:
        f.write(html_content)
    print("DONE: blog/index.html updated.")

if __name__ == "__main__":
    generate_index()
