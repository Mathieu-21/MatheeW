#Programme de morpion

# --- Fonctions --- # 
def croix(x1,y1): #on définis ici les croix
    can1.create_line(x1-140,y1-140,x1+140,y1+140,fill="white",width=3)
    can1.create_line(x1+140,y1-140,x1-140,y1+140,fill="white",width=3)

def rond(x1,y1): #on définis ici les ronds
    can1.create_oval(x1-140,y1-140,x1+140,y1+140,outline="white",width=3)

def pos(event): 
    global a,c1,c2,c3,c4,c5,c6,c7,c8,c9
    X = event.x #coordonnées de la souris
    Y = event.y
    if a==0:
        if X < 300:
            if Y<300:
                if c1!=1 and c1!=5 and c1!=9:
                    croix(150,150)
                    c1=1
                    a=1
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
            if Y>300 and Y<600:
                if c2!=1 and c2!=5 and c2!=9:
                    croix(150,450)
                    c2=1
                    a=1
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
            if Y>600:
                if c3!=1 and c3!=5 and c3!=9:
                    croix(150,750)
                    c3=1
                    a=1
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
        if X>300 and X<600:
            if Y<300:
                if c4!=1 and c4!=5 and c4!=9:
                    croix(450,150)
                    c4=1
                    a=1
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
            if Y>300 and Y<600:
                if c5!=1 and c5!=5 and c5!=9:
                    croix(450,450)
                    c5=1
                    a=1
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
            if Y>600:
                if c6!=1 and c6!=5 and c6!=9:
                    croix(450,750)
                    c6=1
                    a=1
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
        if X>600:
            if Y<300:
                if c7!=1 and c7!=5 and c7!=9:
                    croix(750,150)
                    c7=1
                    a=1
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
            if Y>300 and Y<600:
                if c8!=1 and c8!=5 and c8!=9:
                    croix(750,450)
                    c8=1
                    a=1
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
            if Y>600:
                if c9!=1 and c9!=5 and c9!=9:
                    croix(750,750)
                    c9=1
                    a=1
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
        return
    if a==1:
        if X < 300:
            if Y<300:
                if c1!=1 and c1!=5 and c1!=9:
                    rond(150,150)
                    c1=5
                    a=0
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
            if Y>300 and Y<600:
                if c2!=1 and c2!=5 and c2!=9:
                    rond(150,450)
                    c2=5
                    a=0
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
            if Y>600:
                if c3!=1 and c3!=5 and c3!=9:
                    rond(150,750)
                    c3=5
                    a=0
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
        if X>300 and X<600:

            if Y<300:
                if c4!=1 and c4!=5 and c4!=9:
                    rond(450,150)
                    c4=5
                    a=0
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
            if Y>300 and Y<600:
                if c5!=1 and c5!=5 and c5!=9:
                    rond(450,450)
                    c5=5
                    a=0
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
            if Y>600:
                if c6!=1 and c6!=5 and c6!=9:
                    rond(450,750)
                    c6=5
                    a=0
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
        if X>600:
            if Y<300:
                if c7!=1 and c7!=5 and c7!=9:
                    rond(750,150)
                    c7=5
                    a=0
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
            if Y>300 and Y<600:
                if c8!=1 and c8!=5 and c8!=9:
                    rond(750,450)
                    c8=5
                    a=0
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
            if Y>600:
                if c9!=1 and c9!=5 and c9!=9:
                    rond(750,750)
                    c9=5
                    a=0
                    verif()
                else:
                    showinfo(title='ERROR',message="You can't !")
        return

def verif(): #win ou pas ?
    global c1,c2,c3,c4,c5,c6,c7,c8,c9,comp_c,comp_r
    if (c1+c2+c3)==15 or (c4+c5+c6)==15 or (c7+c8+c9)==15 or (c1+c4+c7)==15 or (c2+c5+c8)==15 or (c3+c6+c9)==15 or (c1+c5+c9)==15 or (c3+c5+c7)==15:
        showwarning(title='Bien joué !!',message="Rond a gagné !")
        comp_r+=1
        compteur()
        retry()
    if (c1+c2+c3)==3 or (c4+c5+c6)==3 or (c7+c8+c9)==3 or (c1+c4+c7)==3 or (c2+c5+c8)==3 or (c3+c6+c9)==3 or (c1+c5+c9)==3 or (c3+c5+c7)==3:
        showwarning(title='Bien joué !!',message="Croix a gagné !")
        comp_c+=1
        compteur()
        retry()
    if (c1+c2+c3+c4+c5+c6+c7+c8+c9)==25:
        showwarning(title='Dommage',message="Egalité ... ")
        retry()

def retry():
    global c1,c2,c3,c4,c5,c6,c7,c8,c9
    n=askyesno(title="Rejouer ?",message="Oui ou non ?")
    if n==True:
        restart()
    if n==False:
        m=askyesno(title="Exit",message="Voulez vous quitter ?")
        if m==True:
            fen.destroy()
        c1,c2,c3,c4,c5,c6,c7,c8,c9=9,9,9,9,9,9,9,9,9

def restart(): #reset
    global c1,c2,c3,c4,c5,c6,c7,c8,c9,a
    can1.delete(ALL)
    c1,c2,c3,c4,c5,c6,c7,c8,c9=0,0,0,0,0,0,0,0,0
    a=0
    can1.create_line(0,300,900,300,fill="black",width=4)
    can1.create_line(0,600,900,600,fill="black",width=4)
    can1.create_line(300,0,300,900,fill="black",width=4)
    can1.create_line(600,0,600,900,fill="black",width=4)

def compteur():
    global comp_c,comp_r
    can2.delete(ALL)
    l1=can2.create_text(120,25,text="Compteur ", font=("Courrier",25),fill="white")
    l2=can2.create_text(70,70,text=comp_c, font=("Courrier",25),fill="white")
    l4=can2.create_text(110,70,text="VS", font=("Courrier",25),fill="red")
    l3=can2.create_text(150,70,text=comp_r,font=("Courrier",25),fill="white")
    can2.create_oval(135,100,165,130,outline="cyan",width=3)
    can2.create_line(60,100,90,130,fill="cyan",width=3)
    can2.create_line(60,130,90,100,fill="cyan",width=3)




# --- Import --- #
from tkinter import*
from random import*
from tkinter.messagebox import*

# --- Init --- #
fen=Tk()
fen.title("Morpion")
fen.geometry("1180x960+400+40")
fen.configure(bg="#41B77F")

a=0
c1,c2,c3,c4,c5,c6,c7,c8,c9=0,0,0,0,0,0,0,0,0
comp_c=0
comp_r=0



can1=Canvas(fen,bg="grey",height=900,width=900)
can1.bind("<Button-1>", pos)
can1.pack(padx=20,pady=5,side = LEFT)
can2=Canvas(fen,bg="#41B77F",height=150,width=225)
can2.pack(pady=380)
but1=Button(fen,text='Exit',command=fen.destroy)
but1.pack(side = TOP)



#damier
can1.create_line(0,300,900,300,fill="black",width=4)
can1.create_line(0,600,900,600,fill="black",width=4)
can1.create_line(300,0,300,900,fill="black",width=4)
can1.create_line(600,0,600,900,fill="black",width=4)


fen.mainloop()


"""
case 1 : 150 150
case 2 : 150 450
case 3 : 150 750
case 4 : 450 150
case 5 : 450 450
case 6 : 450 750
case 7 : 750 150
case 8 : 750 450
case 9 : 750 750

"""