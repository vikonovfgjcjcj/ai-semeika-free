import tkinter as tk
import webbrowser

class SimpleOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Моя Семейка ОС")
        self.root.geometry("600x400")
        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Добро пожаловать!
Используйте клавиши:
"
                                              "B - браузер
"
                                              "C - калькулятор
"
                                              "Esc - выход", font=("Arial", 14))
        self.label.pack(pady=20)

        self.output = tk.Text(self.root, height=10, width=50)
        self.output.pack(pady=10)

        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=5)

    def bind_keys(self):
        self.root.bind('<b>', self.open_browser)
        self.root.bind('<c>', self.open_calculator)
        self.root.bind('<Escape>', self.exit_os)

    def open_browser(self, event=None):
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, "Открытие браузера...
")
        webbrowser.open("https://www.google.com")

    def open_calculator(self, event=None):
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, "Введите выражение для вычисления и нажмите Enter:
")
        self.entry.focus()

        def calculate(event):
            expr = self.entry.get()
            try:
                result = eval(expr)
                self.output.insert(tk.END, f"{expr} = {result}
")
            except Exception as e:
                self.output.insert(tk.END, f"Ошибка: {e}
")
            self.entry.delete(0, tk.END)

        self.entry.bind('<Return>', calculate)

    def exit_os(self, event=None):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleOS(root)
    root.mainloop()
