# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from qiniu import Auth, put_file, etag, urlsafe_base64_encode

def upload_to_cloud(bucket_name, key, local_file):
    '''
    :param bucket_name: 文件上传到的空间
    :param key: 上传到七牛后保存的文件名
    :param local_file: 要上传文件的本地路径
    :return: ret和info的元组
    '''
    access_key = 'EWyCQ6d9Y5FVoo1N7LmCjwn8cQld4YLTYrsnnjFw'
    secret_key = '7JpiUFDIN8LU37s2OC4H_n7fCLEwxuACMYZchloQ'
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    token = q.upload_token(bucket_name, key, 3600)

    ret, info = put_file(token, key, local_file)
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(local_file)
    return (ret, info)


if __name__ == '__main__':
    upload_to_cloud('star', 'ans.wav', 'ans.wav')
