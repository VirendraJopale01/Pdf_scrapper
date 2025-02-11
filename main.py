import os
import threading
from Controller.pdf_downloader import download_pdf
from Controller.data_scrap import *
from Utils.utlis import *
import math 
def controller(pages):
    """
    This function acts as a controller for the user interface.
    It takes the pages of a PDF as input and provides the user with options to fetch CIN Number,
    Email ID, Phone Number, PAN Number, Dates, and Websites present in the PDF.
 
    Parameters:
        pages (list): A list of strings where each string is a page of the PDF.
    
    Returns:
        None
    """
    while True:
        print("\nOptions:")
        print("1. Fetch CIN Number")
        print("2. Fetch Email ID")
        print("3. Fetch Phone Number")
        print("4. Fetch PAN Number")
        print("5. Fetch Dates")
        print("6. Fetch Websites")
        print("7. Exit")
        
        ch = int(input("\nEnter your choice: "))
        
        if ch == 1:
            fetch_cin(pages)
        elif ch == 2:
            fetch_emails(pages)
        elif ch == 3:
            fetch_phone(pages)
        elif ch == 4:
            fetch_PAN(pages)
        elif ch == 5:
            fetch_dates(pages)
        elif ch == 6:
            fetch_website(pages)
        elif ch == 7:
            break
        else:
            print("\nEnter a Valid Choice!!")
 
 

def extract_pages_threaded(reader, start, end, result, index):
    """
    Extracts pages in a thread and stores results.

    Parameters:
        reader (PyPDF reader object): The PyPDF reader object.
        start (int): The starting page number for this thread.
        end (int): The ending page number for this thread.
        result (list): A list to store the results of each thread.
        index (int): The index of the result list to store the result in.

   
    """
    # Extract the text from the pages
    extracted_text = pages_extract(reader, start, end)
    # Store the result in the list
    result[index] = extracted_text
    print(result)
 
def pages_extract_multithreaded(reader, num_pages, num_threads=4):
    """
    Extracts PDF pages using multiple threads.
 
    Parameters:
        reader (PyPDF reader object): The PyPDF reader object.
        num_pages (int): The number of pages to extract.
        num_threads (int): The number of threads to use. Defaults to 4.
 
    Returns:
        list: A list of strings where each string is a page of the PDF.
    """

    result = [None] * num_threads  # A list to store the results of each thread
    threads = []
    pages_per_thread = math.ceil(num_pages / num_threads)  # Calculate the number of pages per thread
 
    # Create a thread for each set of pages
    for i in range(num_threads):
        start = i * pages_per_thread  # The starting page number for this thread
        end = min(start + pages_per_thread, num_pages)  # The ending page number for this thread
        print(start,end)
        thread = threading.Thread(target=extract_pages_threaded, args=(reader, start, end, result, i))
        threads.append(thread)
        thread.start()  # Start the thread
 
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
 
    # Flatten the list of lists into a single list
    return [page for sublist in result if sublist for page in sublist]
 
 
def main():
    """
    Entry point for the program.
    It provides the user with options to either download a new PDF or extract data from an existing PDF.
    If the user chooses to download a new PDF, it asks for the URL and downloads the PDF.
    If the user chooses to extract from an existing PDF, it provides a list of existing PDFs.
    The selected PDF's pages are extracted and passed to the controller function.
    """
    try:
        # Set up the folder path for the downloaded PDFs
        folder_path = os.path.join(os.getcwd(), 'downloads')
        os.makedirs(folder_path, exist_ok=True)
        directories = folder_path
        
        while True:
            # Print the options for the user to choose from
            print("\n1. Download New PDF")
            print("2. Extract From Existing PDF")
            print("3. Exit")
            
            # Get the user's choice
            choice = int(input("\nChoose an option (1/2): "))
            
            if choice == 1:
                # Ask for the URL and download the PDF
                url = str(input("\nEnter URL for downloading the PDF: "))
                
                if url:
                    # Extract the PDF name from the URL
                    filename = extract_Pdf_Name(url)
                    
                    # Check if the PDF already exists in the directory
                    is_exist_pdf = pdf_In_local(directories)
                    
                    if filename not in is_exist_pdf:
                        # Download the PDF
                        file = download_pdf(url, directories, filename)
                        print("\nFor scrapping data select pdf", file)
                        
                        # Extract the pages from the PDF
                        reader = select_pdf(file)
                        num_pages = int(input("\nEnter the number of pages to extract: "))
                        pages = pages_extract_multithreaded(reader, num_pages)
                        
                        # Pass the extracted pages to the controller
                        controller(pages)
                    else:
                        print("File Already Exists")
                else:
                    print("Invalid URL")
            
            elif choice == 2:
                # Get the list of PDFs in the directory
                pdfs_list = pdf_In_local(directories)
                
                if pdfs_list:
                    # Print the list of PDFs and ask the user to select one
                    print("\nAvailable PDFs:")
                    for i, pdf in enumerate(pdfs_list):
                        print(f"{i + 1}. {pdf}")
                    
                    pdf_choice = int(input("\nSelect a PDF: "))
                    
                    if 1 <= pdf_choice <= len(pdfs_list):
                        # Construct the full path to the selected PDF
                        selected_pdf = directories + '\\' + pdfs_list[pdf_choice - 1]
                        reader = select_pdf(selected_pdf)
                        num_pages = int(input("\nEnter the number of pages to extract: "))
                        pages = pages_extract_multithreaded(reader, num_pages)
                        
                        # Pass the extracted pages to the controller
                        controller(pages)
                    else:
                        print("Invalid Selection")
                else:
                    print("No PDFs Found")
            
            else:
                print("Invalid Choice. Exiting...")
                break
    
    except Exception as e:
        print(f"An error occurred: {e}")
 
 
if __name__ == "__main__":
    main()