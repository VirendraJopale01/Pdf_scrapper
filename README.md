# PDF Data Extractor
```
Directory structure:
└── virendrajopale01-pdf_scrapper/
    ├── README.md
    ├── main.py
    ├── requirements.txt
    ├── Controller/
    │   ├── data_scrap.py
    │   ├── pdf_downloader.py
    │   └── __pycache__/
    ├── Utils/
    │   ├── utlis.py
    │   └── __pycache__/
    └── downloads/
```
## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/pdf-data-extractor.git
```
2. Navigate to the project directory:
```
cd pdf-data-extractor
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Run the main script:
```
python main.py
```
2. Choose an option:
   - **Download New PDF**: Enter the URL of the PDF you want to download and extract data from.
   - **Extract From Existing PDF**: Select a PDF from the list of available PDFs in the `downloads` directory.
3. Enter the number of pages you want to extract.
4. Choose an option to extract the desired data (CIN Number, Email ID, Phone Number, PAN Number, Dates, or Websites).
