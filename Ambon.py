from tkinter import*
window = Tk()

#Fungsi Untuk Tombol
def tombol_klik(item):
	global ekspresi
	ekspresi=ekspresi + str(item)
	input_text.set(ekspresi)

#Fungsi Tombol Hapus
def tombol_hapus(): 
    global ekspresi
    ekspresi = "" 
    input_text.set("")

#Fungsi Tombol SamaDengan
def tombol_samadengan():	
	global ekspresi    
	
	try:
		hasil = str(eval(ekspresi.replace('%', '/100')))
		input_text.set(hasil)
		ekspresi = ""
	
	except:
		input_text.set("Error")
		ekspresi = ""

command=lambda: tombol_klik("%")

#Fungsi Tombol Positive Negative
def tombol_negasi():
    global ekspresi
    if ekspresi:
        try:
            angka_terakhir = eval(ekspresi)
            ekspresi = str(-angka_terakhir)
            input_text.set(ekspresi)
        except Exception as e:
            input_text.set("Error")
            ekspresi = ""
            
ekspresi=""
input_text=StringVar()
 
 #Frame Kalkulator
frame=Frame(window,bg="black",width=500,height=300)
frame.pack()

frame2=Frame(window,bg="gray",width=500,height=300)
frame2.pack()

label=Label(frame,text="Kalkulator Wafa",width=50,anchor="w",
font=("Arial",10))
label.pack(padx=20,pady=20)

label2=Label(frame,textvariable=input_text,width=30,anchor="e",bg="gray",fg="white",font=("Arial",20))
label2.pack(padx=20,pady=20)


#Button Simbol
Button(frame2,text="AC",command=lambda:tombol_hapus() ,fg="white",bg="black",font=("Arial",15)).grid(row=0,column=0,padx=10,pady=10)

Button(frame2,text="%",command=lambda:tombol_klik("%"),bg="black",fg="white",font=("Arial",15)).grid(row=0,column=2,padx=10,pady=10)

Button(frame2,text="± ",command=lambda:tombol_negasi(),bg="black",fg="white",font=("Arial",15)).grid(row=0,column=1,padx=10,pady=10)

Button(frame2,text="/",command=lambda:tombol_klik("/"),bg="orange",fg="white",font=("Arial",15)).grid(row=0,column=3,padx=10,pady=10)

Button(frame2,text="*",command=lambda:tombol_klik("*"),bg="orange",fg="white",font=("Arial",15)).grid(row=1,column=3,padx=10,pady=10)

Button(frame2,text="-",command=lambda:tombol_klik("-"),bg="orange",fg="white",font=("Arial",15)).grid(row=2,column=3,padx=10,pady=10)

Button(frame2,text="=",command=lambda:tombol_samadengan(),bg="orange",fg="white",font=("Arial",15)).grid(row=4,column=3,padx=10,pady=10)

Button(frame2,text="+",command=lambda:tombol_klik("+"),bg="orange",fg="white",font=("Arial",15)).grid(row=3,column=3,padx=10,pady=10)

Button(frame2,text=".",command=lambda:tombol_klik("."),bg="gray",fg="white",font=("Arial",15)).grid(row=4,column=2,padx=10,pady=10)


#Button Angka
Button(frame2,text="0",command=lambda:tombol_klik("0"),width=7,bg="gray",fg="white",font=("Arial",15)).grid(row=4,column=0,columnspan=2)

Button(frame2,text="1",command=lambda:tombol_klik("1"),bg="gray",fg="white",font=("Arial",15)).grid(row=3,column=0,padx=10,pady=10)

Button(frame2,text="2",command=lambda:tombol_klik("2"),bg="gray",fg="white",font=("Arial",15)).grid(row=3,column=1,padx=10,pady=10)

Button(frame2,text="3",command=lambda:tombol_klik("3"),bg="gray",fg="white",font=("Arial",15)).grid(row=3,column=2,padx=10,pady=10)

Button(frame2,text="4",command=lambda:tombol_klik("4"),bg="gray",fg="white",font=("Arial",15)).grid(row=2,column=0,padx=10,pady=10)

Button(frame2,text="5",command=lambda:tombol_klik("5"),bg="gray",fg="white",font=("Arial",15)).grid(row=2,column=1,padx=10,pady=10)

Button(frame2,text="6",command=lambda:tombol_klik("6"),bg="gray",fg="white",font=("Arial",15)).grid(row=2,column=2,padx=10,pady=10)

Button(frame2,text="7",command=lambda:tombol_klik("7"),bg="gray",fg="white",font=("Arial",15)).grid(row=1,column=0,padx=10,pady=10)

Button(frame2,text="8",command=lambda:tombol_klik("8"),bg="gray",fg="white",font=("Arial",15)).grid(row=1,column=1,padx=10,pady=10)

Button(frame2,text="9",command=lambda:tombol_klik("9"),bg="gray",fg="white",font=("Arial",15)).grid(row=1,column=2,padx=10,pady=10)







window.mainloop()
