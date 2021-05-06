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

from sys import exit as sys_exit
from sys import argv
from re import sub


def read_from_file(file_name):
    try:
        input_file = open(file_name, 'r', encoding='utf8')
        text = input_file.read()
        input_file.close()
        return text
    except FileNotFoundError:
        print('File not found')
        sys_exit()


def remove_empty_lines(text):
    text = sub(' +\n', '\n', text)
    text = sub('\n+', '\n', text)
    if text[0] == '\n':
        text = text[1:]
    return text


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
    values = sorted(dictionary.values(), reverse=True)
    result = {}
    for i in values:
        for j in dictionary.keys():
            if dictionary[j] == i:
                result[j] = i
    return result


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


def print_to_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as out_file:
        out_file.write(data)


def print_utf8(data):
    utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
    print(data, file=utf8stdout)


def select_file():
    if len(argv) > 1:
        return argv[1]
    else:
        return 'sample.txt'


def exit_if_there_is_no_data(text_data):
    if text_data == '':
        print('The string is empty')
        sys_exit()


def print_to_output(text_data):
    if len(argv) == 3:
        print_to_file(argv[2], text_data)
    else:
        print_utf8(text_data)


def process_data(text_data):
    text_data = remove_punctuation(text_data)
    text_data = text_to_list(text_data)
    text_data = word_frequency(text_data)
    return make_printable(text_data)


if __name__ == '__main__':
    file_name = select_file()
    data = read_from_file(file_name)
    exit_if_there_is_no_data(data)
    data = process_data(data)
    print_to_output(data)

# TODO
# Print to output in chunks
# Fix GUI
# Make GUI use the new methods
