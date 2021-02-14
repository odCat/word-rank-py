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

root = tk.Tk()
root.geometry('640x480')
root.title('Word Rank Py')

command_frame = tk.Frame(root)
command_frame.pack(side = 'right')
button1 = tk.Button(command_frame, text = 'Open Text File')
button1.pack(expand = tk.YES)
button2 = tk.Button(command_frame, text = 'Get Text')
button2.pack(expand = tk.YES)

text_frame = tk.Frame(root)
text_frame.pack(side = 'left', fill = 'both', expand = True)
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side = 'right', fill = 'y')
text = tk.Text(text_frame, wrap = 'word', yscrollcommand = scrollbar.set)
text.pack(side = 'left', fill = 'both', expand = True)
scrollbar['command'] = text.yview

button2['command'] = (lambda: print(text.get(1.0, tk.END)))

root.mainloop()
