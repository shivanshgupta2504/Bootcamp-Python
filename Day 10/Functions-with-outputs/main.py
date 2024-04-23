# Functions with outputs
def format_name(f_name, l_name):
    # Creating DocString for the function
    """
    Take first and last name and format it to return title
    case version of the name
    """
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"


print(format_name("SHIVANSH", "guPta"))



