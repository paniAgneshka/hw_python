import argparse
import textwrap as tw
parser = argparse.ArgumentParser(description='Text file name')

parser.add_argument('file_name', type=str, help='Input file name')

args =parser.parse_args()
t = open(args.file_name, 'r')
value=t.read()
for line in t.readlines():
    if len(line) > 90:
        f=open('new_text.txt', 'w')
        f.write(tw.wrap(text=value, width= 70))
        break
