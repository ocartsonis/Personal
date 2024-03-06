import tkinter as tk
import ClientToServer as cs

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Initialize container for pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Define the pages
        for F in (HomePage, StartSessionPage, JoinSessionPage, SessionPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        cs.authenticate_with_spotify()
        self.controller = controller

        label = tk.Label(self, text="Home Page")
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Start Session", command=lambda: controller.show_frame("StartSessionPage"))
        button.pack()

        button2 = tk.Button(self, text="Join Session", command=lambda: controller.show_frame("JoinSessionPage"))
        button2.pack()

class JoinSessionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Join Session")
        label.pack(side="top", fill="x", pady=10)

        session_name_label = tk.Label(self, text="Session Name:")
        session_name_label.pack(side="top", fill="x", pady=10)

        self.text_box = tk.Entry(self)
        self.text_box.pack()

        accept_button = tk.Button(self, text="Accept", command=self.continue_to_next_page)
        accept_button.pack()

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame("HomePage"))
        back_button.pack()
    def continue_to_next_page(self):
        session_name = self.text_box.get()
        print("Session Name entered:", session_name)
        cs.join_session(session_name)
        self.controller.show_frame("SessionPage")

class StartSessionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Start Session")
        label.pack(side="top", fill="x", pady=10)

        session_name_label = tk.Label(self, text="Session Name:")
        session_name_label.pack(side="top", fill="x", pady=10)

        self.text_box = tk.Entry(self)
        self.text_box.pack()

        accept_button = tk.Button(self, text="Accept", command=self.continue_to_next_page)
        accept_button.pack()

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame("HomePage"))
        back_button.pack()
    def continue_to_next_page(self):
        session_name = self.text_box.get()
        print("Session Name entered:", session_name)
        cs.create_session(session_name)
        self.controller.show_frame("SessionPage")

class SessionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


