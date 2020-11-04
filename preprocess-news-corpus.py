import os
import argparse

from preprocessor import Preprocessor, Language
p = Preprocessor(Language.vietnamese)

def read_large_file(file_handler, block_size=14470):
    # 7690 × 14470 = 111,274,300
    block = []
    for line in file_handler:
        block.append(line)
        if len(block) == block_size:
            yield block
            block = []
    
    #yield the last block
    if block:
        yield block

def get_output_name(count):
    zeros = ['', '0', '00', '000'][(len(str(count)) <= 3) + (len(str(count)) <= 2) + (len(str(count)) <= 1)]
    output_name = zeros + str(count) + r'.txt'
    return output_name

def run(args):
    input_file = os.path.join(args.inp, 'corpus-full.txt')
    if not os.path.exists(args.out):
        os.mkdir(args.out)
    with open(input_file, 'r+', encoding='utf-8') as file_handler:
        count = 0
        for block in read_large_file(file_handler):
            output_name = get_output_name(count)
            output_file = open(os.path.join(args.out, output_name), 'w+', encoding='utf-8')
            # lines = p.preprocess_list([line for line in block])
            output_file.write("".join([line for line in block]))
            output_file.close()
            print(count)
            count += 1
        print('Done!')

        # p.preprocess_files(args.out, args.out, {'overwrite': True})

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inp', type=str)
    parser.add_argument('out', type=str)
    args = parser.parse_args()
    run(args)