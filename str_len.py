import argparse
import textwrap as tw
parser = argparse.ArgumentParser(description='Text file name')

parser.add_argument('file_name', type=str, help='Input file name')

args =parser.parse_args()
t = open(args.file_name, 'r')
value=t.read()
for line in value:
    if len(line) > 90:
        print(len(line))
        with open('new_text.txt', 'w') as file:
            wrapper=tw.wrap(text=value, width= 70)
            print(wrapper)
        
