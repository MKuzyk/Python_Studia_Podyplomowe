class Books:

    def __init__(self, title_name, author_name, year_of_release):
        self.__title_name = title_name
        self.__author_name = author_name
        self.__year_of_release = year_of_release


    def get_title_name(self):
        return self.__title_name

    def get_author_name(self):
        return self.__author_name

    def get_year_of_release(self):
        return self.__year_of_release

books_list=[]

books_list.append(Books("Pan Tadeusz", "Adam Mickiewicz", "1800"))
books_list.append(Books("Potop", "Henryk Sienkiewicz", "1886"))
books_list.append(Books("Wladca Pierćieni", "J R R Tolkien", "1954"))

for Books in books_list:
    print("Tytuł: ", Books.get_title_name(),", Autor: ", Books.get_author_name()," Rok wydania: ", Books.get_year_of_release())