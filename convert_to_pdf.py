# https://jeltef.github.io/PyLaTeX/current/examples/full.html
from datetime import date

from pylatex import Document, Section, Subsection

if __name__ == '__main__':
    # def convert_to_pdf(answer: list[String]):
    geometry_options = {"tmargin": "2cm", "lmargin": "2cm"}
    datetime = str(date.today().strftime("%d/%m/%Y"))
    doc = Document(geometry_options=geometry_options)
    doc.create(Section(f'Patient\'s data {datetime}'))
    doc.generate_pdf('full', clean_tex=False, compiler='pdflatex')
