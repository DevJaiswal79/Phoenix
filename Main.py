from tkinter import *
import ttkbootstrap as tb
# from ttkbootstrap import Style
import tkinter.scrolledtext as st

root = tb.Window(themename="flatly")
# root = Tk
root.title("Asymmetric Lattice Based Cryptography System")
# root.iconbitmap("img/python.ico")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d" % (w-850,h))
root.configure(bg="grey")

tab_frame = tb.Notebook(root, bootstyle="light",width=w//2,height=h-220)
tab_frame.grid(row = 1, column = 0,columnspan=2,padx=60,pady=60)

tab1 = tb.Frame(tab_frame, bootstyle="dark")
tab2 = tb.Frame(tab_frame, bootstyle="dark")
# tab3 = tb.Frame(encryption_frame, bootstyle="light")

## for encryption tab

# title_frame = tb.Frame(tab1, bootstyle="dark")
# title_frame.grid(row = 0, column = 0, padx = w//4,pady=40)
# title_Label = tb.Label(tab1, text = "  Encryption Tab  ", font = ("helvetica", 25),style='secondary.Inverse.TLabel')
# title_Label.grid(row = 0, column = 0 )


main_frame = tb.Frame(tab1,bootstyle="light")
main_frame.grid(row = 1, column = 0,padx = 140, pady = 60,columnspan=2)
 # main_frame.configure(style='primary.TFrame')

title_lable = tb.Label(main_frame, text = " Encrypt ", font = ("helvetica", 25), style='secondary.Inverse.TLabel')
title_lable.grid(row = 0, column = 4, padx = 20, pady = 30,columnspan=2,ipady=3)            


##label for public key
public_frame = tb.Frame(main_frame,style='secondary.TFrame',relief="flat",borderwidth=4)
public_frame.grid(row = 1, column = 4 ,pady=20)

public_key_label = tb.Label(public_frame, text = "Public Key", font = ("helvetica", 16),style='secondary.Inverse.TLabel' )
public_key_label.grid(row = 0, column = 0  ,padx= 7, pady=7, ipadx=10,ipady=5 )

public_key_entry = tb.Entry(public_frame,font=("helvetica", 16))
public_key_entry.grid(row = 0, column = 1,padx= 7 , pady=7, ipadx=40 )

## for Plain text
plain_text_frame = tb.Frame(main_frame,style='secondary.TFrame',relief="flat",borderwidth=4)
plain_text_frame.grid(row = 2, column = 4 ,pady=20)

plain_text_label = tb.Label(plain_text_frame, text = "Plain Text", font = ("helvetica", 16),style='secondary.Inverse.TLabel' )
plain_text_label.grid(row = 0, column = 0 ,padx= 7, pady=7,ipadx=10,ipady=5)

plain_text_entry = tb.Entry(plain_text_frame,font=("helvetica", 16))
plain_text_entry.grid(row = 0, column = 1 ,padx= 7,pady=7, ipadx=40 )

def validate():
    public_key = public_key_entry.get()
    plain_text = plain_text_entry.get()
    if public_key == "" or plain_text == "":
        return False
    return True

def generatedText(): 
    if not validate():
        return
    cipher_label['state'] = 'normal'
    ct = """Y44_OSsEU0u4XmtTFn5N0NCOLTvzBKkXopi1CkaIegCuPprHxDWVAIkIC7WP9LpIzx6b0AqrIbphtbikqidoXAleeHzAUY-18atiyA1qNRD9scV077rcV1p7j2jOaQp2ccsWaoVkbWUpUNN3tN-F3Suv8CE4Dl6yH74aNuJh8TVDX3Z6pbeQ-tsmGFGIQKOteOVYxJc9ziXG_MVgPRZYGJPxlb7ysPKt5ldgVmUxgRcVGi_1ctQ-mJjoBMMdqmWcNlXYkECU4rSex0nBYWywZiDD7k0FqkELzn3ayfEYo-biI8uYvwAfhBcEDf_zcZyCaKWYZMUSqrTGBEzaDAO5Icwnus6YYBluNQGN-O80z2SRWVIEURIFqVdtcbqQbTUnJ8VIs7LKBr-pnbAIOBHW82RHOh1oxEwESpBjBL8vBJAv_fZpMbzWAbPp2IFSYNe6LArisfZK9zSBqsyqc6n2_s-TjXKMxbad18JoMVa03JFPGXy7xJ4JogwRqErVK58BeAfmN_UaH2yAiaBQqUJo5qvv6loN2xU5Wyzz8WzQ7X7FMC1CNQ_atGHY0jOfD5AXY_gHm1QjrmWAPbA95YwdCSDJ3Z4JNGVzzaAo6E8R3rZKbRokM2w9KetmDZPV8bGH-EKwulwxAt8KIkbfk_7pZLduOjUIoomjk8eHPnICdHP5-0-I65FVCIpdedWINBC-Odc5IkPhV8I8m4ZzCnxqKB60UZXXGz1fD6yavkRqaQbVQKr-4AqM_FXW4Z4AAE7Cu0-pYgoTo0RTQ7zXMc0zpX-LqE7iB20cPWQMn9nMN1k2O9XQA6Voh5mnuKcWKynl"""
    cipher_label.insert('end', ct) 
    cipher_label['state'] = 'disabled'
    button['state'] = 'disabled'

## for cypertext
cipher_frame = tb.Frame(main_frame,style='secondary.TFrame',relief="flat",borderwidth=10)
cipher_frame.grid(row = 3, column = 4 ,padx=30,pady=20)

cipher_heading  = tb.Label(cipher_frame, text = "  Cipher Text: ", font = ("helvetica", 18),style='secondary.Inverse.TLabel' )
cipher_heading.grid(row = 0, column = 0 ,padx= 7, pady=7,ipadx=5,ipady=3)

cipher_label = st.ScrolledText(cipher_frame, height=7, width =46 ,font=("helvetica", 12),state='disabled')
cipher_label.grid(row = 1, column = 0  ,padx= 7, pady=7,ipadx=5,ipady=3)

## for button
button = tb.Button(main_frame, text="Encrypt",command=generatedText, style='success.TButton')
button.grid(row = 4, column = 4 ,pady=15 , columnspan=2,ipadx=9,ipady=5)

#--------------------------------------------------------------------------------------------------------------







## for decryption tab
# title_frame = tb.Frame(tab2, bootstyle="dark")
# title_frame.grid(row = 0, column = 0, padx = w//4,pady=40)
# title_Label = tb.Label(tab2, text = "  Decryption Tab  " , font = ("helvetica", 25),style='secondary.Inverse.TLabel')
# title_Label.grid(row = 0, column = 0 )


main_frame1 = tb.Frame(tab2,bootstyle="light")
main_frame1.grid(row = 1, column = 0,padx = 140, pady = 35,columnspan=2)
 # main_frame.configure(style='primary.TFrame')

title_lable = tb.Label(main_frame1, text = " Decrypt ", font = ("helvetica", 25), style='secondary.Inverse.TLabel')
title_lable.grid(row = 0, column = 4, padx = 20, pady = 30,columnspan=2,ipady=3)            


##for public key
public_frame1 = tb.Frame(main_frame1,style='secondary.TFrame',relief="flat",borderwidth=4)
public_frame1.grid(row = 1, column = 4,padx = 30 ,pady=20)

public_heading1  = tb.Label(public_frame1, text = "  Public Key: ", font = ("helvetica", 16),style='secondary.Inverse.TLabel' )
public_heading1.grid(row = 0, column = 0 , pady=7,columnspan=2)

generate_button1 = tb.Button(public_frame1, text="Generate",command=generatedText, style='success.outline.TButton')
generate_button1.grid(row = 0, column = 3 ,pady=7 ,ipadx=6,ipady=4)

public_label1 = st.ScrolledText(public_frame1, height=1, width =50 ,font=("helvetica", 12),state='disabled')
public_label1.grid(row = 1, column = 1  ,padx= 7, pady=10,columnspan=3)


## for private key

private_frame1 = tb.Frame(main_frame1,style='secondary.TFrame',relief="flat",borderwidth=4)
private_frame1.grid(row = 2, column = 4 ,pady=20)

private_heading1  = tb.Label(private_frame1, text = "  private Key: ", font = ("helvetica", 16),style='secondary.Inverse.TLabel' )
private_heading1.grid(row = 0, column = 0 , pady=7,columnspan=2)

private_label1 = st.ScrolledText(private_frame1, height=1, width =50 ,font=("helvetica", 12),state='disabled')
private_label1.grid(row = 1, column = 1  ,padx= 7, pady=10,columnspan=3)


## for cipher text

cipher_frame1 = tb.Frame(main_frame1,style='secondary.TFrame',relief="flat",borderwidth=4)
cipher_frame1.grid(row = 3, column = 4 ,pady=20)

cipher_heading1  = tb.Label(cipher_frame1, text = " Cipher Text: ", font = ("helvetica", 16),style='secondary.Inverse.TLabel' )
cipher_heading1.grid(row = 0, column = 0 ,padx= 7, pady=7,ipadx=10,ipady=5)

cipher_entry1 = tb.Entry(cipher_frame1,font=("helvetica", 16))
cipher_entry1.grid(row = 0, column = 1  ,padx= 7,pady=7, ipadx=35 ,ipady=5)

#for Plain text

plain_text_frame1 = tb.Frame(main_frame1,style='secondary.TFrame',relief="flat",borderwidth=4)
plain_text_frame1.grid(row = 4, column = 4 ,pady=20)

plain_text_heading1  = tb.Label(plain_text_frame1, text = " Plain Text: ", font = ("helvetica", 16),style='secondary.Inverse.TLabel' )
plain_text_heading1.grid(row = 0, column = 0 ,padx= 7, pady=7)

plain_text_label1 = st.ScrolledText(plain_text_frame1, height=1, width =36 ,font=("helvetica", 12),state='disabled')
plain_text_label1.grid(row = 0, column = 1  ,padx= 7, pady=7)

## for button
button1 = tb.Button(main_frame1, text="Decrypt",command=generatedText, style='success.TButton')
button1.grid(row = 5, column = 4 ,pady=10 , columnspan=2,ipadx=9,ipady=5)



tab_frame.add(tab1, text='Encryption', compound='left') 
tab_frame.add(tab2, text='Decryption', compound='left')
# encryption_frame.add(tab3, text='Key Generation', compound='left')



root.mainloop()
