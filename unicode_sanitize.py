def scan_zero_space(file_in, file_out):
    lines = list()
    try:
        with open(file_in, 'r') as f:
            for line in f:
                lines.append(line.replace(u'\u200b', ''))
        with open(file_out, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line)
    except FileNotFoundError:
        print('could not open ', file_in)

def clean_all_non_ascii(file_in, file_out):
    lines = list()
    try:
        with open(file_in, 'r') as f:
            for line in f:  #oooh, pythonic!
                good_chars = filter(lambda char: ord(char) <= 255, line)
                lines.append(''.join(good_chars))
        with open(file_out, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line)
    except FileNotFoundError:
        print('could not open ' + file_in)

def main():
    from sys import argv
    argc = len(argv)
    if argc < 2:
        print('Usage: ' + argv[0] + ' <in filename> [out filename] -all')
        print('all\t: clean all non-ascii')
        return -1

    file_in     = argv[1]
    file_out    = argv[1] if argc < 3 else argv[2]

    if argv[argc - 1] == '-all':
        clean_all_non_ascii(file_in, file_out)
    else:
        scan_zero_space(file_in, file_out)
    return 0

if __name__ == '__main__':
    main()
