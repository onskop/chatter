import gcsfs

    
# upload file to gcs
def upload_file(key, file, data):
    fs = gcsfs.GCSFileSystem(token=key)
    with fs.open(file, 'wb') as f:
        f.write(data)

svc_key = r'C:\Projects\Python\2_Experimental\Projekty\chatter\.streamlit\gcs_gymbro.json'

file_far = 'food-bro/instruct.json'
#file2 = 'food-bro/convo_db.json'
file_near = 'memo/instruct.json'

with open(file_near, 'rb') as f:
    data = f.read()

upload_file(svc_key, file_far, data)

print('Data uploaded: ', data)



