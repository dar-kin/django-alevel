from django import template
from random import randint, choice
from string import ascii_lowercase


register = template.Library()


@register.simple_tag(name="rand_int")
def rand_int():
    return randint(5, 10)


@register.simple_tag(name="rand_slug")
def rand_slug():
    n = randint(5, 10)
    return ''.join(choice(ascii_lowercase) for _i in range(n))
