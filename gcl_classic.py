import gcsfs

def read_gcs(bucket_name, blob_name, key_path):

    fs = gcsfs.GCSFileSystem(token=key_path)
    
    # Use the file-like interface
    with fs.open(f'{bucket_name}/{blob_name}', 'r', encoding = 'utf-8') as f:
        content = f.read()
        
    return content

# Path to the service account key
service_account_key = r'C:\Projects\Python\2_Experimental\Projekty\chatter\.streamlit\gcs_gymbro.json'



# Use the function
file_content = read_gcs('food-bro', 'instruct.json', service_account_key)
print(file_content)
