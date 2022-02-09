import tkinter as tk

def show_output():
    # number = number_input.get() #เดิมคือจะใช้คำสั่งนี้ แต่ get คืนค่าเป็นข้อความ
    number = int(number_input.get()) #เราจึงต้องใช้ int เพื่อแปลงตัวเลขให้เป็นข้อมูลก่อนคือ คำสั่ง int

    if number == 0:
        output_label.configure(text='ผิดที่ไว้ใจ')
        return

    output = ''

    for i in range(1, 13):
       output += str(number) + ' x ' + str(i)
       output += ' = ' + str(number * i) + '\n'

    output_label.configure(text=output)

window = tk.Tk()
window.title('JustPython')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='สูตรคูณแม่')
title_label.pack(pady=20)

number_input = tk.Entry(master=window, width=15)
number_input.pack()

go_button = tk.Button(
    master=window, text='ได้แก่',
    command=show_output ,width=15, height=2
)
go_button.pack()

output_label = tk.Label(master=window)
output_label.pack(pady=20)

window.mainloop()