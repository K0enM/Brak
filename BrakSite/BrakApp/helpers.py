import json


def get_form_class(Form):
    config = open("C:\\Users\\koenm\\PycharmProjects\\Brak\\BrakSite\\BrakApp", "r")
    styles = json.load(config)
    return styles[Form]
