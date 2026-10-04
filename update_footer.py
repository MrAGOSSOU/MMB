import os

# 1. Update index.html
with open("index.html", "r") as f:
    html = f.read()

# Replace <a href="/" class="logo" style="font-size: 2rem;">MMB.</a>
logo_html = '<a href="/" class="logo" style="display:inline-block; max-width:250px;"><img src="Image/logo_mmb_footer.jpg" alt="MMB Logo" style="width: 100%; height: auto; object-fit: contain;"></a>'

html = html.replace('<a href="/" class="logo" style="font-size: 2rem;">MMB.</a>', logo_html)

with open("index.html", "w") as f:
    f.write(html)

# 2. Update css/style.css
with open("css/style.css", "r") as f:
    css = f.read()

# Replace footer background
css = css.replace('background: var(--c-charbon-dark);', 'background: #000000;')

# Change hover color of footer links to gold
css = css.replace('.f-links a:hover {\n  opacity: 1;\n}', '.f-links a:hover {\n  opacity: 1;\n  color: #c79e61;\n}')

# Optional: Add a subtle gold top border to the footer
css = css.replace('.footer {\n  background: #000000;\n  padding: 5rem var(--px) 2rem;\n}', '.footer {\n  background: #000000;\n  padding: 5rem var(--px) 2rem;\n  border-top: 2px solid #c79e61;\n}')

with open("css/style.css", "w") as f:
    f.write(css)

print("Footer updated successfully.")
