from fpdf import FPDF
from fpdf import Align
from PIL import Image


def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    shirt = Image.open("shirtificate.png")
    pdf.image(shirt, x=Align.C, y=80, w=180, h=190)
    pdf.set_font("helvetica", "B", 32)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(140)
    pdf.cell(w=0, txt=f"{name} took CS50", align="C")
    pdf.set_font("helvetica", "B", 50)
    pdf.set_text_color(0,0,0)
    pdf.set_y(40)
    pdf.cell(w=0, txt="CS50 Shirtificate", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()