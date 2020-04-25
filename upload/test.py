#!/usr/bin/env python
# coding=utf-8

from qiniu import Auth, put_file, etag
import qiniu.config
from PIL import Image
#from PIL import ImageGrab

#需要填写你的 Access Key 和 Secret Key
access_key = '3GlXcvfhHUDRLZP-SVJZ1odN85f_bDN-4lGURcKG'
secret_key = 'fke-BfPPP8lTX4e6ejCx7WNCuAK_q0rSSGvOFj8W'

#构建鉴权对象
q = Auth(access_key, secret_key)

#要上传的空间
bucket_name = 'haizei-test'

#上传后保存的文件名
key = 'lws02.jpg'

#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)

#要上传文件的本地路径
#localfile = '/home/lws/Pictures/wallpaper/1.jpg'
im = pyperclip.copy()

if isinstance(im, Image.Image):
    ret, info = put_file(token, key, im)
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(im)
else:
    pass
