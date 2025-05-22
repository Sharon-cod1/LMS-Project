from django import template




# Register the template tag library
# This is a custom template tag library for checking user roles
register = template.Library()

@register.simple_tag()
def convert_uppercase(text):

    return text.upper()


@register.simple_tag()
def user_role_checking(request,roles):

    roles=roles.split(',')

    print(roles)

    if request.user.is_authenticated and request.user.role in roles:

        return True
    
    return False