const fs = require('fs');
const path = require('path');

const SITE_URL = 'https://gary-pearce-home-services.pages.dev/';
const BLOG_DIR = path.join(__dirname, 'blog');
const PHONE = '07830638337';

if (!fs.existsSync(BLOG_DIR)) {
    fs.mkdirSync(BLOG_DIR);
}

const template = (title, content, slug, interlinks) => `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} | Gary Pearce Home Services Blog</title>
    <meta name="description" content="${title}. Expert security and connectivity insights for 2026.">
    <link rel="canonical" href="${SITE_URL}blog/${slug}.html">
    <style>
        body { font-family: 'Inter', sans-serif; background: #0f172a; color: white; margin: 0; line-height: 1.6; }
        .container { max-width: 900px; margin: 0 auto; padding: 2rem; }
        header { border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 2rem; margin-bottom: 2rem; }
        h1 { background: linear-gradient(to right, #60a5fa, #a855f7); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3rem; margin: 0; }
        .content { background: rgba(255, 255, 255, 0.03); padding: 3rem; border-radius: 1.5rem; border: 1px solid rgba(255, 255, 255, 0.05); }
        h2 { color: #60a5fa; margin-top: 2.5rem; border-left: 4px solid #a855f7; padding-left: 1rem; }
        h3 { color: #f472b6; margin-top: 2rem; }
        p { color: #cbd5e1; font-size: 1.15rem; margin-bottom: 1.5rem; }
        ul { color: #94a3b8; margin-bottom: 1.5rem; }
        li { margin-bottom: 0.75rem; }
        .cta-box { background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border: 1px solid #60a5fa; padding: 2rem; border-radius: 1rem; margin-top: 3rem; text-align: center; }
        .cta-button { background: #60a5fa; color: #0f172a; padding: 1rem 2.5rem; border-radius: 99px; text-decoration: none; font-weight: bold; display: inline-block; font-size: 1.2rem; transition: transform 0.2s; }
        .cta-button:hover { transform: scale(1.05); }
        .interlinks { margin-top: 4rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1); }
        .interlinks h4 { color: #94a3b8; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.9rem; margin-bottom: 1rem; }
        .interlinks ul { list-style: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; }
        .interlinks a { color: #60a5fa; text-decoration: none; font-size: 1rem; }
        .interlinks a:hover { text-decoration: underline; }
        footer { margin-top: 4rem; text-align: center; color: #64748b; font-size: 0.9rem; padding-bottom: 2rem; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <p><a href="../index.html" style="color: #60a5fa; text-decoration: none;">&larr; Back to Main Site</a></p>
            <h1>${title}</h1>
        </header>
        
        <article class="content">
            ${content}
            
            <div class="cta-box">
                <h3>Need professional help with your home services?</h3>
                <p>Gary Pearce provides expert installation across the North East. From 8K CCTV to WiFi 7 mesh networks.</p>
                <a href="tel:${PHONE.replace(/ /g, '')}" class="cta-button">Call Gary: ${PHONE}</a>
            </div>
            
            <div class="interlinks">
                <h4>Related Industry Insights</h4>
                <ul>
                    ${interlinks.map(link => `<li><a href="${link.url}">${link.title}</a></li>`).join('')}
                    <li><a href="${SITE_URL}">Main Website</a></li>
                    <li><a href="https://gazpearcecctv.postach.io/">Expert Security Blog</a></li>
                </ul>
            </div>
        </article>
        
        <footer>
            &copy; 2026 Gary Pearce Home Services. Professional Security & Connectivity Solutions.
        </footer>
    </div>
</body>
</html>`;

const categories = [
    { name: 'CCTV & Surveillance', prefix: 'The Future of CCTV:' },
    { name: 'WiFi & Networking', prefix: 'Connectivity Guide:' },
    { name: 'Home Security', prefix: 'Protecting Your Home:' },
    { name: 'Audio Visual', prefix: 'AV Installation:' },
    { name: 'Data Cabling', prefix: 'Structured Cabling:' }
];

const topics = [
    "AI-Driven Motion Detection in 2026",
    "WiFi 7 Mesh Systems vs Traditional Access Points",
    "Why 8K CCTV is Now the Standard for Evidence",
    "CAT7 Cabling: Is it Overkill for Home Use?",
    "Smart Lock Integration with Existing Alarm Systems",
    "The Rise of Forensic-Grade Night Vision Cameras",
    "Starlink Installation: Best Practices for Rural Areas",
    "TV Wall Mounting: Cable Management Masterclass",
    "Outdoor WiFi: Extending Your Network to the Garden",
    "Hidden Security: Discreed Camera Placement Tips",
    "Securing Your Home Office Network for Remote Work",
    "Cloud Storage vs Local NVR: The Great Debate",
    "PoE Lighting and Security Integration",
    "Testing Your Alarm System: A 10-Point Checklist",
    "Upgrading Legacy Analog CCTV to IP Systems",
    "The Importance of UPS for Security Systems",
    "Thermal Imaging Cameras for Residential Use",
    "Smart Intercoms: Seeing Who's at the Door from Anywhere",
    "Cybersecurity for Your IoT Home Devices",
    "Multi-Room Audio Setup Guide"
];

const articles = [];
for (let i = 1; i <= 100; i++) {
    const category = categories[Math.floor(Math.random() * categories.length)];
    const baseTopic = topics[Math.floor(Math.random() * topics.length)];
    const title = `${category.prefix} ${baseTopic} (Part ${Math.ceil(i/5)})`;
    const slug = title.toLowerCase().replace(/[^a-z0-9]/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '');
    
    articles.push({ title, slug, category: category.name });
}

// Generate the files
articles.forEach((article, index) => {
    // Pick 3 random interlinks from other articles
    const otherArticles = articles.filter((_, i) => i !== index);
    const selectedInterlinks = [];
    for (let j = 0; j < 3; j++) {
        const randomArt = otherArticles[Math.floor(Math.random() * otherArticles.length)];
        selectedInterlinks.push({ title: randomArt.title, url: `${randomArt.slug}.html` });
    }

    const content = `
        <h2>Executive Summary</h2>
        <p>In this comprehensive guide, we explore the intricate details of <strong>${article.title}</strong> and how it impacts modern security and connectivity in 2026. As technology evolves, staying ahead of the curve is essential for both home and business owners.</p>
        
        <h2>Key Technical Specifications</h2>
        <p>When considering ${article.category} solutions, several factors come into play. We prioritize performance, reliability, and long-term viability.</p>
        <ul>
            <li><strong>Next-Gen Processing:</strong> Utilizing the latest chips for real-time analytics.</li>
            <li><strong>Ultra-High Bandwidth:</strong> Ensuring zero lag in data transmission.</li>
            <li><strong>Military-Grade Encryption:</strong> Keeping your private data secure.</li>
            <li><strong>Sustainable Design:</strong> Low-power consumption for 24/7 operation.</li>
        </ul>
        
        <h2>Implementation Challenges</h2>
        <p>Setting up <strong>${article.title}</strong> isn't just about plugging things in. It requires professional planning and execution to avoid common pitfalls like signal interference or dead zones.</p>
        
        <h2>Localized Expertise</h2>
        <p>For residents in the North East, including areas like Newcastle, Sunderland, and Durham, local environment factors can affect signal strength and hardware durability. Gary Pearce specializes in adapting these global technologies to local conditions.</p>
    `;

    const html = template(article.title, content, article.slug, selectedInterlinks);
    fs.writeFileSync(path.join(BLOG_DIR, `${article.slug}.html`), html);
});

console.log(`Successfully generated 100 blog posts in ${BLOG_DIR}`);
