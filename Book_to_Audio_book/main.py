import pyttsx3
from pypdf import PdfReader
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def pdf_to_audio():
    # Hide root tkinter window
    root = Tk()
    root.withdraw()

    # Select PDF file
    file_path = askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    if not file_path:
        print("No file selected.")
        return

    # Read PDF
    reader = PdfReader(file_path)

    # Initialize TTS engine ONCE
    engine = pyttsx3.init()

    for page in reader.pages:
        text = page.extract_text()
        if text:
            engine.say(text)

    engine.runAndWait()


if __name__ == "__main__":
    pdf_to_audio()
