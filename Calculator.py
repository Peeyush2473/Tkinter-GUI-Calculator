import tkinter as tk

# Function to recognise the button clicked and add to display
def click(event):
    text = event.widget.cget('text')
    if text == 'AC':
        clear_all()
        return
    elif text == 'CLR':
        delete_one()
        return
    elif text == '=':
        evaluate()
        return
    add_to_dis(text)

# Function to add a new element to the output display
def add_to_dis(text):
    global exp
    
    if text == 'x\u207b\u00b9':
        text = '\u207b\u00b9'
    elif text == 'x\u00b2':
        text = '^2'
    exp += text
    dis.delete(1.0, tk.END)
    dis.insert(1.0, exp, 'right')

# Function to calculate and display the result
def evaluate():
    global exp
    if exp =='':
        return
    rep_list = (('÷', '/'), ('x', '*'), ('\u207b\u00b9', '**-1'), ('^', '**'), ('%', '/100'))
    for i in rep_list:
        if i[0] in exp:
            exp = exp.replace(i[0], i[1])
    
    dis.delete(1.0, tk.END)
    try:
        result = eval(exp)
        dis.insert(1.0, f'= {result:.4f}')
        dis.tag_add("right", "1.0", "1.end")
    except:
        result = "Invalid Input!"
        dis.insert(1.0, result)
        dis.tag_add("center", "1.0", "1.end")
    
    exp =''

# Function to clear the output display
def clear_all():
    global exp
    dis.delete(1.0,tk.END)
    exp = ''

# Function to remove the last entered element from the display
def delete_one():
    global exp
    exp = exp[:-1]
    dis.delete(1.0, tk.END)
    dis.insert(1.0, exp, 'right')

# Function to use Keyboard for input
def shortcut(event):
    if event.keysym == 'Return':
        evaluate()
    elif event.keysym == 'BackSpace':
        delete_one()
    elif event.char.isdigit() or event.char in ('.', '%', '+', '-', '^', '(', ')'):
        add_to_dis(event.char)
    elif event.char == '/':
        add_to_dis('÷')
    elif event.char == '*' or event.char.lower() == 'x':
        add_to_dis('x')



#--- Main Code ---#
root = tk.Tk()
root.geometry('450x300+700+350')
root.bind('<KeyPress>', shortcut)

frame =tk.Frame(root)
frame.columnconfigure(0, weight= 1)
frame.columnconfigure(1, weight = 1)
frame.columnconfigure(2, weight = 1)
frame.columnconfigure(3, weight = 1)
frame.columnconfigure(4, weight = 1)
frame.columnconfigure(5, weight = 1)


exp = ''
dis = tk.Text(root, height = 1, width = 25, font = ('lucida 20 bold', 30))
dis.tag_configure('right', justify= tk.RIGHT)
dis.tag_configure('center', justify= tk.CENTER)
dis.pack(pady = 7)

bttn_sym = (
    '7', '8', '9', '÷', 'CLR', 'AC',
    '4', '5', '6', 'x', '(' , ')',
    '1', '2', '3', '-', 'x\u207b\u00b9' , 'x\u00b2',
    '0', '.', '%', '+', '='
    )

for i in range(len(bttn_sym)):
    bttn = tk.Button(frame, height = 2, font = ('lucida 20 bold', 20),text = bttn_sym[i])
    bttn.bind('<Button-1>', click)
    bttn.grid(row= i//6, column= i%6, sticky= 'nsew')
bttn.grid(columnspan=2)
frame.pack(fill= 'both')
root.mainloop()