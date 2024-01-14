import fitz

doc = fitz.open("tamthilia.pdf")

text = ""  # Initialize an empty string to store the text

for page_num in range(doc.page_count):
    page = doc[page_num]
    text += page.get_text()

with open("text.txt", "w", encoding="utf-8") as text_file:
    text_file.write(text)

doc.close()
print("Text extraction completed successfully!")
