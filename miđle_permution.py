def middle_permutation(string):
    chr_list = []
    for chr in string:
        chr_list.append(chr)
    chr_list.sort()
    if len(chr_list) %2 == 0:
        mid_chr = chr_list[int(len(chr_list)/2) - 1]
        chr_list.remove(mid_chr)
        chr_list.reverse()
        return mid_chr + ''.join(chr_list)
    else:
        mid_chr = chr_list[int(len(chr_list)/2)]
        chr_list.remove(mid_chr)
        return mid_chr + middle_permutation(''.join(chr_list))