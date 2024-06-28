from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

root = Tk()
root.title("Bookify")
root.geometry("800x600")
header = Label(root, text="Bookify - Book Management System", font=("Arial", 14))
header.pack(anchor="center")

# Tabs framework
notebook = ttk.Notebook(root)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
notebook.add(tab1, text="All Books")
notebook.add(tab2, text="Our Inventory")
notebook.add(tab3, text="Customers")
notebook.pack(expand=1, fill="both")

# Scrollable Frame Class
class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

# All Books Tab
scrollable_tab1 = ScrollableFrame(tab1)
scrollable_tab1.pack(fill="both", expand=True)

input_text = StringVar() 
searchHeader =ttk.Label(scrollable_tab1.scrollable_frame)
searchHeader.config(text="Search books", font=("Arial", 20, "bold"), padding=(0, 10))
searchBar = ttk.Entry(scrollable_tab1.scrollable_frame, textvariable=input_text)
searchBar.config(font=("Arial", 18))
searchHeader.pack(anchor="center")
searchBar.pack(anchor="center")
resultsContainer = ScrollableFrame(scrollable_tab1.scrollable_frame)
resultsContainer.pack(fill="both", expand=True)
image_references = []


def searchButton():
    global resultsContainer
    global image_references
    print("Search button clicked")
    # change results to call api function
    resultsContainer.destroy()
    resultsContainer = ScrollableFrame(scrollable_tab1.scrollable_frame)
    resultsContainer.pack(fill="both", expand=True)
    results = ["Book 1", "Book 2", "Book 3"]
    image_references = []
    for result in results:
        resultFrame = ttk.Frame(resultsContainer, padding=(10, 10))
        url = "https://i0.wp.com/maps.org/wp-content/uploads/2024/05/Rhythms-of-Resistance-Photo-1.png?w=910&ssl=1"
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        image = image.resize((100, 100))
        resultPicture = ImageTk.PhotoImage(image)
        
        image_references.append(resultPicture)  # Keep a reference to the image
        resultLabel = ttk.Label(resultFrame)
        resultLabel.config(text=result, font=("Arial", 18), padding=(0, 10))
        resultImage = ttk.Label(resultFrame)
        resultImage.config(image=resultPicture)
        resultFrame.pack(anchor="center")
        resultImage.pack(anchor="center")
        resultLabel.pack(anchor="center")
searchButton = ttk.Button(scrollable_tab1.scrollable_frame, text="Search", command=searchButton)
searchButton.pack(anchor="center")

root.mainloop() 
