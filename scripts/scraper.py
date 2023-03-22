"""
This script scrapes the keyword "metazoa" from the nucleotide/nuccore database
of Entrez using the E-utils API and writes the result to a CSV file(esummary.csv)
"""

from pathlib import Path
import os
from scripts.utils import file_writer, get_soup, esearch

base_dir = Path(r"C:\Users\Client\Documents\Entrez scraper")
data_dir = base_dir / "data"

# writing headers to csv file
field_names = ['Accessionid', 'title', 'extra', 'gi', 'createdate', 'updatedate', 'flags', 'taxid', 'slen',
               'biomol', 'moltype', 'topology', 'sourcedb', 'segsetsize', 'projectid', 'genome', 'subtype',
               'subname',
               'assemblygi', 'assemblyacc', 'tech', 'completeness', 'geneticcode', 'strand', 'organism', 'strain',
               'biosample']

if os.path.exists(data_dir / 'esummary.csv'):
    print('file exist, hence headers written!!!')
else:
    file_writer(file_name='esummary.csv', row_data=field_names)

# making an esearch to get all 'metazoa' on the entrez nucleotide db
# and retrieve the webenv and querykey from the history
webenv, query_key, count = esearch(search_term='metazoa', db='nucleotide')

# setting ret_max to X. N.B: the maximum ret_max is 10,000 and is kind of slow
ret_max = 10000

# i.e from 0 till the count
for ret_start in range(0, int(count), ret_max):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&query_key={query_key}&WebEnv" \
          f"={webenv}&retmode=xml&retstart={ret_start}&retmax={ret_max}&version=2.0"

    try:
        soup = get_soup(url)
    except BaseException as e:
        # saving scenarios of an error, to a csv file.
        # To keep the script running
        # todo: write a script to check for skipped ids and re-run them.
        #  Retaining the history web-env should be required
        file_writer('skipped_ret_start.csv', [ret_start])
        print(f'Skipped ret_start: {ret_start}!!!...\nIt caused an {e}')
        continue

    for doc_sum in soup.findAll("documentsummary"):
        esummary = []
        for field_name in field_names:

            if field_name == 'Accessionid': # accessionid is the caption tag on the xml
                field_name = 'caption'

            try:
                field_name = doc_sum.find(f'{field_name}').text
            except AttributeError:
                field_name = None

            esummary.append(field_name)
        file_writer('esummary.csv', row_data=esummary)
    print(f"Extracted {ret_max + ret_start} 'u_id's..")