# Automate-metazoa
A python-based system to scrape the metazoan species from INSDC , filter and rank them based on some parameters.  


## Data folder
It contains the `esummary.csv` file which was used for the analysis  


## Scripts folder
It contains 3 python files
* `utils.py`
* `scraper.py`
* `analysis.py`


### `utils.py` 
Which contains some important functions for scraper.py  


### `scraper.py`  
This script scrapes the keyword "metazoa" from the nucleotide/nuccore database
of Entrez using the E-utils API and writes the result to a CSV file `esummary.csv`



### `analysis.py`  
This script filters and rank the `esummary.csv` data based on the presence of some parameters(i.e `assemblyacc` -> assembly accession id, `assemblygi` and `completeness`).  
 It creates a `score` column and if the row have the required variable, the score column would increment accordingly.  
 It then prints the score column greater than 0 to rank them 

![image](https://user-images.githubusercontent.com/109805657/228125892-0adffc14-3d28-47a1-ac6f-90f8254f62fa.png)
