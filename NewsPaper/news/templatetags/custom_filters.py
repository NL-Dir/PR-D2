from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    stop_words = {'ipsum', 'incididunt', 'commodo', 'occaecat', 'aute'}
    if isinstance(value, str):
        for word in stop_words:
            value = value.replace(word, '*' * len(word))
        return value
    else:
        raise ValueError(f'Невозможно применить censor к {type(value)}')