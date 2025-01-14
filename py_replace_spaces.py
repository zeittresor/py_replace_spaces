import tkinter as tk
from tkinter import scrolledtext
import re

def replace_spaces_in_brackets(text):

    pattern = re.compile(r'\{([^}]*)\}', re.DOTALL)  
    def replacer(match):
        content = match.group(1)  
        replaced_content = content.replace(" ", "_")  
        return '{' + replaced_content + '}'
    
    return pattern.sub(replacer, text)

def on_replace():

    original_text = text_box_1.get("1.0", tk.END) 
    replaced_text = replace_spaces_in_brackets(original_text)
    
    text_box_2.delete("1.0", tk.END)
    text_box_2.insert(tk.END, replaced_text)

def on_copy():

    result_text = text_box_2.get("1.0", tk.END)
    
    root.clipboard_clear()
    root.clipboard_append(result_text)

root = tk.Tk()
root.title("Replace spaces between {..} with underline")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_1 = tk.Label(frame, text="Original Text:")
label_1.grid(row=0, column=0, sticky="w")

text_box_1 = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=10)
text_box_1.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

label_2 = tk.Label(frame, text="Replaced Text:")
label_2.grid(row=2, column=0, sticky="w")

text_box_2 = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=10)
text_box_2.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

replace_button = tk.Button(frame, text="Replace", command=on_replace)
replace_button.grid(row=4, column=0, padx=5, pady=5, sticky="e")

copy_button = tk.Button(frame, text="Copy to Clipboard", command=on_copy)
copy_button.grid(row=4, column=1, padx=5, pady=5, sticky="w")

root.mainloop()
