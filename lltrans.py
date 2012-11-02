from  argparse import ArgumentParser
import sys

src = """#include <stdio.h>

int main(void)
{
    printf("LinkedList NYC\\n");
    return 0;
}
"""

def learn_language(input_line):
    pass

parser = ArgumentParser(description="An anything-to-C translator with some caveats")
parser.add_argument('-i', '--input', help="Source file to translate (defaults to stdin)")
parser.add_argument('-o', '--output', help="Output C file (defaults to lltrans.c)")
args = parser.parse_args()

infile = open(args.input, "r") if args.input else sys.stdin

outfile_name = args.output if args.output else "lltrans.c"
outfile = open(outfile_name, "w")

for line in infile:
    learn_language(line)

outfile.write(src)

infile.close()
outfile.close()
