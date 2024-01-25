from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("665x400+550+250")
        self.master.resizable(0, 0)
        self.master.configure(bg="#B5E5CF")

        self.init_database()
        self.init_ui()

    def init_database(self):
        self.connection = sql.connect('listOfTasks.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('create table if not exists tasks (title text)')
        self.tasks = []
        self.retrieve_database()

    def init_ui(self):
        functions_frame = Frame(self.master, bg="#8EE5EE")
        functions_frame.pack(side="top", expand=True, fill="both")

        task_label = Label(functions_frame, text="To-Do LIST \n Enter the task Title:",
                           font=("blue", "14", "bold"),
                           background="#8EE5EE",
                           foreground="#FF6103")
        task_label.place(x=20, y=30)

        self.task_field = Entry(
            functions_frame,
            font=("Arial", "14"),
            width=42,
            foreground="black",
            background="pink",
        )
        self.task_field.place(x=180, y=30)

        add_button = Button(
            functions_frame,
            text="Add",
            width=15,
            bg='#D4AC0D', font=("arial", "14", "bold"),
            command=self.add_task,
        )

        del_button = Button(
            functions_frame,
            text="Remove",
            width=15,
            bg="#D4AC0D", font=("Arial", "14", "bold"),
            command=self.delete_task,
        )

        del_all_button = Button(
            functions_frame,
            text="Delete All",
            width=15,
            bg="red", font=("arial", "14", "bold"),
            command=self.delete_all_tasks
        )

        exit_button = Button(
            functions_frame,
            text="Exit/Close",
            width=52,
            bg="green",
            font=("arial", "14", "bold"),
            command=self.close
        )

        add_button.place(x=18, y=80)
        del_button.place(x=240, y=80)
        del_all_button.place(x=17, y=330)

        self.task_listbox = Listbox(
            functions_frame,
            width=70,
            height=9,
            font="bold",
            selectmode="SINGLE",
            background="WHITE",
            foreground="BLACK",
            selectbackground="#FF8C00",
            selectforeground="BLACK"
        )
        self.task_listbox.place(x=17, y=140)

        self.retrieve_database()
        self.list_update()

        exit_button.place(x=17, y=370)

    def add_task(self):
        task_string = self.task_field.get()
        if len(task_string) == 0:
            messagebox.showinfo('Error', 'Field is empty')
        else:
            self.tasks.append(task_string)
            self.cursor.execute('insert into tasks values (?)', (task_string,))
            self.list_update()
            self.task_field.delete(0, 'end')

    def list_update(self):
        self.clear_list()
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    def delete_task(self):
        try:
            the_value = self.task_listbox.get(self.task_listbox.curselection())
            if the_value in self.tasks:
                self.tasks.remove(the_value)
                self.list_update()
                self.cursor.execute('delete from tasks where title = ?', (the_value,))
        except TclError:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

    def delete_all_tasks(self):
        message_box = messagebox.askyesno('Delete All', 'Are you sure?')
        if message_box:
            while len(self.tasks) != 0:
                self.tasks.pop()
            self.cursor.execute('delete from tasks')
            self.list_update()

    def clear_list(self):
        self.task_listbox.delete(0, 'end')

    def close(self):
        print(self.tasks)
        self.master.destroy()

    def retrieve_database(self):
        while len(self.tasks) != 0:
            self.tasks.pop()
        for row in self.cursor.execute('select title from tasks'):
            self.tasks.append(row[0])

    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    root = Tk()
    app = ToDoListApp(root)
    root.mainloop()
