import pandas as pd
import os
import requests
from urllib.parse import urlparse


# Function to download file and save with a generated filename
def download_file(url, file_name, folder_name, subfolder_name):
    try:
        # Create the folder if it does not exist
        folder_path = os.path.join(folder_name, subfolder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        # Check if the request was successful
        if response.status_code == 200:
           # Get the filename and extension from the URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            # Split the filename into name and extension
            name, extension = os.path.splitext(filename)
            # Create a new filename by combining the given file_name with the extension
            new_filename = f"{file_name}{extension}"
            # Save the content to a file with the given filename
            file_path = os.path.join(folder_path, new_filename)
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"File downloaded and saved as {new_filename}")
        else:
            print(f"Failed to download file from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading file from {url}: {e}")

# Read the CSV file
csv_file = 'import.csv'  # Replace with the path to your CSV file
year = '2024'           # Replace with the desired year
folder_name = 'Supplier'  # Replace with the desired folder name
df = pd.read_csv(csv_file)  # for semicolon-delimited CSV

# Loop through each row in the DataFrame
for index, row in df.iterrows():

    if folder_name == 'Supplier':
        supplier = str(row['Supplier']).replace(' ', '_')
        url1 = row['url1']
        url2 = row['url2']
        url3 = row['url3']
        url4 = row['url4']
    else:
        supplier = str(row['Customer']).replace(' ', '_')
        url1 = row['url1']
        url2 = ''
        url3 = ''
        url4 = ''

    submitted_by = str(row['Submitted_by']).replace(' ', '_')  # Convert to string and replace spaces with underscores

    file_name = f"{index+1}_{supplier}_{submitted_by}"
        
    if pd.notna(url1):
        download_file(url1, file_name, year , folder_name)
    if pd.notna(url2):
        download_file(url2, file_name + '_2', year, folder_name)
    if pd.notna(url3):
        download_file(url3, file_name + '_3', year, folder_name)
    if pd.notna(url4):
        download_file(url4, file_name + '_4', year, folder_name) 
