from fpdf import FPDF
def print(djson):
    pdf = FPDF(format='letter', unit='in')

    # Add new page. Without this you cannot create the document.
    pdf.add_page()

    # Remember to always put one of these at least once.
    pdf.set_font('Times', '', 10.0)

    # Effective page width, or just epw
    epw = pdf.w - 2 * pdf.l_margin

    # Set column width to 1/4 of effective page width to distribute content
    # evenly across table and page
    col_width = epw / 2

    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.

    header = [['Skill', 'Rate']]
    data = []
    for key, value in djson['skills'].items():
        data.append([key, value])
    # Document title centered, 'B'old, 14 pt
    pdf.set_font('Times', 'B', 14.0)
    pdf.cell(epw, 0.0, djson['strSearch'], align='L')
    pdf.ln(0.3)
    pdf.cell(epw, 0.0, djson['amountvacstr'], align='L')
    pdf.set_font('Times', 'B', 14.0)
    pdf.ln(0.3)

    th = pdf.font_size

    for row in header:
        for datum in row:
            pdf.cell(col_width, th, str(datum), border=1)

        pdf.ln(th)

    pdf.set_font('Times', '', 14.0)
    for row in data:
        for datum in row:
            pdf.cell(col_width, th, str(datum), border=1)

        pdf.ln(th)

    pdf.output("skills.pdf")
    return pdf