import PyPDF2

def extract_text_from_pdf(file_path: str):
    # Open the PDF file
    pdf_file = open(file_path, 'rb')

    # Read the PDF file
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Search for a keyword in each page of the PDF file
    keyword1 = 'ABSTRACT'
    keyword2 = 'Abstract'
    keyword3 = 'abstract'
    result = ""
    for page in pdf_reader.pages:
        # Extract the entire text of the page
        page_text = page.extract_text()

        # Split the text into paragraphs
        paragraphs = page_text.split('\n')

        # Search for the keyword in each paragraph
        extracted_text = ''
        found_keyword = False
        for paragraph in paragraphs:
            if keyword1 in paragraph or keyword2 in paragraph or keyword3 in paragraph:
                found_keyword = True
                extracted_text += paragraph + '\n'
            elif found_keyword:
                # Concatenate the current paragraph and any subsequent paragraphs
                # until we encounter another paragraph that does not contain any text
                if paragraph.strip() == '':
                    break
                extracted_text += paragraph + '\n'

        # Print the extracted text
        # return extracted_text
        result += extracted_text

    # Close the PDF file
    pdf_file.close()
    return result