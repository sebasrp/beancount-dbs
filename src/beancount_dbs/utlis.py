import pypdfium2 as pdfium

def pdf_to_text(filename):
    text = ""
    pdf = pdfium.PdfDocument(filename)
    for i in range(len(pdf)):
        page = pdf.get_page(i)
        textpage = page.get_textpage()
        text += textpage.get_text_range()
        text += "\n"
        [g.close() for g in (textpage, page)]
    pdf.close()
    return text