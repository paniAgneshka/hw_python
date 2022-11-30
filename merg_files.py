from pathlib import Path

outpath = input()
if not outpath.strip():
    outpath = "."
with open("result.txt", "w") as out:
    for path in Path(outpath).glob("*.txt"):
        out.write(path.name + "\n" + path.read_text() + "\n")
    
