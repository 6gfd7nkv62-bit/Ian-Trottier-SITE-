import pathlib
p=pathlib.Path("about.html"); s=p.read_text()
fig=pathlib.Path("/opt/data/fig2.html").read_text()
anchor="</figcaption></figure>"
print("anchor found:", s.count(anchor))
s=s.replace(anchor, anchor+fig, 1)
p.write_text(s)
print("added:", "ian-about.jpg" in s)
