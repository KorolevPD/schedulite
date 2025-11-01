from users.models import User

EMAIL_MAX_LENGHT = User._meta.get_field('email').max_length
USERNAME_MAX_LENGHT = User._meta.get_field('username').max_length
FIRST_NAME_MAX_LENGHT = User._meta.get_field('first_name').max_length
LAST_NAME_MAX_LENGHT = User._meta.get_field('last_name').max_length
