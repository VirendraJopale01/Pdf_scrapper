import os
def pdf_In_local(directories):
    """
    This function takes a directory as input and returns a list of all the PDFs present in the directory.

    Parameters:
    directories (str): The path of the directory where the PDFs are located.

    Returns:
    list: A list of all the PDFs present in the directory.
    """
    pdfs_list = []  # Initialize an empty list to store the PDFs
    for (root, dir, file) in os.walk(directories):  # Iterate through all the files in the directory
        for f in file:  
            if '.pdf' in f:  # Check if the file is a PDF
                pdfs_list.append(f)  # Add the PDF to the list
    return pdfs_list  
