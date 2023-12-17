from tkinter import *
import ttkbootstrap as tb
# from ttkbootstrap import Style
import tkinter.scrolledtext as st
from NTRUencrypt import NTRUencrypt
from NTRUdecrypt import NTRUdecrypt


encrypt = NTRUencrypt()
decrypt = NTRUdecrypt()


root = tb.Window(themename="cosmo")
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

plain_text_label = tb.Label(plain_text_frame, text = "Plain Text", font = ("helvetica", 16),style='secondar n  y.Inverse.TLabel' )
plain_text_label.grid(row = 0, column = 0 ,padx= 7, pady=7,ipadx=10,ipady=5)

plain_text_entry = tb.Entry(plain_text_frame,font=("helvetica", 16))
plain_text_entry.grid(row = 0, column = 1 ,padx= 7,pady=7, ipadx=40 )

def validate():
    public_key = public_key_entry.get()
    plain_text = plain_text_entry.get()
    if public_key == "" or plain_text == "":
        return False
    return public_key, plain_text

def generatedText(): 
    print("in generatedText")
    
    if not validate():
        return
    cipher_label['state'] = 'normal'
    public_key, plain_text = validate()
    print(public_key, plain_text)
    ct=""
    try:
        encrypt.setKeyFromStr(public_key)
        encrypt.encryptString(plain_text)
        ct = encrypt.Me
        print(ct)
    except:
        ct="Invalid Public Key"
    # copy the selected text to clipboard
    selected_text = ct
    root.clipboard_clear()
    root.clipboard_append(selected_text)
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


#for Plain text
priv=""
pub=""

def generate():
    print("in generate")
    decrypt.genKeys()
    priv, pub = decrypt.Keys2Str()
    private_label1['state'] = 'normal'
    private_label1.insert('end', priv)
    private_label1['state'] = 'disabled'
    public_label1['state'] = 'normal'
    public_label1.insert('end', pub)
    public_label1['state'] = 'disabled'
    selected_text = pub
    #copy the selected text to clipboard
    root.clipboard_clear()
    root.clipboard_append(selected_text)
    # print(priv+"\n"+pub)

def decryptMessage():
    print("in decryptMessage")
    cipher_text = cipher_entry1.get()
    if cipher_text == "":
        return
    plain_text_label1['state'] = 'normal'
    plain_text=""
    try:
        plain_text=decrypt.decryptString(cipher_text)
        print(plain_text)
    except:
        plain_text="Invalid Cipher Text"

    plain_text_label1.insert('end', plain_text)
    plain_text_label1['state'] = 'disabled'
    button1['state'] = 'disabled'

main_frame1 = tb.Frame(tab2,bootstyle="light")
main_frame1.grid(row = 1, column = 0,padx = 140, pady = 15,columnspan=2)
 # main_frame.configure(style='primary.TFrame')

title_lable = tb.Label(main_frame1, text = " Decrypt ", font = ("helvetica", 25), style='secondary.Inverse.TLabel')
title_lable.grid(row = 0, column = 4, padx = 20, pady = 30,columnspan=2,ipady=3)            


##for public key
public_frame1 = tb.Frame(main_frame1,style='secondary.TFrame',relief="flat",borderwidth=4)
public_frame1.grid(row = 1, column = 4,padx = 30 ,pady=20)

public_heading1  = tb.Label(public_frame1, text = "  Public Key: ", font = ("helvetica", 16),style='secondary.Inverse.TLabel' )
public_heading1.grid(row = 0, column = 0 , pady=7,columnspan=2)

generate_button1 = tb.Button(public_frame1, text="Generate",command=generate, style='success.outline.TButton')
generate_button1.grid(row = 0, column = 3 ,pady=7 ,ipadx=6,ipady=4)

public_label1 = st.ScrolledText(public_frame1, height=3, width =50 ,font=("helvetica", 12),state='disabled')
public_label1.grid(row = 1, column = 1  ,padx= 7, pady=10,columnspan=3)


## for private key

private_frame1 = tb.Frame(main_frame1,style='secondary.TFrame',relief="flat",borderwidth=4)
private_frame1.grid(row = 2, column = 4 ,pady=20)

private_heading1  = tb.Label(private_frame1, text = "  private Key: ", font = ("helvetica", 16),style='secondary.Inverse.TLabel' )
private_heading1.grid(row = 0, column = 0 , pady=7,columnspan=2)

private_label1 = st.ScrolledText(private_frame1, height=3, width =50 ,font=("helvetica", 12),state='disabled')
private_label1.grid(row = 1, column = 1  ,padx= 7, pady=10,columnspan=3)


## for cipher text

cipher_frame1 = tb.Frame(main_frame1,style='secondary.TFrame',relief="flat",borderwidth=4)
cipher_frame1.grid(row = 3, column = 4 ,pady=20)

cipher_heading1  = tb.Label(cipher_frame1, text = " Cipher Text: ", font = ("helvetica", 16),style='secondary.Inverse.TLabel' )
cipher_heading1.grid(row = 0, column = 0 ,padx= 7, pady=7,ipadx=10,ipady=5)

cipher_entry1 = tb.Entry(cipher_frame1,font=("helvetica", 16))
cipher_entry1.grid(row = 0, column = 1  ,padx= 7,pady=7, ipadx=35 ,ipady=5)


plain_text_frame1 = tb.Frame(main_frame1,style='secondary.TFrame',relief="flat",borderwidth=4)
plain_text_frame1.grid(row = 4, column = 4 ,pady=20)

plain_text_heading1  = tb.Label(plain_text_frame1, text = " Plain Text: ", font = ("helvetica", 16),style='secondary.Inverse.TLabel' )
plain_text_heading1.grid(row = 0, column = 0 ,padx= 7, pady=7)

plain_text_label1 = st.ScrolledText(plain_text_frame1, height=2, width =36 ,font=("helvetica", 12),state='disabled')
plain_text_label1.grid(row = 0, column = 1  ,padx= 7, pady=7)

## for button
button1 = tb.Button(main_frame1, text="Decrypt",command= decryptMessage, style='success.TButton')
button1.grid(row = 5, column = 4 ,pady=10 , columnspan=2,ipadx=9,ipady=5)



tab_frame.add(tab1, text='Encryption', compound='left') 
tab_frame.add(tab2, text='Decryption', compound='left')
# encryption_frame.add(tab3, text='Key Generation', compound='left')



root.mainloop()
