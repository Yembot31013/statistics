from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(40, 10, "Hello World!")
pdf.image("yembot.png", 10, 30, 100)
pdf.output("new.pdf", "F")