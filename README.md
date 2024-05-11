# PDF Manager

## Overview
The PDF Manager is a Python-based command-line tool designed to merge, extract pages from, and convert text files into PDF format. It leverages the `pypdf` and `fpdf` libraries for PDF manipulation tasks. Users can merge specific pages from multiple PDF files, extract selected pages from a PDF, or convert a text file to PDF.

## Features
- **Merge PDF Files:** Users can merge specific pages from multiple PDF files into a single PDF document.
- **Extract Pages:** Users have the option to extract selected pages from a PDF file.
- **Convert Text to PDF:** Users can convert plain text files into PDF format.

## Code Structure
- **Modules Used:**
  - `pypdf`: For merging and extracting pages from PDF files.
  - `fpdf`: For creating PDF files from text.

- **Classes:**
  - `all`: Represents a PDF file with methods to select pages for merging.

- **Functions:**
  - `write_it(writer,reader,each_page_num)`: Writes selected pages to a PDF writer object.
  
- **Main Execution:**
  - Users are prompted to choose from three options: Merge PDF files, Extract pages, or Convert text to PDF.
  - Depending on the chosen option, users are guided through the process, including selecting files and pages, specifying output paths, and handling errors.
  - The program provides a user-friendly interface with clear instructions and error handling.

## Usage
1. Execute the Python script.
2. Choose the desired operation: Merge PDF files, Extract pages, or Convert text to PDF.
3. Follow the prompts to input file paths, select pages, and specify output locations.

## Potential Improvements
- Implement encryption and password protection for merged PDF files.
- Add support for more advanced PDF manipulation features, such as rotating pages or adding watermarks.
- Enhance error handling to provide more informative messages and guidance to users.

## Conclusion
The PDF Manager project provides a convenient and efficient solution for handling PDF files through a command-line interface. Whether merging, extracting, or converting PDFs, the tool offers flexibility and ease of use for various PDF manipulation tasks.
