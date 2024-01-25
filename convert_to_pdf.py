# https://jeltef.github.io/PyLaTeX/current/examples/full.html
from datetime import date

from pylatex import Document, Section, Subsection, NewLine, NoEscape


def convert_to_pdf(answers: list):
    geometry_options = {"tmargin": "2cm", "lmargin": "2cm"}
    datetime = str(date.today().strftime("%d/%m/%Y"))
    doc = Document(geometry_options=geometry_options)

    with doc.create(Section(f'Patient\'s data {datetime}')):
        with doc.create(Subsection('Name')):
            doc.append(answers[0])

        with doc.create(Subsection('Symptoms')):
            doc.append(answers[1])

        with doc.create(Subsection('Diagnosis')):
            doc.append('')

        with doc.create(Subsection('Prescription')):
            doc.append(NoEscape(r"\noindent\rule{\textwidth}{1pt}"))
            doc.append(NewLine())
            doc.append("Clinic")

    doc.generate_pdf('patient_data', clean_tex=False, compiler='pdflatex')


def main():
    convert_to_pdf(['John', 'symptoms'])


if __name__ == '__main__':
    main()
