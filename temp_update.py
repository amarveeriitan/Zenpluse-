import re

with open('c:/PAGE/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
css_old = """        :root {
            --neon-green: #00ffa3;
            --deep-navy: #0a0e1c;
            --glass-bg: rgba(30, 41, 59, 0.4);
            --glass-border: rgba(255, 255, 255, 0.1);
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--deep-navy);
            color: #ffffff;
            overflow-x: hidden;
            background: radial-gradient(circle at top right, #1e293b, #0a0e1c 60%);
        }

        h1, h2, h3, .font-heading {
            font-family: 'Outfit', sans-serif;
        }

        .glass-card {
            background: var(--glass-bg);
            backdrop-filter: blur(16px);
            border: 1px solid var(--glass-border);
            border-radius: 28px;
            transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
            position: relative;
            overflow: hidden;
        }

        .glass-card::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, transparent 100%);
            pointer-events: none;
        }

        .glass-card:hover {
            transform: translateY(-8px);
            border-color: rgba(0, 255, 163, 0.4);
            background: rgba(30, 41, 59, 0.6);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), 0 0 20px rgba(0, 255, 163, 0.1);
        }

        .neon-text { color: var(--neon-green); text-shadow: 0 0 10px rgba(0, 255, 163, 0.3); }
        .neon-bg { 
            background: linear-gradient(135deg, #00ffa3 0%, #00d186 100%); 
            color: #000; 
            box-shadow: 0 4px 15px rgba(0, 255, 163, 0.3);
        }

        .progress-dash {
            height: 4px;
            border-radius: 2px;
            flex: 1;
            margin: 0 4px;
            background: #1e293b;
        }

        .progress-dash.active { background: #00ffa3; }

        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }

        @keyframes slideUp {
            from { transform: translateY(100%); }
            to { transform: translateY(0); }
        }

        .cart-animation { animation: slideUp 0.4s cubic-bezier(0.4, 0, 0.2, 1); }

        .product-image {
            background: #111827;
            border-radius: 20px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid rgba(255,255,255,0.05);
        }

        .product-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.6s cubic-bezier(0.23, 1, 0.32, 1);
        }

        .glass-card:hover .product-image img {
            transform: scale(1.1);
        }

        .badge {
            font-size: 10px;
            font-weight: 800;
            padding: 5px 12px;
            border-radius: 99px;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            backdrop-filter: blur(4px);
        }

        .cat-btn { transition: all 0.2s ease; }
        .cat-btn.active {
            background-color: #00ffa3;
            color: #000;
            border-color: #00ffa3;
        }

        .goal-pill {
            transition: all 0.3s ease;
            cursor: pointer;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .goal-pill.active {
            background: rgba(0, 255, 163, 0.1);
            border-color: #00ffa3;
            color: #00ffa3;
        }"""

css_new = """        :root {
            --primary-blue: #0d6efd;
            --primary-gradient: linear-gradient(90deg, #0d6efd, #6610f2);
            --bg-light: #f8fafc;
            --text-dark: #2d3748;
            --card-bg: #ffffff;
            --card-border: rgba(0, 0, 0, 0.05);
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #f8fafc, #eef2f7);
            color: var(--text-dark);
            overflow-x: hidden;
        }

        h1, h2, h3, .font-heading {
            font-family: 'Outfit', sans-serif;
        }

        .glass-card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 20px;
            transition: all 0.3s cubic-bezier(0.23, 1, 0.32, 1);
            position: relative;
            overflow: hidden;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.04);
        }

        .glass-card:hover {
            transform: translateY(-5px);
            border-color: rgba(13, 110, 253, 0.2);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08), 0 0 15px rgba(13, 110, 253, 0.05);
        }

        .neon-text { color: var(--primary-blue); }
        .neon-bg { 
            background: var(--primary-gradient); 
            color: #fff; 
            box-shadow: 0 4px 15px rgba(13, 110, 253, 0.3);
        }

        .progress-dash {
            height: 4px;
            border-radius: 2px;
            flex: 1;
            margin: 0 4px;
            background: #e2e8f0;
        }

        .progress-dash.active { background: var(--primary-gradient); }

        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }

        @keyframes slideUp {
            from { transform: translateY(100%); }
            to { transform: translateY(0); }
        }

        .cart-animation { animation: slideUp 0.4s cubic-bezier(0.4, 0, 0.2, 1); }

        .product-image {
            background: #f1f5f9;
            border-radius: 16px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid var(--card-border);
        }

        .product-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.6s cubic-bezier(0.23, 1, 0.32, 1);
        }

        .glass-card:hover .product-image img {
            transform: scale(1.08);
        }

        .badge {
            font-size: 10px;
            font-weight: 800;
            padding: 5px 12px;
            border-radius: 99px;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            background: #ffffff;
            color: var(--text-dark);
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .cat-btn { transition: all 0.2s ease; }
        .cat-btn.active {
            background: var(--primary-blue);
            color: #fff;
            border-color: var(--primary-blue);
        }

        .goal-pill {
            transition: all 0.3s ease;
            cursor: pointer;
            border: 1px solid #e2e8f0;
            background: #ffffff;
            color: #64748b;
        }
        .goal-pill.active {
            background: rgba(13, 110, 253, 0.1);
            border-color: var(--primary-blue);
            color: var(--primary-blue);
        }"""
content = content.replace(css_old, css_new)

# Replacements
replacements = {
    'bg-[#0a0e1c]/90': 'bg-white/90',
    'bg-slate-800/50': 'bg-white',
    'bg-slate-800/80': 'bg-white',
    'border-slate-700': 'border-slate-200',
    'text-[#00ffa3]': 'text-[#0d6efd]',
    'bg-[#00ffa3]': 'bg-[#0d6efd]',
    'text-slate-400': 'text-slate-500',
    'text-slate-500': 'text-slate-400',
    'text-slate-300': 'text-slate-600',
    'text-slate-100': 'text-slate-800',
    'text-white': 'text-slate-800',
    'bg-slate-700': 'bg-slate-200',
    'bg-slate-600': 'bg-slate-300',
    'bg-[#111827]': 'bg-white',
    'bg-slate-800': 'bg-slate-100',
    'bg-slate-800/30': 'bg-slate-50',
    'border-slate-700/50': 'border-slate-200',
    'bg-black/60': 'bg-slate-900/40',
    'bg-black/80': 'bg-slate-900/60',
    'shadow-[0_-20px_50px_rgba(0,0,0,0.5)]': 'shadow-[0_-20px_50px_rgba(0,0,0,0.1)]',
    'border-t border-slate-800': 'border-t border-slate-200',
    'border border-[#00ffa3]/20 hover:bg-[#00ffa3]/20': 'border border-blue-500/20 hover:bg-blue-500/10',
    'bg-[#00ffa3]/10': 'bg-blue-500/10',
    'text-[#00ffa3]': 'text-blue-600',
    'text-[#00ffa3] font-bold': 'text-[#0d6efd] font-bold',
    'bg-[#0a0e1c]': 'bg-[#f8fafc]',
    'bg-[#1e293b]': 'bg-white',
    'stroke="black"': 'stroke="white"',
    'text-black': 'text-white'
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Special fixes
content = content.replace('text-slate-800 font-bold px-2 py-1', 'text-white font-bold px-2 py-1')
content = content.replace('class="absolute top-4 right-4 z-10 p-2 bg-black/50 backdrop-blur-md rounded-full text-slate-800 hover:bg-black/80 transition"', 'class="absolute top-4 right-4 z-10 p-2 bg-white/80 backdrop-blur-md rounded-full text-slate-800 hover:bg-white transition"')
content = content.replace('<h1 class="text-3xl font-bold mb-1">Zen Shop <span id="goalIcon">🔥</span></h1>', '<h1 class="text-3xl font-bold mb-1 brand-logo inline-block" style="background: linear-gradient(90deg, #0d6efd, #6610f2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Zen Shop <span id="goalIcon" style="-webkit-text-fill-color: initial;">🔥</span></h1>')
content = content.replace("dash.classList.add('bg-[#0d6efd]');", "dash.style.background = 'var(--primary-gradient)';")

with open('c:/PAGE/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")
