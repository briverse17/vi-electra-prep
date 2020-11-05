import os
import argparse

from preprocessor import Preprocessor, Language
p = Preprocessor(Language.vietnamese)

def read_large_file(file_handler, block_size=1000):
    # 1000 × 4233 + 198 = 4,233,198
    block = []
    for line in file_handler:
        if len(line) == 0:
            continue
        block.append(line)
        if len(block) == block_size:
            yield block
            block = []
    
    #yield the last block
    if block:
        yield block

def run(args):
    with open(args.inp, 'r+', encoding='utf-8') as file_handler:
        count = 0
        f_out = open(args.out, 'w+', encoding='utf-8')
        for block in read_large_file(file_handler):
            try:
                block = p.preprocess_list(block)
            except:
                print("Error in block %d. Processing each sentence" % count)
                block1 = []
                for line in block:
                    try:
                        line = p.preprocess(line)
                        block1.append(line)
                    except:
                        # If encountered error, eliminate the whole line
                        print('Error: %s (%d characters)' % (line, len(line)))
                block = block1
            # f_out.write('\n'.join(p.preprocess_list(block)))
            f_out.write('\n'.join(block))
            print(count)
            count += 1
        f_out.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inp', type=str)
    parser.add_argument('out', type=str)
    args = parser.parse_args()
    run(args)
