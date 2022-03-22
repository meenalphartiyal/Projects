from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("Spam Email Detector")
root.iconbitmap('mail_icon.ico')
root.geometry("1252x726")

# Defining Heading Font Style
headingFont = Font(
    family="Georgia",
    size=40,
    weight="bold"
)

# Defining Body Font Style
bodyFont = Font(
    family="Lucida Console",
    size=10
)

# Defining Button Font Style
btnFont = Font(
    family="Lucida Console",
    weight="bold"
)

# Defining Heading Font Style
answerFont = Font(
    family="Georgia",
    size=50,
    weight="bold"
)

# Background Image
my_img = PhotoImage(file="Background.png")
frame = Label(root, image=my_img)
frame.place(x=0, y=0)

# Heading
heading = Label(root, text="Spam Detection", font=headingFont, fg="#DFDFDF", bg="#2B3032")
heading.place(x=85, y=50)

# Message from Creator
creator_message = f"""With an Accuracy score of something%,\n
Check if the Email you type is Spam or Not.\n 
This Application is trained to evaluate if an \n
email is spam or not spam (ham).\n 
The model has been trained on a dataset of over \n
5000 emails including both 'Spam' and 'not Spam'\n
Please enter the email below in the text field and \n
then click on Check button."""

info = Label(text=creator_message, width=60, height=18, bg="#404244", fg="#DFDFDF", font=bodyFont, bd=2, relief=SOLID)
info.place(x=65, y=150)

# User Input
email = Text(width=58, height=15, fg="#404244", padx=10, pady=10, font=bodyFont, bd=3, relief=SUNKEN)
email.place(x=65, y=420)


# Result Button
def OnClick():
    email.get("1.0", "end")
    res = "Spam"
    answer = Label(text=res, bg="#1E2122", fg="#DFDFDF", font=answerFont)
    answer.place(x=830, y=310)


    def again():
        email.delete("1.0", "end")
        answer.destroy()

    tryAgain_btn = Button(text="TRY AGAIN", width=15, height=2, font=btnFont, command=again)
    exit_btn = Button(root, text="EXIT", width=15, height=2, font=btnFont, command=root.quit)

    tryAgain_btn.place(x=840, y=150)
    exit_btn.place(x=840, y=510)


check_btn = Button(text="CHECK", width=15, height=2, font=btnFont, relief=SOLID, command=OnClick)
check_btn.place(x=215, y=615)

# status bar
status = Label(root, text="Created By Meenal Phartiyal  ", width=178, bd=1, relief=SUNKEN, anchor=E)
status.place(x=0, y=705)

mainloop()
