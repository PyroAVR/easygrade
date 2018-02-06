def scan_for_comments(f):
    accepting = False
    size = 0
    block_lengths_list = list()
    for line in f:   #this is bound to be gross
        if '/*' in line:
            accepting = True
            continue
        if '*/' in line:
            accepting = False
            block_lengths_list.append(size)
            size = 0
        if accepting == True:
            size += 1
    return block_lengths_list



def main():
    from sys import argv
    argc = len(argv)
    if argc < 2:
        print('Usage: ' + argv[0] + ' filename')
        return -1
    with open(argv[1]) as f:
        blocks = scan_for_comments(f)
        for block in blocks:
            print('found comment block with length:' + str(block))
    return 0

if __name__ == '__main__':
    main()
