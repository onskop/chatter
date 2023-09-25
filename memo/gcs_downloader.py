import gcsfs

# download file from gcs
def download_file(file, key):
    fs = gcsfs.GCSFileSystem(token=key)
    with fs.open(file, 'rb') as f:
        return f.read()
    

svc_key = r'C:\Projects\Python\2_Experimental\Projekty\chatter\.streamlit\gcs_gymbro.json'

file_from = 'food-bro/instruct.json'
#file2 = 'food-bro/convo_db.json'
file_to = 'memo/instruct.json'

data = download_file(file_from, svc_key)
with open(file_to, 'wb') as f:
    f.write(data)

print('Data downloaded: ', data)



