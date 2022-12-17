from tkinter import *
from Sort_Functions import is_checked
from Sort_Functions import read_data
import tkinter.font as font
from Display_Screen_GUI import create_scroll

# creating the gui and setting it to full screen
window = Tk()
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width, height))


# making the gui
def gui() -> None:
    """
    Pre-condition:
        tkinter is properly imported and the window is made

    my_font: font - Varela
    my_header: label
    submit_button: button

    Post-conditions:
        The window screen is properly made and displays all the labels and checkboxes
    return: None
    """
    global window
    window.configure(bg='#FFC772')  # setting the color of the gui
    window.title("HaverCourse")  # setting the title of the gui
    my_font = font.Font(family='Valera', size=55)  # making a my_font variable to store the font for the gui

    my_header = Label(text="HaverCourse", bg='#FFC772', pady=20)  # creating a header Label
    my_header['font'] = my_font  # setting the font to our selected font
    my_header.pack()  # displays the header label on the screen

    domains()  # call to the domain function which creates the checkboxes for the domains
    levels()  # call to the domain function which creates the checkboxes for the levels

    submit_button = Button(window, text='Submit', bg='#FFAE30', fg='#ffffff', font='Varela',
                           command=create_scroll)
    # creating the submit button
    window.bind("<Return>", lambda event: create_scroll())  # making the enter key do the same as the submit button
    submit_button.pack(side=BOTTOM, anchor="e", padx=10, pady=10)  # places the submit button at the bottom of the gui

    window.mainloop()  # makes the gui stay active while waiting for user actions


# making the labels and checkboxes for the domains
def domains() -> None:
    """
    Pre-condition:
        tkinter is properly imported and the window is made and the previous information that should be printed
        before the domains has been printed

    my_font: font - Varela
    my_header: label
    a_var, b_var, and c_var: variables that hold 1 or 0 depending on the status of the checkboxes (checked/unchecked)

    .is_checked(): keeps track of whether the checkbox is checked/unchecked
    .deselect(): sets the checkboxes to initially be deselected
    .pack(): displays the label on the screen

    Post-conditions:
        The domain label and checkboxes are accurately packed on the screen
    return: None
    """
    my_font = font.Font(family='Varela', size=15)

    my_header = Label(text="Domains", bg='#FFC772', pady=20)  # makes the domain label
    my_header_font = font.Font(family='Varela', size=30)
    my_header['font'] = my_header_font  # sets the font of the label
    my_header.pack()  # displays the label on the screen

    a_var = IntVar()  # holds 1 if the checkbox is checked and 0 otherwise
    a = Checkbutton(window, text="A: Meaning, Interpretation, and Creative Expression",
                    variable=a_var, bg='#FFC772', command=lambda: is_checked(0, a_var.get(), "domain"))
    a['font'] = my_font
    a.deselect()
    a.pack()

    b_var = IntVar()
    b = Checkbutton(window, text="B: Analysis of the Social World: Individuals, Institutions, and Cultures",
                    variable=b_var, bg='#FFC772', command=lambda: is_checked(1, b_var.get(), "domain"))
    b['font'] = my_font
    b.deselect()
    b.pack()

    c_var = IntVar()
    c = Checkbutton(window, text="C: Physical and Natural Process, Mathematical and Computational Constructs",
                    variable=c_var, bg='#FFC772', command=lambda: is_checked(2, c_var.get(), "domain"))
    c['font'] = my_font
    c.deselect()
    c.pack()


# making the label/widgets for the levels
def levels() -> None:
    """
    Pre-condition:
        tkinter is properly imported and the window is made and the previous information that should be printed
        before the domains has been printed

    my_font: font - Varela
    my_header: label
    zero_var, one_var, two_var, and three_var:
        variables that hold 1 or 0 depending on the status of the checkboxes (checked/unchecked)

    .is_checked(): keeps track of whether the checkbox is checked/unchecked
    .deselect(): sets the checkboxes to initially be deselected
    .pack(): displays the label on the screen

    Post-conditions:
        The levels label and checkboxes are accurately made and packed on the screen
    return: None
    """
    my_font = font.Font(family='Varela', size=15)

    my_header = Label(text="Level", bg='#FFC772', pady=20)  # makes the domain label
    my_header_font = font.Font(family='Varela', size=30)
    my_header['font'] = my_header_font  # sets the font of the label
    my_header.pack()

    zero_var = IntVar()  # holds 1 if the checkbox is checked and 0 otherwise
    zero = Checkbutton(window, text="000", variable=zero_var, bg='#FFC772',
                       command=lambda: is_checked(0, zero_var.get(), "level"))  # making the checkbox
    # call to the is_checked function to keep track of whether the function has been clicked or not
    zero['font'] = my_font
    zero.deselect()
    zero.pack()

    one_var = IntVar()
    one = Checkbutton(window, text="100", variable=one_var, bg='#FFC772',
                      command=lambda: is_checked(1, one_var.get(), "level"))
    one['font'] = my_font
    one.deselect()
    one.pack()

    two_var = IntVar()
    two = Checkbutton(window, text="200", variable=two_var, bg='#FFC772',
                      command=lambda: is_checked(2, two_var.get(), "level"))
    two['font'] = my_font
    two.deselect()
    two.pack()

    three_var = IntVar()
    three = Checkbutton(window, text="300+", variable=three_var, bg='#FFC772',
                        command=lambda: is_checked(3, three_var.get(), "level"))
    three['font'] = my_font
    three.deselect()
    three.pack()


if __name__ == "__main__":
    read_data('courses_fixed.csv')  # makes the initial call for the data to be read
    gui()  # displays the gui
