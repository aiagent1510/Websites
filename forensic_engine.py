class ForensicEngine:
    @staticmethod
    def get_prompt(question, pillars):
        return f'''
        You are a Master Forensic SEO Expert with 20 years experience in UK security (CCTV, Alarms, Data Cabling). 
        Write a hyper-technical, forensic-grade audit answering: "{question}"
        
        CRITICAL SEO SKILLS TO DEPLOY:
        1. NO FILLER: Do not use phrases like "Today we are focusing on" or "In this blog post".
        2. ENTITY DENSITY: Mention specific hardware: Ajax Hub 2 Plus, Hikvision ColorVu G2, Dahua TiOC 2.0, Cat7 LSZH (Low Smoke Zero Halogen).
        3. LOCAL FORENSICS: If the topic is location-based, mention specific technical challenges like "Sunderland coastal salinity impact on outdoor PIRs" or "Leeds city center RF interference at 868MHz".
        4. TECHNICAL DEPTH: Talk about bitrates (H.265+), throughput (Gbps), frequency hopping, and Grade 3 EN50131 compliance.
        
        STRUCTURE:
        - <h2> {question}
        - <p> A strong, technical opening that defines the current 2026 standard.
        - [INSERT_TABLE_HERE] - A technical specification table comparing the top 3 hardware solutions for this specific problem.
        - <h3> Forensic Implementation Strategy
        - <p> 2-3 sentences on the exact installation methodology (e.g. "We deploy CAT7 backbone to eliminate latency for 4K AI triggers").
        - <h3> The 2026 Verdict
        - <p> Final authoritative recommendation.
        
        INTERLINKING:
        Link naturally to the regional hubs using technical anchor text:
        {pillars}
        
        [INSERT_VIDEO_HERE] - Placeholder for a professional installation demo.
        [INSERT_SCHEMA_HERE] - JSON-LD FAQ schema for Google Rich Results.
        '''

    @staticmethod
    def wrap_html(content, title, canonical_url, image_url=None):
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Forensic Security Audit 2026</title>
    <meta name="description" content="Technical forensic audit on {title}. Professional security standards for 2026 UK market.">
    <link rel="canonical" href="{canonical_url}">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Montserrat:wght@900&display=swap" rel="stylesheet">
    <style>
        :root {{ --gold: #f59e0b; --dark: #0f172a; --text: #f8fafc; --muted: #94a3b8; }}
        body {{ font-family: 'Inter', sans-serif; background: var(--dark); color: var(--text); line-height: 1.8; margin: 0; padding: 0; }}
        .container {{ max-width: 900px; margin: 0 auto; padding: 6rem 2rem; }}
        header {{ border-left: 4px solid var(--gold); padding-left: 2rem; margin-bottom: 4rem; }}
        h1 {{ font-family: 'Montserrat', sans-serif; color: var(--gold); font-size: 3rem; text-transform: uppercase; line-height: 1.1; margin-bottom: 1rem; }}
        h2 {{ color: var(--gold); font-size: 2rem; margin-top: 3rem; border-bottom: 1px solid rgba(245, 158, 11, 0.2); padding-bottom: 1rem; }}
        h3 {{ color: #fff; font-size: 1.5rem; margin-top: 2.5rem; }}
        p {{ margin-bottom: 1.5rem; font-size: 1.15rem; color: #cbd5e1; }}
        a {{ color: var(--gold); text-decoration: none; font-weight: 800; border-bottom: 1px dashed var(--gold); transition: 0.3s; }}
        a:hover {{ border-bottom-style: solid; background: rgba(245, 158, 11, 0.1); }}
        .infographic {{ width: 100%; border-radius: 16px; border: 1px solid rgba(245, 158, 11, 0.3); margin: 3rem 0; box-shadow: 0 30px 60px rgba(0,0,0,0.6); }}
        table {{ width: 100%; border-collapse: collapse; margin: 3rem 0; background: rgba(30, 41, 59, 0.5); border-radius: 12px; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); }}
        th, td {{ padding: 1.2rem; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.05); }}
        th {{ background: rgba(245, 158, 11, 0.15); color: var(--gold); font-weight: 800; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px; }}
        .video-box {{ background: #000; border-radius: 16px; border: 1px solid #334155; margin: 3rem 0; overflow: hidden; }}
        .forensic-stamp {{ display: inline-block; background: var(--gold); color: var(--dark); padding: 4px 12px; font-weight: 900; border-radius: 4px; font-size: 0.7rem; text-transform: uppercase; margin-bottom: 1rem; }}
    </style>
</head>
<body>
    <div class="container">
        <a href="index.html" style="border:none; color: var(--muted); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 2px;">&larr; Back to Forensic Hub</a>
        <header style="margin-top: 2rem;">
            <div class="forensic-stamp">Verified Forensic Audit 2026</div>
            <h1>{title}</h1>
        </header>
        
        <article>
            {f'<img src="../{image_url}" class="infographic" alt="{title}">' if image_url else ''}
            {content}
        </article>
        
        <footer style="margin-top: 8rem; padding-top: 4rem; border-top: 1px solid rgba(255,255,255,0.1); text-align: center;">
            <p style="color: var(--muted);">Gary Pearce Home Services | Engineering Excellence Since 2004</p>
            <p style="font-size: 0.8rem;">[Manchester | Leeds | York | Huddersfield | Sheffield]</p>
        </footer>
    </div>
</body>
</html>
'''
