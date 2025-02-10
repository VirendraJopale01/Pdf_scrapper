import os
from Controller.pdf_downloader import download_pdf
from Controller.data_scrap import *
from Utils.utlis import *

def controller(pages):
    """
    This function acts as a controller for the user interface. It takes the pages of a PDF as input and provides the user with options to fetch CIN Number, Email ID, Phone Number, PAN Number, Dates, and Websites present in the PDF.

    Parameters:
    pages (list): A list of strings where each string is a page of the PDF.

    Returns:
    None
    """
    while True:
        # Display options to the user
        print("1. Fetch CIN Number")
        print("2. Fetch Email ID")
        print("3. Fetch Phone Number")
        print("4. Fetch PAN Number")
        print("5. Fetch Dates")
        print("6. Fetch Websites")
        print("7. Exit")
        
        # Get user choice
        ch = int(input("\nEnter your choice : "))
        
        # Perform the corresponding action based on user choice
        if ch == 1:
            fetch_cin(pages)  # Fetch CIN numbers from the pages
        elif ch == 2:
            fetch_emails(pages)  # Fetch email IDs from the pages
        elif ch == 3:
            fetch_phone(pages)  # Fetch phone numbers from the pages
        elif ch == 4:
            fetch_PAN(pages)  # Fetch PAN numbers from the pages
        elif ch == 5:
            fetch_dates(pages)  # Fetch dates from the pages
        elif ch == 6:
            fetch_website(pages)  # Fetch websites from the pages
        elif ch == 7:
            break  # Exit the loop
        else:
            print("\nEnter a Valid choice!!")  # Display error message for a valid choice



def main():
    """
    This function acts as the entry point for the program. 
    It provides the user with options to either download a new pdf or extract data from an existing pdf.
    If the user chooses to download a new pdf, it asks for the url of the pdf and then downloads the pdf.
    If the user chooses to extract from an existing pdf, it provides the user with a list of existing pdfs and then asks for the pdf to be extracted. 
    After selecting the pdf, it asks for the number of pages to be extracted and then calls the controller
    function to provide the user with the options to fetch CIN Number, Email ID, Phone Number, PAN Number,
    Dates and Websites present in the pdf.

   
    """
    try:
        pdfs_list = []
        directories = "C:\\Users\\VirendraJopale\\Downloads\\Assign_PDF_Scrap\\downloads"
        while True:
            # Display options to the user
            print('1. For New pdf')
            print('2. Extract From Existing pdf')
            
            # Get user choice
            choice = int(input('Choose (1,2): '))
            
            if choice == 1:
                # Download a new PDF
                print("\nEnter URL for downloading the PDF\n")
                url = str(input('URL here: -> '))
                
                if url:
                    filename = extract_Pdf_Name(url)
                    
                    # Check if the PDF already exists in the directory
                    is_exist_pdf = pdf_In_local(directories)
                    if filename not in is_exist_pdf:
                        file = download_pdf(url, directories, filename)
                        print('\nFor scrapping data select pdf', file)
                        reader = select_pdf(file)
                        
                        pages = pages_extract(reader, int(input("\nEnter the number of pages to extract: ")))
                        controller(pages)
                    else:
                        print("File Already Exists")
                else:
                    print("PDF does not exist")
                    break
            elif choice == 2:
                # Extract from an existing PDF
                pdfs_list = pdf_In_local(directories) 
                if pdfs_list:
                # Display the list of existing PDFs
                    for i, pdf in enumerate(pdfs_list):
                        print(f'{i + 1}. {pdf}')

                # Get user choice for PDF
                    pdf_choice = int(input("Selected PDF: "))            
                    if pdf_choice <= len(pdfs_list):
                        print(pdfs_list[pdf_choice - 1])
                        reader = select_pdf(directories + '\\' + pdfs_list[pdf_choice - 1])
                        
                        pages = pages_extract(reader, int(input("Enter the number of pages to extract: ")))
                        controller(pages)
                    else:
                        print("PDF does not exist")
                        break
                else: 
                    print('No PDF found')    
            else:
                # Invalid choice
                print('Wrong URL \t ... closing the console')  
                break
    except Exception as e:    
        print(f"There was an error: {e}")

main()        