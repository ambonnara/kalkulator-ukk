from tkinter import*
window = Tk()

def tombol_klik(item):
	global ekspresi
	ekspresi=ekspresi + str(item)
	input_text.set(ekspresi)

def tombol_hapus(): 
    global ekspresi
    ekspresi = "" 
    input_teks.set("")
    
def tombol_samadengan():
    global ekspresi
    hasil = str(eval(ekspresi)) 
    input_teks.set(hasil)
    ekspresi = ""
    
ekspresi=""
input_text=StringVar()
 
frame=Frame(window,bg="yellow",width=500,height=300)
frame.pack()

frame2=Frame(window,bg="black",width=500,height=300)
frame2.pack()

label=Label(frame,text="Kalkulator Python",
font=("Arial",10))
label.pack(padx=20,pady=20)

label2=Label(frame,textvariable=input_text,
font=("Arial",10))
label2.pack(padx=20,pady=20)



Button(frame2,text="C",command=lambda:tombol_hapus(),width=7,fg="white",bg="red").grid(row=0,column=0,columnspan=2)

Button(frame2,text="/",command=lambda:tombol_klik("/"),bg="gray").grid(row=0,column=2,padx=10,pady=10)

Button(frame2,text="*",command=lambda:tombol_klik("*"),bg="gray").grid(row=0,column=3,padx=10,pady=10)

Button(frame2,text="+",command=lambda:tombol_klik("+"),bg="gray").grid(row=1,column=3,padx=10,pady=10)

Button(frame2,text="-",command=lambda:tombol_klik("-"),bg="gray").grid(row=2,column=3,padx=10,pady=10)

Button(frame2,text="=",command=lambda:tombol_samadengan(),height=3,bg="gray").grid(row=3,column=3,rowspan=2)

Button(frame2,text=".",command=lambda:tombol_klik(".")).grid(row=4,column=2,padx=10,pady=10)



Button(frame2,text="0",command=lambda:tombol_klik("0"),width=7).grid(row=4,column=0,columnspan=2)


Button(frame2,text="1",command=lambda:tombol_klik("1")).grid(row=3,column=0,padx=10,pady=10)


Button(frame2,text="2",command=lambda:tombol_klik("2")).grid(row=3,column=1,padx=10,pady=10)


Button(frame2,text="3",command=lambda:tombol_klik("3")).grid(row=3,column=2,padx=10,pady=10)

Button(frame2,text="4",command=lambda:tombol_klik("4")).grid(row=2,column=0,padx=10,pady=10)

Button(frame2,text="5",command=lambda:tombol_klik("5")).grid(row=2,column=1,padx=10,pady=10)

Button(frame2,text="6",command=lambda:tombol_klik("6")).grid(row=2,column=2,padx=10,pady=10)

Button(frame2,text="7",command=lambda:tombol_klik("7")).grid(row=1,column=0,padx=10,pady=10)

Button(frame2,text="8",command=lambda:tombol_klik("8")).grid(row=1,column=1,padx=10,pady=10)

Button(frame2,text="9",command=lambda:tombol_klik("9")).grid(row=1,column=2,padx=10,pady=10)







window.mainloop()