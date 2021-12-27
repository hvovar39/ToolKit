#!/bin/python3

"""Get morse code from the length of the word of the given .txt"""

import argparse
from os import sep
from typing import DefaultDict

def init_arg_parser() :
    '''Initialize and return the argument parser.'''
    parser = argparse.ArgumentParser(
        description='Get morse code from the length of the word of the given .txt'
        )
    parser.add_argument('source_txt',
        help = 'The source .txt file.')
    parser.add_argument('-s',
        nargs = '+',
        default = ['.', ','],
        help = 'Word separator (default is "," and ".").')
    parser.add_argument('-d',
        type = int,
        default = 5,
        help = 'The word size under wich a word is consider a dot (default is 5).')
    return parser

def cut(line, separators):
    words = list()
    for word in line :
        word_list = word.split(separators[0])
        if word_list[-1] == '' :
            word_list = word_list[:-1]
        for word in word_list :
            words.append(word.strip('\n '))
    
    if len(separators) == 1 :
        return words
    else :
        return cut(words, separators[1:])


def treat_line (words, dot_size):
    morse_code = ''
    for elt in words :
        word = elt.split(' ')
        for letter in word :
            if len(letter) < dot_size :
                morse_code += '.'
            else :
                morse_code += '-'
        morse_code += ' '
    return morse_code+'/ '

def main():
    parser = init_arg_parser()
    args = parser.parse_args()
    res = ''

    with open(args.source_txt, 'r') as source:
        line = 'initialization'
        while line != '' :
            line = source.readline()
            if line != '\n' :
                res += treat_line(cut([line.strip('\n ')], args.s), args.d)
    
    print (res)

if __name__ == '__main__':
    main()