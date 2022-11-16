from fpdf import FPDF
def print(dict_json):
    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size = 15)

    pdf.cell(200, 10, txt = "GeeksforGeeks", ln = 1, align = 'C')

    pdf.cell(200, 10, txt = "A Computer Science portal for geeks.", ln = 2, align = 'C')

    pdf.output("GFG.pdf")