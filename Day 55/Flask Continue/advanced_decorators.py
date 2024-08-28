class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper

# Now what I want is to decorate this function
# To add the functionality of running this function only when user is logged in
@is_authenticated_decorator
def create_bolg_post(user):
    print(f"This is {user.name}'s new blog post!")


user = User("Shivansh")
user.is_logged_in = True
create_bolg_post(user)