import camelot
import PyPDF2
import sys


pdf_name = sys.argv[1]
pdfFileObj = open(pdf_name, 'rb')
# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# number of pages in pdf
num_of_pdf_pages = pdfReader.numPages
list_of_num_pdf_pages = [i for i in range(1,num_of_pdf_pages+1)]
print(list_of_num_pdf_pages)
pages = ','.join(str(e) for e in list_of_num_pdf_pages)

tables = camelot.read_pdf(pdf_name, process_background=True, pages=pages)
number_of_table = len(tables)
print("Processingg....")
for table_no in range(0,number_of_table):
	tables[table_no].to_csv('table'+str(table_no)+'.csv')
