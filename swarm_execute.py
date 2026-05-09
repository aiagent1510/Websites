import os
import time
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
    {"city": "Darlington", "service": "ajax-security-systems"}
]

WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"
BLOG_DIR = os.path.join(WEBSITE_DIR, "blog")

if not os.path.exists(BLOG_DIR):
    os.makedirs(BLOG_DIR)

def generate_high_quality_posts():
    print("--- STARTING HIGH-QUALITY FORENSIC GENERATION ---")
    
    for t in TARGETS:
        city = t["city"]
        service = t["service"]
        service_display = service.replace("-", " ").title()
        title = f"{service_display} in {city} (2026 Forensic Audit)"
        slug = f"{service}-{city.lower().replace(' ', '-')}-2026-audit.html"
        
        print(f"Generating: {title}")
        
        content = ForensicEngine.generate_forensic_content(city, service)
        canonical = f"https://gary-pearce-home-services.pages.dev/blog/{slug}"
        
        final_html = ForensicEngine.wrap_html(content, title, canonical)
        
        file_path = os.path.join(BLOG_DIR, slug)
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(final_html)
            
    print("DONE: Generated 10 premium forensic audits.")

if __name__ == "__main__":
    generate_high_quality_posts()
