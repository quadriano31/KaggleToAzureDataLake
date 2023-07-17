 # Upload Kaggle dataset file to Azure Data Lake Storage Gen2 using Kaggle API

This Python script allows you to use Kaggle python warpper to download dataset and upload a Parquet file to Azure Data Lake Storage Gen2.

## Prerequisites

### Clone the repository or download the script files to your local machine.

### Install dependencies
​
1. Create a python environment using [pythonenv](https://docs.python.org/3/tutorial/venv.html) and activate it.
```bash
python3 -m venv venv
source venv/bin/activate
```
​
2. Install python libraries
```bash
pip install -r requirements.txt
```

3. Environment variables
  - `AZURE_CLIENT_ID`: Azure AD client ID
  - `AZURE_TENANT_ID`: Azure AD tenant ID
  - `AZURE_CLIENT_SECRET`: Azure AD client secret

### Run application
​
```bash
python main.py

```

### Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request.

### License
This project is licensed under the MIT License.