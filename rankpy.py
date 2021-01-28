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


def read_from_file(file_name):
    with open(file_name, 'r', encoding='utf8') as input_file:
        return input_file.read()

def remove_punctuation(text):
    text = (' casă masă  carte\nsă-mi\n Linie de dialog' +
            '\ncasă  masă\ncasă parte\n\npasă parte\n\n'
            'televizor\n\"televizor\"\nși\n') 
    return text

#TODO
## Write tests
## Remove punctuation:
     # (ch != '.' && ch != ',' && ch != ':' && ch != ';'    \
     # && ch != '?' && ch != '!' && ch != '(' && ch != ')' \
     # && ch != '"' && ch != '\'')
     # remember to add Romanian quotes
## Create and update dictionary
## Input file from command line
