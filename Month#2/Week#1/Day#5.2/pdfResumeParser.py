import pdfminer
import spacy
import re
import os
import pandas as pd
import pdf2txt
import sys

names = []
phones = []
emails = []
skills = []
data = {}
nlp = spacy.load("en_core_web_sm")

if len(sys.argv) > 1:
    resume_filepath = sys.argv[1]
else:
    print('Please provide the path to resume directory.')
    exit()


def pdf_to_txt(filename):

    outfilename = os.path.basename(os.path.splitext(filename)[0]) + '.txt'
    outfilepath = os.path.join('./txts/', outfilename)
    pdf2txt.main(args=[filename, '--outfile', outfilepath])
    return open(outfilepath).read()


def extract_from_txt(text):
    skillset = re.compile('sql|java|hadoop|tableau|python|powerbi')
    phone_num = re.compile(
        '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    model = nlp(text)
    name = [entity.text for entity in model.ents if entity.label_ ==
            'PERSON'][0].strip()
    email = str([word for word in model if word.like_email][0])
    phone = str(re.findall(phone_num, text.lower())[0])
    skills = re.findall(skillset, text.lower())
    unique_skills = str(set(skills))
    return name, phone, email, unique_skills


def main():
    for file_ in os.listdir(resume_filepath):
        if file_.endswith('.pdf'):
            text = pdf_to_txt(os.path.join(resume_filepath, file_))
            name, phone, email, skills_ = extract_from_txt(text)
            names.append(name)
            phones.append(phone)
            emails.append(email)
            skills.append(skills_)

    df = pd.DataFrame({'Name': names, 'Email': emails,
                      'Phone': phones, 'Skills': skills})
    df.to_csv('./csvs/DataScientists.csv', index=False)


if __name__ == '__main__':
    main()
