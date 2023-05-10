# CSV File Combiner

The CSV File Combiner is a command-line tool that combines multiple CSV files into a single CSV file. This tool is written in Python.

### Installation
1. Install Python on your system if you haven't already. You can download Python from the official website: https://www.python.org/downloads/
2. Clone or download the repository from GitHub: https://github.com/s-maurya00/CSV_Combiner
3. Create a virtual enviourment by running the following command in your terminal:
```
python -m venv env
```
4. Activate the enviroment using command:
```
env\Scripts\activate
```
5. Install the required dependencies by running the following command in your terminal or command prompt:
```
pip install -r requirements.txt
```

### Usage
1. Open your terminal or command prompt and navigate to the directory where you cloned or downloaded the repository.
2. Run the following command to combine the CSV files:
```
python combine_csv.py "path-to-csv-files" "path-to-output/output_filename.csv"
```

Replace "path-to-csv-files" with the directory path containing the CSV files you want to combine, and "path-to-output/output_filename.csv" with the path and name you want to give to the combined CSV file.

Example
Suppose you have two CSV files, "data1.csv" and "data2.csv", in the directory "/home/user/csv_files". To combine these files into a single CSV file called "/home/user/output/combined.csv", run the following command:

```
python combine_csv.py "/home/user/csv_files" "/home/user/output/combined.csv"
```


### License
- This project is licensed under the MIT License.
