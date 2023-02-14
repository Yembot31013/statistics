from fpdf import FPDF

class PDF(FPDF):
  def header(self):
    #arial bold 15
    self.set_font("Arial", "B", 15)
    #calculate width of title and position
    w = self.get_string_width(title) + 6
    self.set_x((210 - w)/2)
    #colors of frame, background and text
    self.set_draw_color(0, 80, 180)
    self.set_fill_color(230, 230, 0)
    self.set_text_color(220, 50, 50)
    #Thickness of frame(1 mm)
    self.set_line_width(1)
    #Title
    self.cell(w, 9, title, 1, 1, "c", 1)
    #line break
    self.ln(10)

  def footer(self):
    #postion at 1.5cm from bottom
    self.set_y(-15)
    #Arial italic 8
    self.set_font("Arial", "I", 8)
    #Text color in gray
    self.set_text_color(128)
    #page number
    self.cell(0, 10, "Page" + str(self.page_no()), 0, 0, "C")

  def chapter_title(self, num, label):
    #Arial 12
    self.set_font("Arial", "", 12)
    #background color
    self.set_fill_color(200, 220, 2)
    #Title
    self.cell(0, 6, "Chapter %d : %s" % (num, label), 0, 1, "L", 1)
    #line break
    self.ln(4)

  def chapter_body(self, name):
    #add image file
    self.image(name, 10, 30, 100)
    #line break
    self.ln()
    #mention in italics
    self.set_font("", "I")
    self.cell(0, 5, "(Tef Comunity Innovation Hub)")

  def print_chapter(self, num, title, name):
    self.add_page()
    self.chapter_title(num, title)
    self.chapter_body(name)

if __name__ == "__main__": 
  title = "20000 Leagues Under the Seas"
  pdf = PDF()
  pdf.set_title(title)
  pdf.set_author("Adekojo Adeyemi")
  pdf.print_chapter(1, "A RUNAWAY REEF", "yembot.png")
  pdf.print_chapter(2, "THE PROS AND CONS", "yembot.png")
  pdf.output("test.pdf", "F")


