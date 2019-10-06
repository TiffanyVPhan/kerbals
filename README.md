# Kerbal CSV
This is my solution to the interview problem given by LASP. The `convert.py` file reads in the `kerbals.csv` file and prints the JSON and XML encodings. Each row in the csv file represents one Kerbel.

The `Courage` and `Stupidity` columns for each column was transformed to their 'true' values, which are percents between 0 and 100.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pandas.

```bash
pip install pandas
```

## Run
Usage: ./convert.py [json | xmf] [OPTION]
    -f
        output to file

`./convert.py json`     :    prints out JSON encoding
`./convert.py json -f`  :    prints out JSON encoding and writes JSON to a file
`./convert.py xml`      :    prints out XML encoding
`./convert.py xml -f`   :    prints out XML encoding and writes XML to a file
