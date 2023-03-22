"""
This scripts includes some functions for scraper.py
"""
import csv
from pathlib import Path
import requests
from bs4 import BeautifulSoup


# place the path to your base directory
base_dir = Path(r"\path\to\base\directory")
data_dir = base_dir / "data"


def file_writer(file_name: str, row_data: list):
    """
    writes to csv file

    :param file_name: the row of content data
    :param row_data: the header of the file
    :return: writes to the specified csv file
    """

    with open(data_dir / file_name, 'a', newline='', encoding='utf8') as f_obj:
        writer = csv.writer(f_obj)
        writer.writerow(row_data)


def get_soup(url: str):
    """
    make a request to the URL and return the html/xml soup object
    for parsing

    :param url: the URL of the site
    :return: soup object, which can be parsed appropriately
    """
    r = requests.get(url)
    print(f'Request sent!!!..Now receiving response...')
    soup = BeautifulSoup(r.text, 'lxml')
    return soup


def esearch(search_term: str, db: str):
    """
    make an e-search to entrez database

    :param search_term: the query for the search,
    you can pass 'AND'/ 'OR' for complex queries
    :param db: database of the search
    :return: webenv(web environment variable of the search history), query_key, count
    """

    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db={db}&term={search_term}&usehistory=y"

    soup = get_soup(url)
    webenv = soup.find('webenv').text
    query_key = soup.find('querykey').text
    count = soup.find('count').text
    id_list = soup.findAll('id')
    id_list = [i.text for i in id_list]
    return webenv, query_key, count