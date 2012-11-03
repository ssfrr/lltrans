lltrans : An anything-to-C translator
=====================================

Built on decades of machine learning and AI research, lltrans is an
advanced new tool capable of translating any program [1] into highly
efficient, portable C code. lltrans reads any given file (or stdin), and
intelligently learns and parses the input language, generating an
equivalent C program.

    usage: lltrans.py [-h] [-i INPUT] [-o OUTPUT]

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            Source file to translate (defaults to stdin)
      -o OUTPUT, --output OUTPUT
                            Output C file (defaults to lltrans.c)

[1] caveat - currently lltrans only works for programs that print
"LinkedList NYC" to stdout
