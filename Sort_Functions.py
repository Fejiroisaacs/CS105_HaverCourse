from typing import List
import csv

# initializing the lists that keep track of when each checkbox has been checked
checked_levels = [False, False, False, False]
checked_domains = [False, False, False]

# initializing the sorted lists of all the domains
domain_a_lvl_courses: List[List[List[str]]] = []
domain_b_lvl_courses: List[List[List[str]]] = []
domain_c_lvl_courses: List[List[List[str]]] = []


# reads the data file
def read_data(file_name: str) -> None:
    """
        pre-condition:
            file is not empty

        file: file_handler
            acts as a handler for the file that is being transformed to a List[List[str]]

        return - None
        post-condition:
            filters the data by taking out all the courses that have no domain
            sorts the courses into the correct domain lists
    """
    file = open(file_name, "r", encoding="utf8")
    data = list(csv.reader(file, delimiter=","))
    file.close()
    sort_domains(domain_list_filter_1(data))  # removes unnecessary courses found in the list that have no domain,
    # then sorts the data into domains


# takes three parameters, the position, checked status(1 or 0), category of checked - because we use this function to
# check both the domains and levels
def is_checked(pos: int, val: int, category: str) -> None:
    """
    Pre-conditions:
        pos is valid - a valid position in either the domain or level list
        the .get() function returns either 0 or 1
        category is either domain or level

    pos: int
        position of the category in the list
    val: int
        1(checked) or 0(unchecked) depending on state of checkbox
    category: str
        level or domain

    Post-conditions:
        accurately updates the checked_domains and checked_levels list to show which boxes are checked/unchecked
    return: None
        updates global variables
    """
    global checked_levels  # making the global checked_levels variable accessible by this function
    global checked_domains

    if val == 1:  # assigns True to 1 and False to 0 (val would be 1 if the checkbox has been checked and 0 otherwise)
        has_been_checked = True
    elif val == 0:
        has_been_checked = False
    else:
        # should never be an issue but just incase the .get() function doesn't return 1 or 0
        raise Exception("problem with checkbox value.get() check command in domain/level lambda call")

    # checks which category needs to be updated and updates it
    if category == "level":
        checked_levels[pos] = has_been_checked
    elif category == "domain":
        checked_domains[pos] = has_been_checked
    else:
        raise Exception("invalid category")


# gets rid of problematic courses in the list - those with no domains
def domain_list_filter_1(data_list: List[List[str]]) -> List[List[str]]:
    """
    Pre-conditions:
        data_list is a List[List[str]]

    data_list: List[List[str]]
        contains the initial unfiltered list of all the courses
    filtered_list: List[List[str]]
        contains the list of courses that have domains

    Post-conditions:
        returns a list that contains courses that have domains
    return: List[List[str]]
    """
    filtered_list = []
    for j in range(len(data_list)):
        try:
            if data_list[j][4][0] != "":
                filtered_list.append(data_list[j])  # adds the list that has domains in the filtered_list
        except IndexError:
            pass  # ignores Index error

    return filtered_list


def sort_domains(data) -> None:
    """
    Pre-condition:
        data contains courses that have a domain

    domain_a_courses
        contains courses that are only a domain
    domain_b_courses
        contains courses that are only b domain
    domain_c_courses
        contains courses that are only c domain
    abandoned_courses
        contains courses that don't have a domain

    Post-condition:
        data is properly sorted into the right domains
    return: none
    """
    # making the global variables accessible by this function
    global domain_a_lvl_courses
    global domain_b_lvl_courses
    global domain_c_lvl_courses

    # creating the lists that initially holds the unsorted domain courses
    domain_a_courses = []
    domain_b_courses = []
    domain_c_courses = []
    abandoned_courses = []

    # sorting the courses into domains
    for sub_data in data:
        if sub_data[4][0] == "A":
            domain_a_courses.append(sub_data)
        elif sub_data[4][0] == "B":
            domain_b_courses.append(sub_data)
        elif sub_data[4][0] == "C":
            domain_c_courses.append(sub_data)
        else:
            abandoned_courses.append(sub_data)

    # adds all the abandoned courses to the domain c courses ( quantitative and symbolic reasoning courses)
    for course in abandoned_courses:
        domain_c_courses.append(course)

    # updating the domain level courses list to have the
    # sorted courses - 000, 100, 200, 300+ - in each index of the list
    domain_a_lvl_courses = domain_lvl_sort(domain_a_courses)
    domain_b_lvl_courses = domain_lvl_sort(domain_b_courses)
    domain_c_lvl_courses = domain_lvl_sort(domain_c_courses)


# sorts each domain list in the order 000, 100, 200, 300+
def domain_lvl_sort(list_courses) -> List[List[List[str]]]:
    """
        Precondition:
            the list_courses contains only courses of the same domain

        hold_course_list: holds the list of courses being sorted

        Postcondition:
            the returned list is a list sorted according to course levels
        return: List[List[List[str]]]
    """
    hold_course_list: List[List[List[str]]] = [[], [], [], []]

    for sub_data in list_courses:
        if str(sub_data[1][1]) == '0':
            hold_course_list[0].append([sub_data])
        elif sub_data[1][1] == "1":
            hold_course_list[1].append([sub_data])
        elif sub_data[1][1] == "2":
            hold_course_list[2].append([sub_data])
        elif sub_data[1][1] == "3" or sub_data[1][1] == "4":
            hold_course_list[3].append([sub_data])

    return hold_course_list


# way to transfer these global variables to other modules/files
def send_all_sorted_courses():
    """
    Pre-condition:
        domain_a_lvl_courses, domain_b_lvl_courses, and domain_c_lvl_courses are accurately updated
    return: List[List[List[List[str]]], List[List[List[str]]], List[List[List[str]]]]
    """
    return [domain_a_lvl_courses, domain_b_lvl_courses, domain_c_lvl_courses]


def send_checked_categories() -> tuple:
    """
    Pre-condition:
        checked_domains and checked_levels are accurately updated
    return: tuple(List[bool], List[bool])
    """

    return checked_domains, checked_levels
