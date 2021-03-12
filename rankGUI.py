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

import tkinter as tk
import rankpy as rk

root = tk.Tk()
root.title('Word Rank Py')
root.geometry('640x480')

data = ''

def setInputText(text):
    text_input.delete(1.0, tk.END)
    text_input.insert(1.0, text)

def rank_from_input(text):
    data = rk.remove_empty_lines(text)
    if data == '':
        print('The string is empty')
    else:
        data = rk.remove_punctuation(data)
        data = rk.text_to_list(data)
        data = rk.word_frequency(data)
        data = rk.make_printable(data)
        print(data)

# Command frame
command_frame = tk.Frame(root)
command_frame.pack(side = 'right')
button1 = tk.Button(command_frame, text = 'Open Text File')
button1.pack(expand = tk.YES)
button2 = tk.Button(command_frame, text = 'Get Text')
button2.pack(expand = tk.YES)
button3 = tk.Button(command_frame, text = 'Set Text')
button3.pack(expand = tk.YES)

# Text frame
text_frame = tk.Frame(root)
text_frame.pack(side = 'left', fill = 'both', expand = True)
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side = 'right', fill = 'y')
text_input = tk.Text(text_frame, wrap = 'word',
        yscrollcommand = scrollbar.set)
text_input.pack(side = 'left', fill = 'both', expand = True)
scrollbar['command'] = text_input.yview

# Set commands
button2['command'] = (lambda:
        rank_from_input(text_input.get(1.0, tk.END)))
button3['command'] = (lambda: setInputText('new ătext'))

root.mainloop()