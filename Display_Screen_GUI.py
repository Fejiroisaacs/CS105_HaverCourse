from tkinter import *
from tkinter import ttk
from Sort_Functions import send_all_sorted_courses
from Sort_Functions import send_checked_categories
import tkinter.font as font


# makes the gui that has a scrollable window
def create_scroll():
    """
    Pre-condition:
        tkinter is properly imported and the window is made
        the user selects options from the domain and level label and clicks the submit button
        the preceding functions work

    .pack(): displays the label on the screen


    Post-conditions:
        the gui screen is properly made and the right information is printed on the screen
    """
    # creating the main gui window
    window2 = Tk()
    window2.title('Display')  # setting the title of the gui
    window2.configure(bg='#FFC772')  # setting the background color of the gui
    width, height = window2.winfo_screenwidth(), window2.winfo_screenheight()  # gets the width and height of screen
    window2.geometry('%dx%d+0+0' % (width, height))  # sets the gui to the width and height of the screen

    # Create A Main Frame
    main_frame = Frame(window2)
    main_frame.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)

    # setting the color
    my_canvas.configure(bg='#FFC772')
    second_frame.configure(bg='#FFC772')
    main_frame.configure(bg='#FFC772')

    # binding mouse wheel
    my_canvas.bind_all('<MouseWheel>', lambda event: my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # getting the sorted lists and the lists that tell us which domain and level has been selected
    checked_domain = send_checked_categories()[0]
    checked_level = send_checked_categories()[1]
    combined_lvl_dom = send_all_sorted_courses()

    # creating descriptions for the info displayed on the screen
    description = ['Subject', 'Catalog Nbr', 'Title', 'Description', 'Attribute']
    domains = ["A", "B", "C"]
    level = ["0 Level", "100 level", "200 level", '300+ level']

    # creating the font of text displayed on the screen
    my_font_dom = font.Font(family='Varela', size=50)
    my_font_disp = font.Font(family='Times New Roman', size=30)

    # prints the appropriate info selected by the user
    for i in range(len(domains)):  # goes over the domains
        if checked_domain[i]:  # checks if that domain checkbox has been checked
            # making the title of the course domain i.e. Domain A, Domain B, Domain C
            title_label = Label(second_frame, text=f"Domain {domains[i]}", anchor=NW, padx=200, pady=20, bg='#FFC772')
            title_label['font'] = my_font_dom  # setting the font to our font
            title_label.pack()  # displaying it on the screen

            # goes over the levels
            for j in range(len(level)):
                if checked_level[j]:  # checks if the level has been checked
                    # goes over the courses in the level of selected domain
                    for k in range(len(combined_lvl_dom[i][j])):
                        for info in combined_lvl_dom[i][j][k]:  # goes over each course in the list
                            for n in range(len(info)):  # goes over the details of each course
                                description_label = Label(second_frame, text=f"{description[n]}:"
                                                                             f"  {remove_nl(info[n])}", padx=10,
                                                          wraplength=1500, border=10, anchor=NW, bg='#FFC772')
                                # setting the font of the displayed info
                                description_label['font'] = my_font_disp
                                description_label.pack(fill=BOTH, expand=1)

                        # making a blank space for better organization of displayed info
                        make_space = Label(second_frame, pady=10, bg='#FFC772')
                        make_space.pack()

    window2.mainloop()


# allowing the mouse scroll to scroll the gui: function gotten online - cited in the project report
def _on_mousewheel(self, event):
    self.canvas.yview_scroll(-1*(event.delta/120), "units")


# removes the \n from value: function gotten online - cited in the project report
def remove_nl(value):
    return ''.join(value.splitlines())
