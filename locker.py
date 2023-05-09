import os
import tkinter as tk
from tkinter import messagebox, filedialog

# define password
PASSWORD = "password"

class App:
    def __init__(self, root):
        self.root = root
        self.locked_dirs = []

        # create widgets
        self.add_dir_button = tk.Button(root, text="Add Directory", command=self.add_dir)
        self.remove_dir_button = tk.Button(root, text="Remove Directory", command=self.remove_dir)
        self.lock_dirs_button = tk.Button(root, text="Lock Directories", command=self.lock_dirs)
        self.unlock_dirs_button = tk.Button(root, text="Unlock Directories", command=self.unlock_dirs)

        # layout widgets
        self.add_dir_button.pack()
        self.remove_dir_button.pack()
        self.lock_dirs_button.pack()
        self.unlock_dirs_button.pack()

        # ask for password to unlock directories
        self.password = None
        self.unlock_dirs()

    def add_dir(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.locked_dirs.append(dir_path)
            messagebox.showinfo("Success", f"{dir_path} added to locked directories.")

    def remove_dir(self):
        if self.locked_dirs:
            dir_path = self.locked_dirs[-1]
            self.locked_dirs = self.locked_dirs[:-1]
            messagebox.showinfo("Success", f"{dir_path} removed from locked directories.")
        else:
            messagebox.showinfo("Error", "No directories to remove.")

    def lock_dirs(self):
        if self.password != PASSWORD:
            messagebox.showinfo("Error", "Incorrect password.")
            return

        for dir_path in self.locked_dirs:
            os.system(f"attrib +h {dir_path}")

        messagebox.showinfo("Success", "Directories locked.")

    def unlock_dirs(self):
        password = tk.simpledialog.askstring("Password", "Enter password to unlock:")
        if password != PASSWORD:
            messagebox.showinfo("Error", "Incorrect password.")
            return

        self.password = password
        for dir_path in self.locked_dirs:
            os.system(f"attrib -h {dir_path}")

        messagebox.showinfo("Success", "Directories unlocked.")

    def on_close(self):
        self.lock_dirs()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: App.on_close(App))
    app = App(root)
    root.mainloop()