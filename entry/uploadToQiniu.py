from qiniu import Auth
from qiniu import put_data

def uploadToQiniu(file,filename):
    access_key = '33ZeBMUplEyElHGEPVyw9g6z-3pSDlOiwJBVCn9W'
    secret_key = 'tPnroK1ks0KLTCaVTZ49B6XcTCViAP_P01i2OfRv'
    bucket_name = 'pikach'
    q = Auth(access_key, secret_key)
    token = q.upload_token(bucket_name)
    key = filename
    
    ret, info = put_data(token, key, file)
    return ret
