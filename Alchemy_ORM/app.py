import customtkinter as ctk
from alchemy_orm import Author
from ORM_Connection import Session
from sqlalchemy import select
from CTkTable import CTkTable

session = Session()


def load_authors():
    authors = session.execute(select(Author)).scalars().all()
    return [['ID', 'Imię', 'Drugie imię', 'Email', 'Login']] + \
           [[a.id, a.name, a.middle_name, a.email, a.login] for a in authors]


def refresh_table():
    global authors_table
    authors_data = load_authors()

    authors_table.destroy()
    authors_table = CTkTable(master=app_content, row=len(authors_data),
                             column=len(authors_data[0]), values=authors_data)
    authors_table.grid(row=0, column=0, padx=10, pady=10, sticky='ew')


def add_author():
    def save_new_author():
        if not name_entry.get() or not email_entry.get() or not login_entry.get():
            print("Uzupełnij wymagane pola!")
            return

        new_author = Author(
            name=name_entry.get(),
            middle_name=middle_name_entry.get(),
            email=email_entry.get(),
            login=login_entry.get()
        )
        session.add(new_author)
        session.commit()
        add_window.destroy()
        refresh_table()

    add_window = ctk.CTkToplevel(app)
    add_window.title("Dodaj autora")
    add_window.geometry("400x300")

    ctk.CTkLabel(add_window, text="Imię *").pack(pady=5)
    name_entry = ctk.CTkEntry(add_window)
    name_entry.pack()

    ctk.CTkLabel(add_window, text="Drugie imię").pack(pady=5)
    middle_name_entry = ctk.CTkEntry(add_window)
    middle_name_entry.pack()

    ctk.CTkLabel(add_window, text="Email *").pack(pady=5)
    email_entry = ctk.CTkEntry(add_window)
    email_entry.pack()

    ctk.CTkLabel(add_window, text="Login *").pack(pady=5)
    login_entry = ctk.CTkEntry(add_window)
    login_entry.pack()

    save_button = ctk.CTkButton(add_window, text="Zapisz", command=save_new_author)
    save_button.pack(pady=15)


if __name__ == '__main__':
    app = ctk.CTk()
    app.title('Biblioteka')
    app.geometry('1024x700')

    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=1)

    menu_bar = ctk.CTkFrame(app, corner_radius=20)
    menu_bar.grid_columnconfigure(0, weight=1)
    menu_bar.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

    app_title = ctk.CTkLabel(menu_bar, text='Biblioteka', font=ctk.CTkFont(size=15, weight='bold'))
    app_title.grid(row=0, column=0, padx=25, pady=10, sticky='w')

    add_author_button = ctk.CTkButton(menu_bar, text='Dodaj autora', command=add_author)
    add_author_button.grid(row=0, column=1, padx=25, pady=10)

    app_content = ctk.CTkFrame(app)
    app_content.grid_columnconfigure(0, weight=1)
    app_content.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    authors_table = CTkTable(master=app_content, row=0, column=0, values=[[]])  # Placeholder
    refresh_table()

    app.mainloop()
