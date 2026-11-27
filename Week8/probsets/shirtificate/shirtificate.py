
from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.set_font("helvetica", size=36)
pdf.cell(0, 50, "CS50 Shirtificate", align="C")

pdf.image("shirtificate.png", x=10, y=70, w=190)

pdf.set_font("helvetica", size=20)
pdf.set_text_color(255, 255, 255)

text = f"{name} took CS50"
text_width = pdf.get_string_width(text)
x = (210 - text_width) / 2

pdf.text(x=x, y=150, txt=text)

pdf.output("shirtificate.pdf")

