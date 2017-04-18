import hashlib
from Tkinter import *


class Application(Frame):
    def __init__(self, parent):
        def response():
            try:
                hashvalue.delete('1.0', END)
                value = v.get()

                message = str(text.get("1.0", 'end-1c'))

                if value == 1:
                    sha1 = hashlib.sha1(message).hexdigest()

                    hashvalue.insert(INSERT, sha1)

                if value == 2:
                    sha224 = hashlib.sha224(message).hexdigest()

                    hashvalue.insert(INSERT, sha224)

                if value == 3:
                    sha256 = hashlib.sha256(message).hexdigest()

                    hashvalue.insert(INSERT, sha256)

                if value == 4:
                    sha384 = hashlib.sha384(message).hexdigest()

                    hashvalue.insert(INSERT, sha384)

                if value == 5:
                    sha512 = hashlib.sha512(message).hexdigest()

                    hashvalue.insert(INSERT, sha512)

            except ValueError:
                pass

        Frame.__init__(self, parent)
        self.parent = parent

        self.parent.title("Python SHA")
        self.pack(fill=BOTH, expand=TRUE)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side=RIGHT, fill=Y)

        textlabel = Label(frame1, text="Text", width=6)
        textlabel.pack()

        text = Text(frame1, wrap=WORD, yscrollcommand=scrollbar.set, borderwidth=3, relief="ridge")
        text.pack(side=LEFT, pady=5, padx=5, anchor=W, expand=TRUE, fill=BOTH)

        scrollbar.config(command=text.yview)

        v = IntVar()

        optionslabel = Label(frame1, text="SHA Options\n", width=15)
        optionslabel.pack()

        Radiobutton(frame1, text="SHA-1", variable=v, value='1').pack(anchor=W, padx=20)
        Radiobutton(frame1, text="SHA-224", variable=v, value='2').pack(anchor=W, padx=20)
        Radiobutton(frame1, text="SHA-256", variable=v, value='3').pack(anchor=W, padx=20)
        Radiobutton(frame1, text="SHA-384", variable=v, value='4').pack(anchor=W, padx=20)
        Radiobutton(frame1, text="SHA-512", variable=v, value='5').pack(anchor=W, padx=20)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        gethashbutton = Button(frame1, text="Get Hash", command=response)
        gethashbutton.pack(pady=15)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        hashlabel = Label(frame3, text="Hash value")
        hashlabel.pack(pady=(15,0))

        hashvalue = Text(frame3, wrap=WORD, borderwidth=3, relief="ridge")
        hashvalue.pack(side=LEFT, pady=5, padx=5, anchor=W, expand=TRUE, fill=BOTH)


def main():
    root = Tk()

    root.geometry("800x550")

    app = Application(root)

    root.mainloop()

if __name__ == '__main__':
    main()
