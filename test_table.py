from extract_data import getRawData
from generate_table import generate_table

parsed_domains = getRawData()

html = generate_table(parsed_domains[1].libraries, 'backwards compatibility')

print(html)