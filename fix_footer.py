with open("realisations.html", "r") as f:
    r_html = f.read()

footer_start = r_html.find('<footer')
footer_end = r_html.find('</html>') + 7

footer_html = r_html[footer_start:footer_end]

with open("index.html", "r") as f:
    html = f.read()

# Add </main> and footer
if not html.endswith('</html>'):
    html = html + "\n  </main>\n\n  " + footer_html
    with open("index.html", "w") as f:
        f.write(html)
    print("Fixed footer on index.html")
