const fs = require('fs');
const path = require('path');

const BLOG_DIR = path.join(__dirname, 'blog');
const files = fs.readdirSync(BLOG_DIR).filter(f => f.endsWith('.html') && f !== 'index.html');

const items = files.map(file => {
    const title = file.replace(/-/g, ' ').replace('.html', '').replace(/\b\w/g, l => l.toUpperCase());
    return `<li><a href="${file}">${title}</a></li>`;
}).join('\n');

const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expert Home Services Blog | Gary Pearce</title>
    <style>
        body { font-family: 'Inter', sans-serif; background: #0f172a; color: white; margin: 0; line-height: 1.6; }
        .container { max-width: 1000px; margin: 0 auto; padding: 4rem 2rem; }
        h1 { background: linear-gradient(to right, #f59e0b, #d97706); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 4rem; text-align: center; margin-bottom: 4rem; }
        ul { list-style: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; }
        li { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 1.5rem; transition: 0.3s; }
        li:hover { transform: translateY(-5px); border-color: #f59e0b; background: rgba(255, 158, 11, 0.05); }
        a { color: white; text-decoration: none; font-weight: 600; display: block; height: 100%; }
        p { text-align: center; margin-top: 4rem; }
        .back { color: #f59e0b; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <p><a href="../index.html" class="back">&larr; Back to Main Site</a></p>
        <h1>Security & Connectivity Insights</h1>
        <ul>
            ${items}
        </ul>
    </div>
</body>
</html>`;

fs.writeFileSync(path.join(BLOG_DIR, 'index.html'), html);
console.log('Blog index generated successfully.');
