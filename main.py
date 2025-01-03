import camelot
import pdfplumber
import json

page_range_input = input("how many pages you want to set to JSON? (example. '1,2,3' of '1-5'): ")

def parse_page_range(page_range):
    pages = []
    for part in page_range.split(','):
        if '-' in part:
            start, end = part.split('-')
            pages.extend(range(int(start), int(end) + 1))
        else:
            pages.append(int(part))
    return pages

pages_to_convert = parse_page_range(page_range_input)

#pdf_path = "input.pdf"
#json_path = "output.json"
pdf_path = input('the path of the pdf:')
json_path = "output.json"

data = []

tables = camelot.read_pdf(pdf_path, pages=page_range_input, flavor="stream")

for i, table in enumerate(tables):
    table_data = table.df  
    table_json = table_data.to_dict(orient="records")  
    data.append({"table": i+1, "data": table_json})

with pdfplumber.open(pdf_path) as pdf:
    for page_num in pages_to_convert:
        page = pdf.pages[page_num - 1]  
        text = page.extract_text()  
        data.append({"page": page_num, "text": text})

with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"PDF set to json {json_path} for pages: {page_range_input}")
