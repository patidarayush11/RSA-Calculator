from tkinter import *
def euclid(a, b):
   
    if b == 0:
        return a
    else:
        return euclid(b, a % b)
 
def extended_euclid(a, b):
    
    if b == 0:
        return [a, 1, 0]
    else:
        previous_d, previous_x, previous_y = extended_euclid(b, a % b)
        d, x, y = (previous_d, previous_y, previous_x - a // b * previous_y)
        return [d, x, y]
 
def generate_keys(p, q):

#Generation of public and private keys.
    n = p * q
    m = (p - 1) * (q - 1)
 
    e = int(2)
    while e < m:
        if euclid(e, m) == 1:
            break
        else:
            e = e + 1
 
    dd, x, y = extended_euclid(m, e)
    if y > 0:
        d = y
    else:
        d = y % m
 
    return [(e, n), (d, n)]
 

def rsa():
    global l2
    p= int(a.get())
    q= int(b.get())
    msg= int(c.get())
    pub_key, priv_key = generate_keys(p, q)
    
    print ('Public Key: ', pub_key)
    print ('Private Key: ', priv_key)
 
    e, n = pub_key
    d, n = priv_key
 
    crypted = (msg ** e) % n
    l2.config(text=crypted)
    #print ('Crypted value is(C): ', crypted)
 
    original = crypted ** d % n
    print ('The original number was(M): ', original)



root = Tk()    
root.title('RSA Calculator')   

l = Label(root,text='First Prime No. (P)')
l.pack() 

a = Entry(root) 
a.pack()

l = Label(root,text='Second Prime No. (Q)')
l.pack()

b = Entry(root) 
b.pack()

l = Label(root,text='msg')
l.pack()

c = Entry(root)
c.pack()

l2= Label(root,text='Crypted (C):')
l2.pack()
button = Button(root,text="Encrypt",command=rsa) 
button.pack()

root.mainloop() 

