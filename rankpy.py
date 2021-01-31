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

from re import sub

def read_from_file(file_name):
    with open(file_name, 'r', encoding='utf8') as input_file:
        return input_file.read()

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

if __name__ == '__main__':
    data = read_from_file('sample.txt')
    data = remove_punctuation(data)
    data = text_to_list(data)
    data = word_frequency(data)
    print(data)

#TODO
## Write tests
## Create and update dictionary
## Input file from command line
## Check for file exception
