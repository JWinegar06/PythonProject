import tkinter as tk
from main import fetch_movies

root = tk.Tk()
root.title("Movie Scraper")
root.geometry("400x500")

movies = []

# Listbox
listbox = tk.Listbox(root)
listbox.pack(fill="both", expand=True)

# Fetch function
def fetch():
    global movies
    movies = fetch_movies()

    listbox.delete(0, tk.END)
    for m in movies:
        listbox.insert(tk.END, m)



# Buttons
tk.Button(root, text="Fetch Movies", command=fetch).pack()


root.mainloop()