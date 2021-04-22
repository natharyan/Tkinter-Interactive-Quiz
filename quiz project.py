from tkinter import *

win = Tk()
win.title("WELCOME")
win.geometry("650x450")
l1 = Label(win, text="Astronomy Quiz!!", fg="black",bg="DodgerBlue3",height="3")
l1.pack(fill=X)
l2 = Label(win, text="General Instructions:", fg="blue")
l2.pack()
l3 = Label(win, text="The quiz contains a total of 10 questions, each of 1 mark each. \nThere is no negative marking",fg="deep sky blue")
l3.pack()
l4 = Label(win, text="ENJOY!!", fg="black",bg="DodgerBlue2",height="3")
l4.pack(fill=X)
l0 = Label(win, text="",height="2")
l0.pack(fill=X)
b = Button(win, text="PRESS TO START QUIZ", fg="white",bg="DodgerBlue4",height="10",command=win.destroy)
b.pack(fill=X)

win.mainloop()

score = 0

def project(a):

    root = Tk()
    root.title("QUIZ")
    root.geometry("650x450")

    def q(a):
        def myclick():
            b1['text'] = "Wrong Answer"
            b1['bg'] = "red"
            b3['text'] = "Wrong Answer"
            b3['bg'] = "red"
            b4['text'] = "Wrong Answer"
            b4['bg'] = "red"

        def myclick1():
            b2['text'] = "Correct Answer"
            b2['bg'] = "Green"
            global score
            score += 1

        if a == 1:
            l5 = Label(root, text="Who speculated that our universe is expanding?", fg="black",bg="gold",height="5")
            l0 = Label(root, text="", height="2")
            b1 = Button(root, text="A. Newton", fg="white",bg="DodgerBlue3",command=myclick)
            b2 = Button(root, text="B. Edwin Hubble", fg="white",bg="DodgerBlue3",command=myclick1)
            b3 = Button(root, text="C. Galilio", fg="white",bg="DodgerBlue3",command=myclick)
            b4 = Button(root, text="D. Copernicus", fg="white",bg="DodgerBlue3",command=myclick)
            l=Label(root,text="",height="5")

            next = Button(root, text=" NEXT QUESTION", fg="white", bg="DodgerBlue4", height="2",command=root.destroy)
            l5.pack(fill=X)
            l0.pack(fill=X)
            b1.pack(fill=X)
            b2.pack(fill=X)
            b3.pack(fill=X)
            b4.pack(fill=X)
            l.pack(fill=X)
            next.pack()

        if a == 2:
            l5 = Label(root, text="Who had propounded the planetary laws?", fg="black",bg="gold",height="5")
            l0 = Label(root, text="", height="2")
            b1 = Button(root, text="A. Newton", fg="white",bg="DodgerBlue3",command=myclick)
            b2 = Button(root, text="B. Kepler", fg="white",bg="DodgerBlue3",command=myclick1)
            b3 = Button(root, text="C. Galilio", fg="white",bg="DodgerBlue3",command=myclick)
            b4 = Button(root, text="D. Copernicus", fg="white",bg="DodgerBlue3",command=myclick)
            l = Label(root, text="", height="5")

            next = Button(root, text=" NEXT QUESTION", fg="white", bg="DodgerBlue4", height="2",command=root.destroy)
            l5.pack(fill=X)
            l0.pack(fill=X)
            b1.pack(fill=X)
            b2.pack(fill=X)
            b3.pack(fill=X)
            b4.pack(fill=X)
            l.pack(fill=X)
            next.pack()

        if a == 3:
            l5 = Label(root, text="Who had proved first that our earth and another planet are revolving?",
                       fg="black", bg="gold",height="5")
            l0 = Label(root, text="", height="2")
            b1 = Button(root, text="A. Aristotle", fg="white",bg="DodgerBlue3",command=myclick)
            b3 = Button(root, text="B. Galileo", fg="white",bg="DodgerBlue3",command=myclick)
            b2 = Button(root, text="C. Copernicus", fg="white",bg="DodgerBlue3",command=myclick1)
            b4 = Button(root, text="D. Edwin Hubble", fg="white",bg="DodgerBlue3",command=myclick)
            l = Label(root, text="", height="5")
            next = Button(root, text=" NEXT QUESTION", fg="white", bg="DodgerBlue4", height="2",command=root.destroy)
            l5.pack(fill=X)
            l0.pack(fill=X)
            b1.pack(fill=X)
            b3.pack(fill=X)
            b2.pack(fill=X)
            b4.pack(fill=X)
            l.pack(fill=X)
            next.pack()

        if a == 4:
            l5 = Label(root, text="Which one of the following elements occurs most abundantly in our universe?",
                       fg="black",bg="gold",height="5")
            l0 = Label(root, text="", height="2")
            b2 = Button(root, text="A. Hydrogen", fg="white",bg="DodgerBlue3",command=myclick1)
            b1 = Button(root, text="B. Nitrogen", fg="white",bg="DodgerBlue3",command=myclick)
            b3 = Button(root, text="C. Copernicus", fg="white",bg="DodgerBlue3",command=myclick)
            b4 = Button(root, text="D. Oxygen", fg="white",bg="DodgerBlue3",command=myclick)
            l = Label(root, text="", height="5")
            next = Button(root, text=" NEXT QUESTION", fg="white", bg="DodgerBlue4", height="2",command=root.destroy)
            l5.pack(fill=X)
            l0.pack(fill=X)
            b2.pack(fill=X)
            b1.pack(fill=X)
            b3.pack(fill=X)
            b4.pack(fill=X)
            l.pack(fill=X)
            next.pack()

        if a == 5:
            l5 = Label(root, text="The stellar and solar source of energy is?", fg="black",bg="gold",height="5")
            l0 = Label(root, text="", height="2")
            b2 = Button(root, text="A. Nuclear fusion", fg="white",bg="DodgerBlue3",command=myclick1)
            b1 = Button(root, text="B. Nuclear fission", fg="white",bg="DodgerBlue3",command=myclick)
            b3 = Button(root, text="C. Electromagnetic induction", fg="white",bg="DodgerBlue3",command=myclick)
            b4 = Button(root, text="D. Electromotive force", fg="white",bg="DodgerBlue3",command=myclick)
            l = Label(root, text="", height="5")
            next = Button(root, text=" NEXT QUESTION", fg="white", bg="DodgerBlue4", height="2",command=root.destroy)
            l5.pack(fill=X)
            l0.pack(fill=X)
            b2.pack(fill=X)
            b1.pack(fill=X)
            b3.pack(fill=X)
            b4.pack(fill=X)
            l.pack(fill=X)
            l0.pack(fill=X)
            next.pack()

        if a == 6:
            l5 = Label(root,
                       text="The device employed to measure the diameters of stars and our galaxy (Milky Way) is called?",
                       fg="black",bg="gold",height="5")
            l0 = Label(root, text="", height="2")
            b1 = Button(root, text="A. Photometer", fg="white",bg="DodgerBlue3",command=myclick)
            b4 = Button(root, text="B. Barometer", fg="white",bg="DodgerBlue3",command=myclick)
            b3 = Button(root, text="C. Viscometer", fg="white",bg="DodgerBlue3",command=myclick)
            b2 = Button(root, text="D. Interferometer", fg="white",bg="DodgerBlue3",command=myclick1)
            l = Label(root, text="", height="5")
            next = Button(root, text=" NEXT QUESTION", fg="white", bg="DodgerBlue4", height="2",command=root.destroy)
            l5.pack(fill=X)
            l0.pack(fill=X)
            b1.pack(fill=X)
            b4.pack(fill=X)
            b3.pack(fill=X)
            b2.pack(fill=X)
            l.pack(fill=X)
            next.pack()

        if a == 7:
            l5 = Label(root,
                       text="The planet whose density is less than water and on keeping in the water it will start to float?",
                       fg="black",bg="gold",height="5")
            l0 = Label(root, text="", height="2")
            b1 = Button(root, text="A. Mercury", fg="white",bg="DodgerBlue3",command=myclick)
            b3 = Button(root, text="B. Venus", fg="white",bg="DodgerBlue3",command=myclick)
            b2 = Button(root, text="C. Saturn", fg="white",bg="DodgerBlue3",command=myclick1)
            b4 = Button(root, text="D. Mars", fg="white",bg="DodgerBlue3",command=myclick)
            l = Label(root, text="", height="5")
            next = Button(root, text=" NEXT QUESTION", fg="white", bg="DodgerBlue4", height="2",command=root.destroy)
            l5.pack(fill=X)
            l0.pack(fill=X)
            b1.pack(fill=X)
            b3.pack(fill=X)
            b2.pack(fill=X)
            b4.pack(fill=X)
            l.pack(fill=X)
            l0.pack(fill=X)
            next.pack()

        if a == 8:
            l5 = Label(root, text="Which of the following planets has the largest number of moons?", fg="black",bg="gold",height="5")
            l0 = Label(root, text="", height="2")
            b2 = Button(root, text="A. Saturn", fg="white",bg="DodgerBlue3",command=myclick1)
            b1 = Button(root, text="B. Jupiter", fg="white",bg="DodgerBlue3",command=myclick)
            b3 = Button(root, text="C. Mars", fg="white",bg="DodgerBlue3",command=myclick)
            b4 = Button(root, text="D. Neptune", fg="white",bg="DodgerBlue3",command=myclick)
            l = Label(root, text="", height="5")
            next = Button(root, text=" NEXT QUESTION", fg="white", bg="DodgerBlue4", height="2",command=root.destroy)
            l5.pack(fill=X)
            l0.pack(fill=X)
            b2.pack(fill=X)
            b1.pack(fill=X)
            b3.pack(fill=X)
            b4.pack(fill=X)
            l.pack(fill=X)
            next.pack()

        if a == 9:
            l5 = Label(root, text="Which one of the following planet is also called morning star or evening star?",
                       fg="black",bg="gold",height="5")
            l0 = Label(root, text="", height="2")
            b1 = Button(root, text="A. Mercury", fg="white",bg="DodgerBlue3",command=myclick)
            b2 = Button(root, text="B. Venus", fg="white",bg="DodgerBlue3",command=myclick1)
            b3 = Button(root, text="C. Mars", fg="white",bg="DodgerBlue3",command=myclick)
            b4 = Button(root, text="D. Saturn", fg="white",bg="DodgerBlue3",command=myclick)
            l = Label(root, text="", height="5")
            next = Button(root, text=" NEXT QUESTION", fg="white", bg="DodgerBlue4", height="2",command=root.destroy)
            l5.pack(fill=X)
            l0.pack(fill=X)
            b1.pack(fill=X)
            b2.pack(fill=X)
            b3.pack(fill=X)
            b4.pack(fill=X)
            l.pack(fill=X)
            next.pack()

        if a == 10:
            l5 = Label(root, text="The planet which completes one revolution in 88 days around the Sun is?",
                       fg="black",bg="gold",height="5")
            l0 = Label(root, text="", height="2")
            b2 = Button(root, text="A. Mercury", fg="white",bg="DodgerBlue3",command=myclick1)
            b1 = Button(root, text="B. Venus", fg="white",bg="DodgerBlue3",command=myclick)
            b3 = Button(root, text="C. Mars", fg="white",bg="DodgerBlue3",command=myclick)
            b4 = Button(root, text="D. Saturn", fg="white",bg="DodgerBlue3",command=myclick)
            l = Label(root, text="", height="5")
            next = Button(root, text=" FINISH QUIZ", fg="white", bg="maroon", height="2",command=root.destroy)
            l5.pack(fill=X)
            l0.pack(fill=X)
            b2.pack(fill=X)
            b1.pack(fill=X)
            b3.pack(fill=X)
            b4.pack(fill=X)
            l.pack(fill=X)
            next.pack()



    q(a)
    root.mainloop()

for a in range(1,11):
    project(a)

root = Tk()
root.title("RESULTS")
root.geometry("650x450")
if score==10:
    l = Label(text="FULL MARKS !!  10/10", fg="white", bg="orange", width="650", height="450")
    l.pack()
else:
    l=Label(text="Your Score = "+str(score),fg="white",bg="orange",width="650",height="450")
    l.pack()

root.mainloop()

# Answer key: b,b,c,a,a,d,c,a,b,a
