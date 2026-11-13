import pathlib
p=pathlib.Path("index.html"); s=p.read_text()
new=pathlib.Path("/opt/data/bookp.html").read_text()
i=s.find("Published by Bombardier Books")
j=s.rfind("<p>", 0, i)
k=s.find("</p>", i)+4
print("replace span:", j, k)
print("old:", s[j:j+60])
s=s[:j]+new+s[k:]
p.write_text(s)
print("new in:", "paper trail behind it" in s)
