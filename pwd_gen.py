#!/Users/quoc-thongnguyen/conda/miniconda3/envs/py39/bin/python3
import tkinter as tk
import random
# from faker import Faker


def generate_password(length: int, seed_seq) -> str:
    random.seed(seed_seq)
    # list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_"
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*()_"
    selected_char = random.sample(list_of_chars, length)
    pass_str = "".join(selected_char)
    return pass_str


class GUI:
    def __init__(self):
        # create the main window
        self.main_window = tk.Tk()
        self.main_window.title('Password Generator')
        self.main_window.geometry('400x250')
        # self.main_window.configure(bg='#333333')

        # create frames
        self.string = tk.Frame(self.main_window)  # input string
        self.length = tk.Frame(self.main_window)  # input length
        self.passwd = tk.Frame(self.main_window)  # output password
        self.button = tk.Frame(self.main_window)  # buttons

        # create the widget for the input frames
        self.prompt_str = tk.Label(self.string, text='Add string to generate:')
        self.str_entry = tk.Entry(self.string, width=20)
        self.prompt_len = tk.Label(self.length, text='Add desired length (default 15):')
        self.len_entry = tk.Entry(self.length, width=20)

        # pack those input frames widgets
        self.prompt_str.pack()
        self.str_entry.pack()
        self.prompt_len.pack()
        self.len_entry.pack()

        # create widget for output values
        self.value = tk.StringVar()
        self.output_pw = tk.Entry(self.passwd, text=self.value, bd=0, bg="systemButtonFace")

        # self.value = tk.StringVar()
        # self.output_pw = tk.Label(self.passwd, textvariable=self.value)

        # pack the output frame widgets
        self.output_pw.pack(side='left')

        # make the bottoms
        self.gen = tk.Button(self.button, text='Generate', command=self.gen_pass)
        self.copy = tk.Button(self.button, text='Copy to clipboard', command=self.clipper)
        self.quit = tk.Button(self.button, text='Quit', command=self.main_window.destroy)

        # pack the bottoms
        self.gen.pack(side='left')
        self.copy.pack(side='left')
        self.quit.pack(side='left')

        # pack all frames
        self.string.pack()
        self.length.pack()
        self.passwd.pack()
        self.button.pack()
        
        # start the main loop
        tk.mainloop()

    def gen_pass(self) -> None:
        get_string = self.str_entry.get()
        get_length = self.len_entry.get()
        if (not get_length.isdecimal()) or (int(get_length) < 4):
            get_length = 15
        # Faker.seed(int.from_bytes(get_string.encode('utf-8'), 'little'))
        # pwd = Faker().password(int(get_length))
        pwd = generate_password(int(get_length), seed_seq=get_string) #comment this to get the faker algo
        self.value.set(pwd)

    def clipper(self) -> None:
        self.main_window.clipboard_clear()
        self.main_window.clipboard_append(self.output_pw.get())


def main() -> None:
    GUI()


if __name__ == '__main__':
    main()
