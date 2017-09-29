# import of modules
import tkinter, random, math, _thread, time, os, sys

# functions for animations
def anim_task5_left():
    global canvas_left, ball1, ball2, ball4, ball5
    while 1:
        try:
            for i in range (1, 16):
                canvas_left.move(ball1, 2, 1)
                x1, y1, x2, y2 = canvas_left.coords(ball1)
                canvas_left.coords(line1, x1+15, y1, 105, 50)
                x1 += 30
                x2 += 30
                canvas_left.coords(ball2, x1, y1, x2, y2)
                canvas_left.coords(line2, x1+15, y1, 135, 50)
                time.sleep(0.05)
            for i in range (1, 16):
                canvas_left.move(ball4, 2, -1)
                x1, y1, x2, y2 = canvas_left.coords(ball4)
                canvas_left.coords(line4, x1+15, y1, 195, 50)
                x1 += 30
                x2 += 30
                canvas_left.coords(ball5, x1, y1, x2, y2)
                canvas_left.coords(line5, x1+15, y1, 225, 50)
                time.sleep(0.05)
            for i in range (1, 16):
                canvas_left.move(ball4, -2, 1)
                x1, y1, x2, y2 = canvas_left.coords(ball4)
                canvas_left.coords(ball4, x1, y1, x2, y2)
                canvas_left.coords(line4, x1+15, y1, 195, 50)
                x1 += 30
                x2 += 30
                canvas_left.coords(ball5, x1, y1, x2, y2)
                canvas_left.coords(line5, x1+15, y1, 225, 50)
                time.sleep(0.05)
            for i in range (1, 16):
                canvas_left.move(ball1, -2, -1)
                x1, y1, x2, y2 = canvas_left.coords(ball1)
                canvas_left.coords(line1, x1+15, y1, 105, 50)
                x1 += 30
                x2 += 30
                canvas_left.coords(ball2, x1, y1, x2, y2)
                canvas_left.coords(line2, x1+15, y1, 135, 50)
                time.sleep(0.05)
        except:
            break
def anim_task5_right():
    global canvas_right, ball6, ball7, ball10
    while 1:
        try:
            for i in range (1, 16):
                canvas_right.move(ball6, 2, 1)
                x1, y1, x2, y2 = canvas_right.coords(ball1)
                canvas_right.coords(line6, x1+15, y1, 105, 50)
                x1 += 30
                x2 += 30
                canvas_right.coords(ball7, x1, y1, x2, y2)
                canvas_right.coords(line7, x1+15, y1, 135, 50)
                time.sleep(0.05)
            for i in range (1, 31):
                canvas_right.move(ball10, 2, -1)
                x1, y1, x2, y2 = canvas_right.coords(ball10)
                canvas_right.coords(line10, x1+15, y1, 225, 50)
                time.sleep(0.05)
            for i in range (1, 31):
                canvas_right.move(ball10, -2, +1)
                x1, y1, x2, y2 = canvas_right.coords(ball10)
                canvas_right.coords(line10, x1+15, y1, 225, 50)
                time.sleep(0.05)
            for i in range (1, 16):
                canvas_right.move(ball6, -2, -1)
                x1, y1, x2, y2 = canvas_right.coords(ball6)
                canvas_right.coords(line6, x1+15, y1, 105, 50)
                x1 += 30
                x2 += 30
                canvas_right.coords(ball7, x1, y1, x2, y2)
                canvas_right.coords(line7, x1+15, y1, 135, 50)
                time.sleep(0.05)
        except:
            break

# functions for widgets and key/mouse events
def close():
    main.destroy()
def startquiz():
    tasknrlabel.place(x = 2, y = 5)
    tasklabel.place(x = 2, y = 25)
    b_go_on.place(relx = 0.5, rely = 0.9, anchor = "s")
    task1()
def moveleft(m):
    global canvas, redball
    x1, y1, x2, y2 = canvas.coords(redball)
    x1 -= 10
    x2 -= 10
    canvas.coords(redball, x1, y1, x2, y2)
def moveright(m):
    global canvas, redball
    x1, y1, x2, y2 = canvas.coords(redball)
    x1 += 10
    x2 += 10
    canvas.coords(redball, x1, y1, x2, y2)
def moveup(m):
    global canvas, redball
    x1, y1, x2, y2 = canvas.coords(redball)
    y1 -= 10
    y2 -= 10
    canvas.coords(redball, x1, y1, x2, y2)
def movedown(m):
    global canvas, redball
    x1, y1, x2, y2 = canvas.coords(redball)
    y1 += 10
    y2 += 10
    canvas.coords(redball, x1, y1, x2, y2)
def go_on():
    # checks the user's result, counts the faults and starts the next task
    global tasknr, wrong, enter_result, result, canvas, blueball, redball, \
        hole, one, two, three, four, wrongtasks, entry_delta_p, delta_p
    if tasknr==1:
        try:
            user_result = float(enter_result.get())
            if user_result != result:
                wrong += 1
        except:
            wrong += 1
    if tasknr==2:
        x1_red, y1_red, x2_red, y2_red = canvas.coords(redball)
        x1_blue, y1_blue, x2_blue, y2_blue = canvas.coords(blueball)
        x1_hole, y1_hole, x2_hole, y2_hole = canvas.coords(hole)
        correct_angle = math.atan((y1_hole-y1_red)/(x1_hole-x1_red))
        impact_angle = math.atan((y1_blue-y1_red)/(x1_blue-x1_red))
        # Is a collision and rolling into the hole possible?
        if x1_red < 210 or x1_red > 600 or y1_red < 100 or y1_red > 150 or \
            abs(correct_angle - impact_angle) > 5:
            wrong += 1
    if tasknr==3:
        if one.get() == "true" or two.get() == "false" or \
        three.get() == "false" or four.get() == "true":
            wrong += 1
    if tasknr==4:
        try:
            delta_p_user = float(entry_delta_p.get())
            print (delta_p)
            if delta_p_user != delta_p:
                wrong += 1
        except:
            wrong += 1
    if tasknr==5 and situation.get()=="left":
        wrong += 1
    tasknr += 1
    if tasknr <= 5:
        tasknrlabel["text"] = "Aufgabe" + str(tasknr) + "/5"
        exec("task"+ str(tasknr) + "()")
    else:
        ending()

# Functions for tasks
def task1():
    # removing former widgets
    frame1.destroy()
    frame2.destroy()
    lb_welcome.destroy()
    b_start.destroy()
    b_close.destroy()
    # globalizing new objects and variables
    global result, enter_result, tasktext
    # new task: text problem
    mleft = random.randint(150, 300)
    mright = random.randint(150, 300)
    vleft = random.randint(2, 10)/10
    vright = random.randint(2, 10)/(-10)
    tasktext = "Zwei Kinder lassen ihre Spielzeugautos " \
        "frontal ineinanderkrachen. Dabei verkeilen sie sich. Die Masse des " \
        "linken Autos beträgt " + str(mleft) + " g, die des rechten " \
        + str(mright) + " g. Das linke Auto bewegt sich mit " + str(vleft) + \
        " m/s, das rechte mit " + str(vright) + " m/s. Wie gross ist die " \
        "Geschwindigkeit des rechten Autos nach dem Stoss (auf zwei " \
        "Nachkommastellen gerundet)?"
    mleft /= 1000
    mright /= 1000
    result = (vleft*mleft + vright*mright)/(mleft+mright)
    result = round(result, 2)
    # building window
    tasklabel["text"] = tasktext
    enter_result = tkinter.Entry(main, font = font_normal)
    enter_result.place(relx = 0.5, rely = 0.5, anchor = "n")
    enter_result.focus_set()

def task2():
    # removing former widgets
    enter_result.destroy()
    # globalizing new objects and variables
    global canvas, redball, blueball, hole, tasktext
    # new task: similar to billard
    tasktext = "Platziere den roten Ball mithilfe der Pfeiltasten so, " \
        "dass ihn der blaue Ball ins Loch stösst. Wenn du ihn platziert hast, "\
        "klicke auf WEITER."
    canvas = tkinter.Canvas(main, width = 800, height = 200,
        background = "white")
    redball = canvas.create_oval(50, 50, 100, 100, fill = "red")
    blueball = canvas.create_oval(160, 150, 210, 200, fill = "blue")
    hole = canvas.create_oval(600, 50, 650, 100, fill = "black")
    vector = canvas.create_line(210, 175, 280, 175, arrow = "last")
    canvas.bind("<Left>", moveleft)
    canvas.bind("<Right>", moveright)
    canvas.bind("<Up>", moveup)
    canvas.bind("<Down>", movedown)
    # building window
    tasklabel["text"] = tasktext
    canvas.place(x = 50, y = 200)
    canvas.focus_set()

def task3():
    # removing former widgets
    canvas.destroy()
    # globalizing new objects and variables
    global tasktext, one, two, three, four, check1, check2, check3, check4
    # new task: true or false statements
    tasktext = "Wähle alle zutreffenden Aussagen aus."
    statement1 = "Nach einem elastischen Stoss haben alle beteiligten " \
        "Objekte dieselbe Geschwindigkeit."
    statement2 = "Bei inelastischen Stössen wird ein Teil der Energie in " \
        "Wärme umgewandelt."
    statement3 = "Die Impulserhaltung gilt sowohl bei elastischen als auch " \
        "inelastischen Stössen."
    statement4 = "Explosionen sind Umkehrungen von elastischen Stössen."
    one = tkinter.StringVar()
    two = tkinter.StringVar()
    three = tkinter.StringVar()
    four = tkinter.StringVar()
    one.set("false")
    two.set("false")
    three.set("false")
    four.set("false")
    check1 = tkinter.Checkbutton(main, text = statement1, variable = one,
        onvalue = "true", offvalue = "false", background = "light yellow",
        font = font_normal)
    check2 = tkinter.Checkbutton(main, text = statement2, variable = two,
        onvalue = "true", offvalue = "false", background = "light yellow",
        font = font_normal)
    check3 = tkinter.Checkbutton(main, text = statement3, variable = three,
        onvalue = "true", offvalue = "false", background = "light yellow",
        font = font_normal)
    check4 = tkinter.Checkbutton(main, text = statement4, variable = four,
        onvalue = "true", offvalue = "false", background = "light yellow",
        font = font_normal)
    # building window
    tasklabel["text"] = tasktext
    check1.place(relx = 0.2, y = 175)
    check2.place(relx = 0.2, y = 200)
    check3.place(relx = 0.2, y = 225)
    check4.place(relx = 0.2, y = 250)

def task4():
    # removing former widgets
    check1.destroy()
    check2.destroy()
    check3.destroy()
    check4.destroy()
    # globalizing new objects and variables
    global delta_p, tasktext, entry_delta_p, soccerlabel, im
    # new task: impulse
    time = (random.randint(10, 100))/10000
    time = round(time, 4)
    mass = random.randint(10, 50) + 400
    velocity = round(120/3.6, 2)
    tasktext = "Timmy beschleunigt beim Elfmeterschiessen einen " + str(mass) + \
    " g schweren Fussball auf " + str(velocity) + " m/s. Der Ballkontakt " + \
    "dauert " + str(time) + " s. Wie gross ist die Impulsänderung (auf zwei " + \
    "Nachkommastellen gerundet)?"
    mass /= 1000
    delta_p = mass * (velocity/time) * time
    delta_p = round(delta_p, 2)
    entry_delta_p = tkinter.Entry(main, font = font_normal)
    # building window
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    im = tkinter.PhotoImage(file = application_path + "/Soccer.gif")
    soccerlabel = tkinter.Label(main, height = 200, width = 150, image = im,
        background = "light yellow")
    tasklabel["text"] = tasktext
    soccerlabel.place(relx = 0.5, rely = 0.2, anchor = "n")
    entry_delta_p.place(relx = 0.5, rely = 0.7, anchor = "n")
    entry_delta_p.focus_set()

def task5():
    # removing former widgets
    entry_delta_p.destroy()
    soccerlabel.destroy()
    # globalizing new objects and variables
    global tasktext, canvas_left, canvas_right, ball1, ball2, ball3, ball4, \
        ball5, ball6, ball7, ball8, ball9, ball10, line1, line2, line3, line4, \
        line5, line6, line7, line8, line9, line10, rb1, rb2, situation
    # new task: newton pendulum
    situation = tkinter.StringVar()
    situation.set("left")
    tasktext = "Welche Situation hat physikalische Fehler?"
    canvas_left = tkinter.Canvas(main, width = 320, height = 180,
        relief = "raised", borderwidth = 4, background = "white")
    canvas_right = tkinter.Canvas(main, width = 320, height = 180,
        relief = "raised", borderwidth = 4, background = "white")
    ball1 = canvas_left.create_oval(60, 85, 90, 115)
    ball2 = canvas_left.create_oval(90, 85, 120, 115)
    ball3 = canvas_left.create_oval(150, 100, 180, 130)
    ball4 = canvas_left.create_oval(180, 100, 210, 130)
    ball5 = canvas_left.create_oval(210, 100, 240, 130)
    ball6 = canvas_right.create_oval(60, 85, 90, 115)
    ball7 = canvas_right.create_oval(90, 85, 120, 115)
    ball8 = canvas_right.create_oval(150, 100, 180, 130)
    ball9 = canvas_right.create_oval(180, 100, 210, 130)
    ball10 = canvas_right.create_oval(210, 100, 240, 130)
    line1 = canvas_left.create_line(75, 85, 105, 50)
    line2 = canvas_left.create_line(105, 85, 135, 50)
    line3 = canvas_left.create_line(165, 100, 165, 50)
    line4 = canvas_left.create_line(195, 100, 195, 50)
    line5 = canvas_left.create_line(225, 100, 225, 50)
    line6 = canvas_right.create_line(75, 85, 105, 50)
    line7 = canvas_right.create_line(105, 85, 135, 50)
    line8 = canvas_right.create_line(165, 100, 165, 50)
    line9 = canvas_right.create_line(195, 100, 195, 50)
    line10 = canvas_right.create_line(225, 100, 225, 50)
    rectangle_right = canvas_right.create_rectangle(90, 50, 240, 40)
    rectangle_left = canvas_left.create_rectangle(90, 50, 240, 40)
    rb1 = tkinter.Radiobutton(main, text = "Situation links",
        variable = situation, value = "left", background = "light yellow",
        font = font_normal)
    rb2 = tkinter.Radiobutton(main, text = "Situation rechts",
        variable = situation, value = "right", background = "light yellow",
        font = font_normal)
    # building window
    tasklabel["text"] = tasktext
    canvas_left.place(relx = 0.1, rely = 0.5, anchor = "w")
    canvas_right.place(relx = 0.5, rely = 0.5, anchor = "w")
    rb1.place(relx = 0.1, rely = 0.2, anchor = "sw")
    rb2.place(relx = 0.1, rely = 0.2, anchor = "nw")
    _thread.start_new_thread(anim_task5_left, ())
    _thread.start_new_thread(anim_task5_right, ())

def ending():
    # removing former widgets
    canvas_left.destroy()
    canvas_right.destroy()
    rb1.destroy()
    rb2.destroy()
    tasknrlabel.destroy()
    tasklabel.destroy()
    b_go_on.destroy()
    # building window
    b_close = tkinter.Button(main, text = "Beenden", command = close,
        background = "firebrick", font = "Arial 14", width = 9)
    ending_label = tkinter.Label(main, background = "light yellow",
        text = "Du hast " + str(5 - wrong) + "/5 Aufgaben richtig gelöst",
        font = "Arial 14 bold")
    assessment_label = tkinter.Label(main, background = "light yellow",
        font = "Arial 30 bold")
    if wrong <= 1:
        assessment_label["text"] = "Gut gemacht!"
        assessment_label["fg"] = "forest green"
    else:
        assessment_label["text"] = "Du brauchst noch ein bisschen Übung!"
        assessment_label["fg"] = "firebrick"
    assessment_label.place(relx = 0.5, rely = 0.2, anchor = "n")
    ending_label.place(relx = 0.5, rely = 0.5, anchor = "n")
    b_close.place(relx = 0.5, rely = 0.9, anchor = "s")

# START OF MAIN PROGRAMME
# variables
tasknr = 1
wrong = 0       # faults of user
tasktext = ""   # instruction for user
windows = False # OS variable

# adapting graphics to operation system
if windows:
    font_normal = "Arial 12"
    font_bold = "Arial 12 bold"
else:
    font_normal = "Arial 14"
    font_bold = "Arial 14 bold"

# main window
main = tkinter.Tk()
main.title("Collisions and Explosions")
main.configure(background = "light yellow")
main.geometry("{}x{}".format(900, 600))

# welcome window
information1 = "1. Dieses Programm garantiert dir nicht die volle Punktzahl " \
    "in deiner Prüfung."
information2 = "2. Bitte gib alle Resultate ohne Einheiten an."
information3 = "3. Die Benutzung eines Taschenrechners wird empfohlen."
information4 = "4. Dieses Programm ist nicht perfekt. Bitte melde Bugs bei " \
    "deinem Physiklehrer."
information5 = "5. Windows: Ich entschuldige mich hiermit für die Grafik wie von 1900."
information6 = "6. Mac OSX: Ich entschuldige mich hiermit für die rucklige Animation."
frame1 = tkinter.Frame(main, width = 400, borderwidth = 5, relief = "raised",
    background = "white")
frame2 = tkinter.Frame(main, height = 200, width = 400,
    background = "light yellow")
lb_welcome = tkinter.Label(main, text = "Willkommen!",
    background = "light yellow", font = "Arial 40 bold")
lb_important = tkinter.Label(frame1, text = "Wichtig", font = font_bold,
    background = "white")
lb_information1 = tkinter.Label(frame1, text = information1, font = font_normal,
    background = "white")
lb_information2 = tkinter.Label(frame1, text = information2, font = font_normal,
    background = "white")
lb_information3 = tkinter.Label(frame1, text = information3, font = font_normal,
    background = "white")
lb_information4 = tkinter.Label(frame1, text = information4, font = font_normal,
    background = "white")
lb_information5 = tkinter.Label(frame1, text = information5, font = font_normal,
    background = "white")
lb_information6 = tkinter.Label(frame1, text = information6, font = font_normal,
    background = "white")
b_start = tkinter.Button(frame2, text = "Start", font = "Arial 14",
    command = startquiz, background = "forest green", width = 9)
b_close = tkinter.Button(frame2, text = "Beenden", font = "Arial 14",
    command = close, background = "firebrick", width = 9)
frame1.place(relx = 0.5, rely = 0.6, anchor = "s")
frame2.place(relx = 0.5, rely = 0.8, anchor = "n")
lb_welcome.place(relx = 0.5, rely = 0.1, anchor = "n")
b_start.pack(side = "left", padx = 10)
b_close.pack(side = "right", padx = 10)
lb_important.pack(side = "top")
lb_information1.pack(fill = "x")
lb_information2.pack(fill = "x")
lb_information3.pack(fill = "x")
lb_information4.pack(fill = "x")
lb_information5.pack(fill = "x")
lb_information6.pack(fill = "x")

# basic task window
tasklabel = tkinter.Label(main, font = font_normal, background = "light yellow",
    wraplength = 890)
tasknrlabel = tkinter.Label(main, text = "Aufgabe" + str(tasknr) + "/5",
    background = "light yellow", font = font_bold)
b_go_on = tkinter.Button(main, text = "Weiter", font = "Arial 14",
    command = go_on, width = 9)

main.mainloop()
