# python script for ToolFactory tool to regularise a tabular file
# finds the longest line and pads all others to the same length with an optional string or blank
# ross lazarus in response to
# https://matrix.to/#/!IEcbSOGXlqPpSmwmPp:gitter.im/$kMtqMiDfGEZ-apT6Wnv5FFe2Np07Ga19pQxXL7xR8n0?via=gitter.im&via=matrix.org&via=sys.reslate.net

import argparse
import sys


parser = argparse.ArgumentParser()
a = parser.add_argument
a('--input_tab', required=True)
a('--header', default='')
a('--delim', default='\t')
a('--fillstring', default='')
a('--output_tab', required= True)
a('--remove_empty_rows', action='store_true')
args = parser.parse_args()
d  = open(args.input_tab, 'r').read()
d = d.split('\n')
if args.remove_empty_rows:
    d = [x for x in d if args.delim in x]
d = [x.split(args.delim) for x in d]
lens = [len(x) for x in d]
print('lens=',lens)
maxlen = max(lens)
minlen = min(lens)
if maxlen == 1:
    print('### possible input error - no tabs found - is this really a tab delimited input file?')
    sys.exit(2)
print(f'##torectangular_tab_tool processing infile {args.input_tab} found lines with max {maxlen} and min {minlen} fields')
if minlen == maxlen:
    print(f'## all rows of {args.input_tab} are the same {maxlen} length - output is identical to input!')
else:
    for i, row in enumerate(d):
        l = lens[i]
        if l < maxlen:
            if l > 1:
                fill = [args.fillstring for x in range(maxlen - l)]
                d[i] = row + fill
            else:
                fill = [args.fillstring for x in range(maxlen)]
                d[i] = fill
outf = open(args.output_tab, 'w')
d = [args.delim.join(x) for x in d]
outf.write('\n'.join(d))
outf.write('\n')
outf.close()
