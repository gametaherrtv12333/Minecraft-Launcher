import customtkinter
import minecraft_launcher_lib
import tkinter.messagebox
import subprocess
from customtkinter import *
import customtkinter as Ctk
import os
from random_username.generate import generate_username
import webbrowser

class App(Ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("760x450")
        self.title("PvpLauncher - by LUVIK")
        self.resizable(width=False, height=False)
        customtkinter.set_default_color_theme("green")

        #Username label
        self.usernameLbl = Ctk.CTkLabel(master=self ,text="Login in your minecraft account", font=("Century Gothic", 22))
        self.usernameLbl.pack(pady=(10,1))

        #Получение имени пользователя
        self.Username = Ctk.CTkEntry(master=self,placeholder_text="Username", width=350, font=("Roboto", 20))
        self.Username.pack(pady=(10,1))

        with open("data/username.txt", "r") as name:
                self.Username.delete(0, tkinter.END)
                self.Username.insert(0, name.read())

        User_Ram = CTkEntry(master=self, placeholder_text="RAM(GB)", width=140,font=("Roboto", 15))
        names1 = ""

        def start_minecraft():
            if self.Username.get() != "":
                if User_Ram.get() == "":
                    options = {
                        'username': self.Username.get(),  # Username
                        "jvmArguments": [f"-Xmx4G", f"-Xms4G"],
                        # Аргументы Jvm / Выставление обьема оперативной памяти
                    }
                else:
                    RAM = User_Ram.get()
                    RAM *= 10
                    options = {
                        'username': self.Username.get(),  # Username
                        "jvmArguments": [f"-Xmx{RAM}", f"-Xms{RAM}"],
                        # Аргументы Jvm / Выставление обьема оперативной памяти
                    }

                with open("data/username.txt", "w") as names:
                    data = self.Username.get()
                    names.write(data)
                self.destroy()
                subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version="1.19.4-forge-45.2.15",minecraft_directory=".launcher", options=options))

        #Функция рандомного никнейма
        def add_random_username():
                random_userName = generate_username(1)
                self.Username.delete(0, tkinter.END)
                self.Username.insert(0, random_userName)

        #Запуск майнкрафт
        self.start_button = CTkButton(master=self, text="Start Game", command=start_minecraft, font=("Century Gothic", 16), fg_color="#38612d")
        self.start_button.pack(pady=(15,1))

        #Пользовательское выделение памяти
        User_Ram.pack(pady=(10,1))

        #Add random username
        self.random_username = Ctk.CTkButton(master=self, text="Add random username ", command=add_random_username, font=("Roboto", 14), fg_color="#38612d")
        self.random_username.place(x=43,y=50)

        #Add random username
        self.reports = Ctk.CTkButton(master=self, text="Send Reports", command=lambda: webbrowser.open("https://forms.yandex.ru/u/665b011e2530c20dd94d3702/"), font=("Roboto", 15), fg_color="#38612d")
        self.reports.place(x=559,y=50)

app = App()
app.mainloop()