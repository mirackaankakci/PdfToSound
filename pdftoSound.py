import customtkinter as ctk
from tkinter import filedialog
import os
import PyPDF2  # Updated import
from gtts import gTTS

class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PDF To Sound")
        self.geometry("400x50")
        self.resizable(False, False)

        btn = ctk.CTkButton(master=self, text='Create', command=self.SoundSet)
        btn.pack(padx=10, pady=10)

    @staticmethod
    def CreateText(filepath):
        text = ""

        try:  # Added error handling
            with open(filepath, "rb") as pdf:  # Assuming binary mode for PDFs
                pdfReader = PyPDF2.PdfReader(pdf)  # Updated class name

                for i in range(len(pdfReader.pages)):
                    text += pdfReader.pages[i].extract_text() + "\n"

            return text
        except FileNotFoundError:  # Example error handling
            return "Error: File not found."

    @staticmethod
    def CreateSound(text, filename):
        sound = gTTS(text=text, lang="tr")
        sound.save(filename)

    def SoundSet(self):
        dialog = filedialog.askopenfilename(defaultextension=".pdf", filetypes=[("pdf files", "*.pdf")])

        if dialog is not None:
            extracted_text = self.CreateText(dialog)  # Store the result
            try:  # Added error handling for potential issues with CreateText
                self.CreateSound(extracted_text, "sound.mp3")
            except Exception as e:  # Catch general exceptions
                print("Error creating sound:", e)  # Log the error for debugging
                # Consider displaying a user-friendly message here

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()