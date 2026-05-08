import os
import json
import time
from forensic_engine import ForensicEngine

# THE FULL INTELLIGENCE CLUSTER
BLOG_POSTS = [
    {"q": "WiFi 7 Upgrades in Sunderland (2026 Technical Audit)", "slug": "wifi-7-upgrades-in-sunderland-2026-technical-audit.html", "cluster": "networking"},
    {"q": "Hikvision AX Pro vs Ajax: The Ultimate 2026 Wireless Security Showdown", "slug": "hikvision-ax-pro-vs-ajax-the-ultimate-2026-wireless-security-showdown.html", "cluster": "alarms"},
    {"q": "Is Ajax Hub 2 Plus truly Grade 2 compliant in the UK?", "slug": "is-ajax-hub-2-plus-truly-grade-2-compliant-in-the-uk.html", "cluster": "alarms"},
    {"q": "Starlink for security cameras: A guide for rural Northumberland businesses", "slug": "starlink-for-security-cameras-a-guide-for-rural-northumberland-businesses.html", "cluster": "surveillance"},
    {"q": "Dahua TiOC 2.0 vs Hikvision ColorVu: 2026 Night Vision Comparison", "slug": "dahua-tioc-2.0-vs-hikvision-colorvu-2026-night-vision-comparison.html", "cluster": "surveillance"},
    {"q": "How to mitigate 868MHz frequency jamming in wireless alarms?", "slug": "how-to-mitigate-868mhz-frequency-jamming-in-wireless-alarms.html", "cluster": "alarms"},
    {"q": "Cat6a vs Cat7 for 10Gbps home networking: What you actually need in 2026", "slug": "cat6a-vs-cat7-for-10gbps-home-networking-what-you-actually-need-in-2026.html", "cluster": "networking"}
]

PILLARS = [
    {"name": "Manchester CCTV Hub", "url": "cctv-cabling-manchester.html"},
    {"name": "Leeds Security Guide", "url": "cctv-cabling-leeds.html"},
    {"name": "Data Cabling UK Authority", "url": "data-cabling-manchester.html"}
]

WEBSITE_DIR = r"C:\Users\Gary\.gemini\antigravity\scratch\Websites"
BLOG_DIR = os.path.join(WEBSITE_DIR, "blog")

def generate_post(post_data):
    question = post_data["q"]
    slug = post_data["slug"]
    cluster = post_data["cluster"]
    
    print(f"--- GENERATING CLUSTERED POST: {question} ---")
    filename = os.path.join(BLOG_DIR, slug)
    canonical = f"https://gary-pearce-home-services.pages.dev/blog/{slug}"
    
    # Logic for Cluster Interlinking
    related_posts = [p for p in BLOG_POSTS if p["cluster"] == cluster and p["slug"] != slug]
    cross_cluster_links = ""
    for rp in related_posts:
        cross_cluster_links += f'<li>See our related audit: <a href="{rp["slug"]}">{rp["q"]}</a></li>'
    
    content = f'''
    <p>In the high-stakes environment of 2026 security, individual components are irrelevant without a cohesive, interlinked architecture. We don't just install hardware; we build resilient intelligence networks.</p>
    
    <table>
        <thead>
            <tr>
                <th>Infrastructure Component</th>
                <th>Traditional Standard</th>
                <th>Forensic 2026 Standard</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Data Backbone</td>
                <td>Cat5e / Cat6</td>
                <td>Cat7 LSZH (10Gbps)</td>
            </tr>
            <tr>
                <td>Wireless Protocol</td>
                <td>WiFi 5 / 6</td>
                <td>WiFi 7 (320MHz MLO)</td>
            </tr>
            <tr>
                <td>Intrusion Bus</td>
                <td>Unencrypted</td>
                <td>AES-128 Bit Dynamic Encryption</td>
            </tr>
        </tbody>
    </table>
    
    <h3>Forensic Implementation Strategy</h3>
    <p>Our methodology focuses on total system integrity. When deploying systems in Sunderland or Leeds, we ensure that the wireless alarm backbone—typically operating at 868MHz—is shielded against local RF interference. This is particularly critical when integrating high-bandwidth 8K CCTV streams that require the sub-ms latency offered by modern WiFi 7 and Cat7 networking standards.</p>
    
    <div style="background: rgba(245, 158, 11, 0.05); padding: 2rem; border-radius: 12px; border: 1px solid rgba(245, 158, 11, 0.2); margin: 2rem 0;">
        <h4 style="color: var(--gold); margin-bottom: 1rem;">Technical Intelligence Cluster:</h4>
        <ul style="list-style: none; padding: 0;">
            {cross_cluster_links}
        </ul>
    </div>
    
    <h3>The 2026 Verdict</h3>
    <p>A fragmented security system is a failed security system. For the most elite properties in the North, total interlinking between your data backbone and your intrusion protocols is the only way to achieve Grade 3 compliance.</p>
    
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{{
        "@type": "Question",
        "name": "{question}",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Total system interlinking using Cat7 and WiFi 7 standards is required for forensic-grade security in 2026."
        }}
      }}]
    }}
    </script>
    '''
    
    image_path = "Images/blog_graphics/ajax_vs_hikvision_2026.png"
    final_html = ForensicEngine.wrap_html(content, question, canonical, image_path)
    
    with open(filename, "w", encoding='utf-8') as f:
        f.write(final_html)
    print(f"DONE: {filename}")

if __name__ == "__main__":
    for p in BLOG_POSTS:
        generate_post(p)
        time.sleep(0.5)
