from pypdf import PdfReader
import re

def select_pdf(pdf):
    """
    This function selects a PDF from the specified path and 
    initializes a PyPDF reader object with it.

    Args:
        pdf (str): The path of the PDF file.

    Returns:
        PyPDF reader object.
    """
    reader = PdfReader(pdf)
    return reader

def extract_Pdf_Name(url):
    """
    This function takes a URL of a PDF file and returns the name of the PDF
    as a string.

    Args:
        url (str): The URL of the PDF file.

    Returns:
        str: The name of the PDF file
    """
    # Extract the name of the PDF from the URL
    # The regular expression matches the last part of the URL before the '.pdf' extension
    name_pattern = r'([^/]+)(?=\.pdf$)'
    pdf_name = re.findall(name_pattern, url)
    # Return the name of the PDF with the '.pdf' extension
    return pdf_name[0]+'.pdf'

def pages_extract(reader, num):
    """
    Extract text from a specified number of pages in a PDF.

    This function takes a PyPDF reader object and an integer as arguments 
    and extracts the text from the specified number of pages in the PDF.

    Args:
        reader (PdfReader): The PyPDF reader object which contains the PDF.
        num (int): The number of pages to be extracted.

    Returns:
        list: A list of strings where each string is the text of a page in the PDF.
    """
    pages_list = []  # Initialize a list to store the text of each page

    # Iterate over the range of pages to extract text
    for i in range(num):
        # Access the page object at index i
        answer = reader.pages[i]
        # Extract text from the page object
        pages = answer.extract_text()
        # Remove leading and trailing whitespace from the extracted text
        cleaned_pgs = pages.strip()
        # Add the cleaned text to the pages list
        pages_list.append(cleaned_pgs)
    
    return pages_list  # Return the list of extracted page texts

def fetch_cin(pages):
    """
    Extracts and counts all CIN numbers from a list of page texts.

    This function searches for and retrieves all Company Identification Numbers
    (CIN) from the given list of strings, where each string represents a page 
    of a PDF document. A CIN is a unique identifier for companies incorporated in India.

    Args:
        pages (list): A list of strings where each string is a page of the PDF.

    Returns:
        tuple: A tuple containing a list of all the CIN numbers found and the total count
        of CIN numbers.
    """
    # Regular expression pattern for matching CIN numbers
    cin_pattern = r'\b[A-Z]{1}[0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}\b'
    cin_list = []  # List to store matched CIN numbers
    cin_count = 0  # Counter for the number of CIN numbers found

    # Iterate over each page's text in the list
    for text in pages:
        # Split the text into lines
        lines = text.split('\n')
        # Check each line for a CIN match
        for line in lines:
            match = re.search(cin_pattern, line)
            if match:
                # Add the matched CIN to the list
                cin_list.append(match.group())
                cin_count += 1  # Increment the CIN count

    # Output the extracted CIN numbers
    print("\nThe CIN values in the PDF are : \n")
    for cin in cin_list:
        print(f"\t{cin}")
    # Output the total count of CIN numbers
    print("\nTotal Count of CIN nos. is : ", cin_count)

    # Return the list of CIN numbers and their count
    return cin_list, cin_count

def fetch_emails(pages):
    """
    Extracts and counts all email IDs from a list of page texts.

    This function searches for and retrieves all email IDs from the given list of strings,
    where each string represents a page of a PDF document.

    Args:
        pages (list): A list of strings where each string is a page of the PDF.

    Returns:
        list: A list containing a list of all the email IDs found and the total count
        of email IDs.
    """
    # Regular expression pattern for matching email IDs
    email_pattern = r"\b[a-zA-Z0-9._]+@[a-z]+\.[a-z]{2,}\b"
    email_list = []  # List to store matched email IDs
    

    # Iterate over each page's text in the list
    for text in pages:
        # Split the text into lines
        lines = text.split("\n")
        # Check each line for an email match
        for line in lines:
            email_match = re.search(email_pattern, line)
            if email_match:
                # Add the matched email to the list
                email_list.append(email_match.group())
                
    # Output the extracted email IDs
    print("\nThe Email IDs in the PDF are : \n")
    for email in email_list:
        print(f"\t{email}")
    # Output the total count of email IDs
    print(f"\nThe Total Count of Emails is : {len(email_list)}")

    # Return the list of email IDs and their count
    return email_list, len(email_list)

def fetch_phone(pages):
    """
    Extracts and counts all phone numbers from a list of page texts.

    This function searches for and retrieves all phone numbers from the given list of strings,
    where each string represents a page of a PDF document.

    Args:
        pages (list): A list of strings where each string is a page of the PDF.

    Returns:
        list: A list of all the phone numbers found.
    """
    
    # Regular expression pattern for matching phone numbers with separators
    phone = r'(\[-\s]?[6-9]\d{9}|[6-9]\d{9}|\d{2,5}[-\s]?\d{5,8})'
    mob_list = []  # List to store matched phone numbers
    
    # Iterate over each page's text in the list
    for text in pages:
        # Split the text into lines
        lines = text.split("\n")
        # Check each line for a phone match
        for line in lines:
            mob_match = re.search(phone, line)
            if mob_match:
                # Add the matched phone to the list
                mob_list.append(mob_match.group())
             
    # Output the extracted phone numbers
    print("\nThe Phone numbers in the PDF are : \n")
    for mob in mob_list:
        print(f"\t{mob}")
    # Output the total count of phone numbers
    print(f"\nThe Total Count of Moblies is : {len(mob_list)}")

    # Return the list of phone numbers
    return mob_list


def fetch_PAN(pages):
    """
    Extracts and counts all PAN Card numbers from a list of page texts.

    This function searches for and retrieves all PAN Card numbers from the given list of strings,
    where each string represents a page of a PDF document.

    Args:
        pages (list): A list of strings where each string is a page of the PDF.

    Returns:
        list: A list of all the PAN Card numbers found.
    """
    # Regular expression pattern for matching PAN Card numbers
    PAN_pattern = r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b"
    PAN_list = []  # List to store matched PAN Card numbers
    
    # Iterate over each page's text in the list
    for text in pages:
        # Split the text into lines
        lines = text.split("\n")
        # Check each line for a PAN match
        for line in lines:
            PAN_match = re.search(PAN_pattern, line)
            if PAN_match:
                # Add the matched PAN to the list
                PAN_list.append(PAN_match.group())
    
    # Output the extracted PAN Card numbers
    print("\nThe PAN Card Numbers in the PDF are : \n")
    for PAN in PAN_list:
        print(f"\t{PAN}")
    # Output the total count of PAN Card numbers
    print(f"\nThe Total Count of PANs is : {len(PAN_list)}")
    return PAN_list, len(PAN_list)

def fetch_dates(pages):
    """
    Extracts and counts all dates from a list of page texts.

    This function searches for and retrieves all dates in the format 'DD/MM/YYYY'
    from the given list of strings, where each string represents a page of a PDF document.

    Args:
        pages (list): A list of strings where each string is a page of the PDF.

    Returns:
        list: A list containing a list of all the dates found and the total count
        of dates.
    """
    # Regular expression pattern for matching dates in 'DD/MM/YYYY' format
    date_pattern = r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19\d{2}|20\d{2})\b"
    date_list = []  # List to store matched dates

    # Iterate over each page's text in the list
    for text in pages:
        # Split the text into lines
        lines = text.split("\n")
        # Check each line for a date match
        for line in lines:
            date_matches = re.findall(date_pattern, line)
            for date in date_matches:
                # Join the date components into a single string
                date_new = '/'.join(date)
                date_list.append(date_new)

    # Output the extracted dates
    print("\nThe Dates in the PDF are : ")
    for date in date_list:
        print(f"\t{date}")
    # Output the total count of dates
    print(f"\nThe Total Count of Dates is : {len(date_list)}")

    # Return the list of dates and their count
    return date_list, len(date_list)

def fetch_website(pages):
    """
    Extracts and counts all websites from a list of page texts.

    This function searches for and retrieves all websites in the format 'www.example.com'
    from the given list of strings, where each string represents a page of a PDF document.

    Args:
        pages (list): A list of strings where each string is a page of the PDF.

    Returns:
        list: A list containing a list of all the websites found and the total count
        of websites.
    """
    # Regular expression pattern for matching websites format
    website_pattern = r"\b[w]{3}+\.[a-z]+\.[a-z]{2,}\b"
    web_list = []  # List to store matched websites

    # Iterate over each page's text in the list
    for text in pages:
        # Split the text into lines
        lines = text.split("\n")
        # Check each line for a website match
        for line in lines:
            website_matches = re.findall(website_pattern, line)
            for website in website_matches:
                # Add the matched website to the list
                web_list.append(website)

    # Output the extracted websites
    print("\nThe Websites in the PDF are : ")
    for website in web_list:
        print(f"\t{website}")
    # Output the total count of websites
    print(f"\nThe Total Count of Websites is : {len(web_list)}")

    # Return the list of websites and their count
    return web_list, len(web_list)


