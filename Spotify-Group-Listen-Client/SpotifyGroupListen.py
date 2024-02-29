import ClientToServer as cs
import ClientFrontend as cf

if __name__ == "__main__":
    app = cf.SampleApp()
    app.title("Listen Together")
    app.geometry("400x300")
    app.mainloop()
