from qiniu import Auth
from qiniu import put_data

def uploadToQiniu(file,filename):
    access_key = 'access_key'
    secret_key = 'secret_key'
    bucket_name = 'pikach'
    q = Auth(access_key, secret_key)
    token = q.upload_token(bucket_name)
    key = filename
    
    ret, info = put_data(token, key, file)
    return ret