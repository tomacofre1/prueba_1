#clase 1 

from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")

pdf.text(10,10,"ASDASDASD")
pdf.output("Presupuesto.pdf")
