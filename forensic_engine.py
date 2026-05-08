class ForensicEngine:
    @staticmethod
    def get_prompt(question, pillars):
        return f'''
        You are a Forensic Security Expert and SEO Master. 
        Write a technical, authoritative blog post answering: "{question}"
        
        STRICT RULES:
        1. NO MARKDOWN. Output PURE HTML structure.
        2. 2-3 SENTENCES PER PARAGRAPH ONLY. This is for mobile SEO.
        3. HIGH TECHNICAL AUTHORITY. Mention specific models, frequencies (868MHz), sensor types (PIR, Microwave), and standards (Grade 2/3).
        
        STRUCTURE:
        - <h2> Title with the question
        - <p> Forensic intro.
        - <h3> The Technical Breakdown
        - <p> Details about technology and security standards.
        - [INSERT_TABLE_HERE] - Create a 3-column HTML table comparing 3 key technical specs.
        - <h3> 2026 Forensic Verdict
        - <p> Final recommendation for UK homeowners.
        - [INSERT_VIDEO_HERE] - Provide a descriptive placeholder for a technical security video.
        - [INSERT_SCHEMA_HERE] - Provide a JSON-LD FAQ Schema for this question.
        
        INTERLINKING:
        Link naturally to at least 2 of these pillar pages using <a href="../{pillars[0]['url']}">:
        {pillars}
        '''

    @staticmethod
    def wrap_html(content, title, canonical_url, image_url=None):
        # Clean up placeholders and inject real data
        # For simplicity in this demo, the LLM will provide the HTML strings for table/schema
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Forensic Security Audit</title>
    <link rel="canonical" href="{canonical_url}">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; background: #0f172a; color: #f8fafc; line-height: 1.8; margin: 0; padding: 0; }}
        .container {{ max-width: 850px; margin: 0 auto; padding: 4rem 2rem; }}
        header {{ border-bottom: 1px solid rgba(245, 158, 11, 0.2); margin-bottom: 3rem; padding-bottom: 2rem; }}
        h1 {{ color: #f59e0b; font-size: 2.5rem; line-height: 1.2; margin-bottom: 1rem; }}
        h2, h3 {{ color: #f59e0b; margin-top: 2.5rem; }}
        p {{ margin-bottom: 1.5rem; font-size: 1.1rem; color: #cbd5e1; }}
        a {{ color: #fbbf24; text-decoration: none; font-weight: 600; border-bottom: 1px solid transparent; transition: 0.3s; }}
        a:hover {{ border-color: #fbbf24; }}
        .infographic {{ width: 100%; border-radius: 12px; border: 1px solid rgba(245, 158, 11, 0.3); margin: 2rem 0; box-shadow: 0 20px 40px rgba(0,0,0,0.5); }}
        table {{ width: 100%; border-collapse: collapse; margin: 2rem 0; background: rgba(30, 41, 59, 0.5); border-radius: 8px; overflow: hidden; }}
        th, td {{ padding: 1rem; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.05); }}
        th {{ background: rgba(245, 158, 11, 0.1); color: #f59e0b; }}
        .video-placeholder {{ background: #000; padding: 2rem; text-align: center; border-radius: 12px; border: 1px solid #334155; margin: 2rem 0; }}
        .back-btn {{ display: inline-block; margin-bottom: 2rem; color: #f59e0b; text-decoration: none; font-weight: bold; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px; }}
    </style>
</head>
<body>
    <div class="container">
        <a href="index.html" class="back-btn">&larr; Back to Security Guides</a>
        <header>
            <h1>{title}</h1>
            <p style="color: #64748b;">Forensic Security Audit | Real-time 2026 Intelligence</p>
        </header>
        
        <article>
            {f'<img src="../{image_url}" class="infographic" alt="{title}">' if image_url else ''}
            {content}
        </article>
        
        <footer style="margin-top: 5rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.05); color: #64748b; font-size: 0.9rem;">
            <p>&copy; 2026 Gary Pearce Home Services | Forensic Security & Technical Compliance</p>
        </footer>
    </div>
</body>
</html>
'''
