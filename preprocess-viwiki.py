import os
import re
import argparse

from preprocessor import *
p = Preprocessor(Language.vietnamese)

def run(args):
    # data path
    input_path = os.path.join(args.inp, 'viwiki')
    output_path = os.path.join(args.out, 'viwiki')
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    # file names list
    file_names = os.listdir(input_path)

    count = 0
    for fname in file_names:
        input_dir = os.path.join(input_path, fname)
        input_file = open(input_dir, 'r+', encoding='utf-8')
        output_dir = os.path.join(output_path, fname)
        output_file = open(output_dir, 'w+', encoding='utf-8')

        lines = input_file.read().splitlines()
        for line in lines:
            if len(line) == 0:
                continue
            m = re.fullmatch(r'^=.*=$', line)
            if m:
                line = line.split()[1:-1]
                line = ' '.join(line)
            try:
                line = p.preprocess(line)
            except:
                print('File:', fname)
                print(' Error:', line)
            output_file.write(line + '\n')

        input_file.close()
        output_file.close()

        count += 1
        if (len(file_names) / count) % 10 == 0:
            print('%d/%d'%(count, len(file_names)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inp', type=str)
    parser.add_argument('out', type=str)
    args = parser.parse_args()
    run(args)
