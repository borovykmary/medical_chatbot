# https://jeltef.github.io/PyLaTeX/current/examples/full.html

from pylatex import Document, Section, Subsection

if __name__ == '__main__':

    geometry_options = {"tmargin": "1cm", "lmargin": "10cm"}
    doc = Document(geometry_options=geometry_options)
    with doc.create(Section('Patient\'s data')):
        doc.append('Name: ')
        doc.append('\nSymptoms: ')
        doc.append('\nAll')
    doc.generate_pdf('full', clean_tex=False, compiler='pdflatex')

