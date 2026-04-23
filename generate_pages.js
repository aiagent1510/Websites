const fs = require('fs');
const path = require('path');

const template = (service, location, phone) => `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expert ${service} ${location} | Gary Pearce Home Services</title>
    <meta name="description" content="Professional ${service} and installation in ${location}. Gary Pearce provides reliable, high-quality solutions for homes and businesses. Call ${phone}.">
    <meta name="keywords" content="${service} ${location}, ${service} installation ${location}, Gary Pearce ${service}, professional ${service} ${location}">
    <style>
        body { font-family: 'Inter', sans-serif; background: #0f172a; color: white; margin: 0; line-height: 1.6; }
        .container { max-width: 800px; margin: 0 auto; padding: 2rem; }
        .card { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); padding: 3rem; border-radius: 1.5rem; border: 1px solid rgba(255, 255, 255, 0.1); margin-top: 2rem; }
        h1 { background: linear-gradient(to right, #60a5fa, #a855f7); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.5rem; margin-bottom: 1rem; }
        h2 { color: #60a5fa; margin-top: 2rem; }
        p { color: #94a3b8; font-size: 1.1rem; }
        .cta { background: #60a5fa; color: #0f172a; padding: 1rem 2rem; border-radius: 99px; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 1.5rem; }
        .faq { margin-top: 3rem; }
        .faq-item { margin-bottom: 1.5rem; }
        .faq-question { font-weight: bold; color: #a855f7; }
        ul { color: #94a3b8; }
        li { margin-bottom: 0.5rem; }
    </style>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "${service} in ${location}",
      "description": "Expert ${service} in ${location} by Gary Pearce. Reliability and quality for your peace of mind.",
      "url": "https://aiagent1510.github.io/Websites/${service.toLowerCase().replace(/ /g, '-')}-${location.toLowerCase()}.html",
      "mainEntity": {
        "@type": "Service",
        "serviceType": "${service}",
        "provider": {
          "@type": "LocalBusiness",
          "name": "Gary Pearce Home Services",
          "telephone": "${phone}"
        },
        "areaServed": {
          "@type": "City",
          "name": "${location}"
        }
      }
    }
    </script>
</head>
<body>
    <div class="container">
        <div class="card">
            <h1>${service} ${location}</h1>
            <p>Reliable, professional ${service} solutions for your home or business in the ${location} area.</p>
            
            <h2>Why Choose Gary Pearce for ${service} in ${location}?</h2>
            <p>Gary Pearce offers expert ${service} services tailored to your specific needs. We focus on quality, reliability, and customer satisfaction in every project we undertake in ${location}.</p>
            
            <p>Our ${location} services include:</p>
            <ul>
                <li>Professional ${service} design and planning</li>
                <li>High-quality materials and components</li>
                <li>Expert installation and testing</li>
                <li>Ongoing support and maintenance</li>
            </ul>

            <a href="tel:${phone.replace(/ /g, '')}" class="cta">Call Gary: ${phone}</a>

            <div class="faq">
                <h2>Common Questions about ${service} in ${location}</h2>
                <div class="faq-item">
                    <p class="faq-question">What areas in ${location} do you cover?</p>
                    <p>We cover all parts of ${location} and the surrounding areas, providing prompt and professional service.</p>
                </div>
                <div class="faq-item">
                    <p class="faq-question">How can I get a quote?</p>
                    <p>You can call Gary directly at ${phone} for a free, no-obligation quote or consultation.</p>
                </div>
            </div>
        </div>
        <p style="text-align:center; margin-top: 2rem;"><a href="index.html" style="color: #94a3b8; text-decoration: none;">&larr; Back to Home</a></p>
    </div>
</body>
</html>`;

const pages = [
    { service: 'CCTV Cabling', location: 'Manchester', file: 'cctv-cabling-manchester.html' },
    { service: 'CCTV Cabling', location: 'Leeds', file: 'cctv-cabling-leeds.html' },
    { service: 'CCTV Cabling', location: 'York', file: 'cctv-cabling-york.html' },
    { service: 'Alarm Services', location: 'Manchester', file: 'alarm-services-manchester.html' },
    { service: 'Alarm Services', location: 'Leeds', file: 'alarm-services-leeds.html' },
    { service: 'Alarm Services', location: 'York', file: 'alarm-services-york.html' },
    { service: 'Data Cabling', location: 'Manchester', file: 'data-cabling-manchester.html' },
    { service: 'Data Cabling', location: 'Leeds', file: 'data-cabling-leeds.html' },
    { service: 'Data Cabling', location: 'York', file: 'data-cabling-york.html' },
    { service: 'TV Aerials', location: 'Leeds', file: 'tv-aerials-leeds.html' },
    { service: 'TV Aerials', location: 'York', file: 'tv-aerials-york.html' }
];

const phone = '07830638337';

pages.forEach(page => {
    const content = template(page.service, page.location, phone);
    fs.writeFileSync(page.file, content);
    console.log(`Generated ${page.file}`);
});
