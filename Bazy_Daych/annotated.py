from typing import Annotated

Capital = Annotated [ str, 'First letter is a capital letter']
name: Capital = 'imię'
print(type(name))
print(name)


def test (name:Capital):
    return name.capitalize()

print(test.__annotations__['name'].__metadata__)