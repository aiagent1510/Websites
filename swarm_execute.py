import os
import time
import random
from forensic_engine import ForensicEngine

# THE EXPANDED HIGH-QUALITY TARGET LIST
TARGETS = [
    {"city": "Newcastle", "service": "cctv-installation"},
    {"city": "Sunderland", "service": "data-cabling"},
    {"city": "Durham", "service": "wireless-alarms"},
    {"city": "Gateshead", "service": "smart-home-security"},
    {"city": "Middlesbrough", "service": "intruder-alarms"},
    {"city": "South Shields", "service": "cctv-maintenance"},
    {"city": "North Shields", "service": "cat7-networking"},
    {"city": "Washington", "service": "business-security"},
    {"city": "Hartlepool", "service": "hikvision-ax-pro"},
    {"city": "Darlington", "service": "ajax-security-systems"},
    {"city": "Leeds", "service": "cctv-installation"},
    {"city": "Manchester", "service": "data-cabling"},
    {"city": "York", "service": "wireless-alarms"},
    {"city": "Liverpool", "service": "smart-home-security"},
    {"city": "Sheffield", "service": "intruder-alarms"},
    {"city": "Nottingham", "service": "cctv-maintenance"},
    {"city": "Hull", "service": "cat7-networking"},
    {"city": "Bradford", "service": "business-security"},
    {"city": "Chester", "service": "hikvision-ax-pro"},
    {"city": "Preston", "service": "ajax-security-systems"},
    {"city": "Huddersfield", "service": "cctv-installation"},
    {"city": "Harrogate", "service": "data-cabling"},
    {"city": "Wakefield", "service": "wireless-alarms"},
    {"city": "Doncaster", "service": "smart-home-security"},
    {"city": "Halifax", "service": "intruder-alarms"},
    {"city": "Blackpool", "service": "cctv-maintenance"},
    {"city": "Bolton", "service": "cat7-networking"},
    {"city": "Oldham", "service": "business-security"},
    {"city": "Stockport", "service": "hikvision-ax-pro"},
    {"city": "Warrington", "service": "ajax-security-systems"},
    {"city": "Rochdale", "service": "cctv-installation"},
    {"city": "Salford", "service": "data-cabling"},
    {"city": "Bury", "service": "wireless-alarms"},
    {"city": "Wigan", "service": "smart-home-security"},
    {"city": "Crewe", "service": "intruder-alarms"},
    {"city": "Lincoln", "service": "cctv-maintenance"},
    {"city": "Scarborough", "service": "cat7-networking"},
    {"city": "Carlisle", "service": "business-security"},
    {"city": "Lancaster", "service": "hikvision-ax-pro"},
    {"city": "Ripon", "service": "ajax-security-systems"},
    {"city": "Beverley", "service": "cctv-installation"},
    {"city": "Hexham", "service": "data-cabling"},
    {"city": "Alnwick", "service": "wireless-alarms"},
    {"city": "Morpeth", "service": "smart-home-security"},
    {"city": "Whitby", "service": "intruder-alarms"},
    {"city": "Blyth", "service": "cctv-maintenance"},
    {"city": "Ashington", "service": "cat7-networking"},
    {"city": "Peterlee", "service": "business-security"},
    {"city": "Bishop Auckland", "service": "hikvision-ax-pro"},
    {"city": "Consett", "service": "ajax-security-systems"}
]

WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"
BLOG_DIR = os.path.join(WEBSITE_DIR, "blog")

if not os.path.exists(BLOG_DIR):
    os.makedirs(BLOG_DIR)

def get_related_links(current_target):
    related = []
    # Pick 3 random targets that are not the current one
    pool = [t for t in TARGETS if t != current_target]
    selection = random.sample(pool, 3)
    
    for s in selection:
        city = s["city"]
        service = s["service"]
        service_display = service.replace("-", " ").title()
        title = f"{service_display} in {city} (2026 Forensic Audit)"
        slug = f"{service}-{city.lower().replace(' ', '-')}-2026-audit.html"
        related.append({"title": title, "url": slug})
    
    return related

def generate_high_quality_posts():
    print("--- STARTING HIGH-QUALITY FORENSIC GENERATION WITH INTERNAL LINKING ---")
    
    for t in TARGETS:
        city = t["city"]
        service = t["service"]
        service_display = service.replace("-", " ").title()
        title = f"{service_display} in {city} (2026 Forensic Audit)"
        slug = f"{service}-{city.lower().replace(' ', '-')}-2026-audit.html"
        
        print(f"Generating: {title}")
        
        related_links = get_related_links(t)
        
        content = ForensicEngine.generate_forensic_content(city, service, related_links)
        canonical = f"https://gary-pearce-home-services.pages.dev/blog/{slug}"
        
        final_html = ForensicEngine.wrap_html(content, title, canonical)
        
        file_path = os.path.join(BLOG_DIR, slug)
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(final_html)
            
    print(f"DONE: Generated {len(TARGETS)} premium forensic audits with internal linking.")

if __name__ == "__main__":
    generate_high_quality_posts()
