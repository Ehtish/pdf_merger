import os 
from PyPDF2 import PdfMerger

# Folder containing PDF files
input_folder = "pdf_files"


# Folder where merged PDF will be saved
output_folder = "output"

#  Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Create PDF merger object
merger = PdfMerger()


# Get all files from the PDF folder
files = os.listdir(input_folder)

# Process each file
for file in files:

    # Check only PDF files
    if file.lower().endswith(".pdf"):
         # Create complete file path
        file_path = os.path.join(input_folder,file)
         # Add PDF to merger
        merger.append(file_path)

# Create final output path
output_file = os.path.join(output_folder,"combined.pdf")


# Save merged PDF
merger.write(output_file)

# Close merger
merger.close()


print("PDF files merged successfully!")
print("Output", output_file)