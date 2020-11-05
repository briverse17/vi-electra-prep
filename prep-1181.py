import os
import argparse

from preprocessor import Preprocessor, Language
p = Preprocessor(Language.vietnamese)

def run(args):
    with open(args.inp, 'r+', encoding='utf-8') as f_in:
        f_out = open(args.out, 'w+', encoding='utf-8')
        lines = f_in.read().splitlines()
        for line in lines:
            try:
                line = p.preprocess(line)
                f_out.write(line + '\n')
            except:
                # If encounter error, eliminate the whole line
                print('Error: %s (%d characters)' % (line, len(line)))
        f_out.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inp', type=str)
    parser.add_argument('out', type=str)
    args = parser.parse_args()
    run(args)
