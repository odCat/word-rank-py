#!python

#   Copyright 2021 Mihai Gătejescu
# 
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from sys import exit as sysexit
from sys import argv
from re import sub

def read_from_file(file_name):
    try:
        input_file =  open(file_name, 'r', encoding='utf8')
        data = input_file.read()
        input_file.close()
        return data
    except FileNotFoundError:
        print('File not found')
        sysexit()

def remove_punctuation(text):
    punctuation = ',.?!\"\'‘’“”()[]{}<>\\/;:_+@#$%^&*~`=|'
            
    text = text.replace('-\n', '')
    text = text.replace('- ', ' ')
    text = text.replace(' -', ' ')
    for c in text:
        if c in punctuation:
            text = text.replace(c, '')

    return text

def text_to_list(text):
    text = remove_punctuation(text)
    text = text.replace('\n', ' ')
    text = text.strip()
    text = sub(' +', ' ', text)
    return text.split(' ')

def sort_dictionary(dictionary):
    values = sorted(dictionary.values(), reverse = True)
    sorted_dict = {}
    for i in values:
        for j in dictionary.keys():
            if dictionary[j] == i:
                sorted_dict[j] = i
    return sorted_dict

def word_frequency(data):
    result = {}
    for word in data:
        try:
            result[word] += 1
        except KeyError:
            result[word] = 1
    return sort_dictionary(result)

def make_printable(dictionary):
    result = ''
    for i in dictionary.keys():
        result += i + ': ' + str(dictionary[i]) + '\n'
    return result

if __name__ == '__main__':
    if len(argv) > 1:
        file_name = argv[1]
    else:
        file_name = 'sample.txt'
    data = read_from_file(file_name)
    data = remove_punctuation(data)
    data = text_to_list(data)
    data = word_frequency(data)
    data = make_printable(data)
    if len(argv) == 3:
        with open(argv[2], 'w', encoding = 'utf-8') as out_file:
            out_file.write(data)
    else:
        print(data)

#TODO
## Print to output in chuncks
## When redirecting the output to a file, it gets and unicode error
