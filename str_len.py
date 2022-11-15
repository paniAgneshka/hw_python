import argparse
import textwrap as tw
parser = argparse.ArgumentParser(description='Text file name')

parser.add_argument('file_name', type=str, help='Input file name')

args = parser.parse_args()
t = open(args.file_name, 'r')

f = open('new_text.txt', 'w')
for line in t.readlines():
    if len(line) > 90:
        lststr = tw.wrap(text=line, width=70)
        for s in lststr:
            f.write(s + "\n")
    else:
        f.write(line + "\n")
t.close()
f.close()
