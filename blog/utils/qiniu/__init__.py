# _*_ coding: utf-8 _*_
import qiniu.conf
import qiniu.io
import qiniu.rs
import qiniu.rsf


import datetime
from flask import current_app

class qiniu_lib(object):

    def __init__(self, access_key=None, secret_key=None):

        self.access_key = access_key

        self.secret_key = secret_key

        self.img_allow_extension = ['jpg','JPG','jpeg','JPEG','BMP','bmp','png','PNG']


    def datetime_to_filename(self, format):

        return str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))+'.'+format


    def upload(self, upload_file=None, bucket_name=None, file_type=None, name_type='datetime', filename='aaa.jpg'):
        """文件上传"""

        if not filename:
            filename = upload_file.filename

        allow_extension = getattr(self, file_type+'_allow_extension', False)

        if '.' in filename and filename.rsplit('.', 1)[1] in allow_extension:

            if self.access_key:
                access_key = self.access_key
            else:
                access_key = current_app.config.get('QINIU_ACCESS_KEY')

            if self.secret_key:
                secret_key = self.secret_key
            else:
                secret_key = current_app.config.get('QINIU_SECRET_KEY')

            qiniu.conf.ACCESS_KEY = access_key
            qiniu.conf.SECRET_KEY = secret_key

            save_filename = ''
            if name_type == 'datetime':
                save_filename = self.datetime_to_filename(filename.rsplit('.', 1)[1])
            if name_type == 'default':
                save_filename = filename
            policy = qiniu.rs.PutPolicy(bucket_name+':'+save_filename)
            uptoken = policy.token()
            ret, err = qiniu.io.put(uptoken, save_filename, upload_file)
            if err is not None:
                return {"status":2, "errmsg":u"文件上传出错"}

            file_url = "http://7xnoif.com1.z0.glb.clouddn.com/"+save_filename
            return {"status":1, "file_url":file_url}

        else:
            return {"status":2, "errmsg":u"文件类型错误"}

    def list_all(self, bucket, rs=None, prefix=None, limit=None):
        if rs is None:
            rs = qiniu.rsf.Client()
        marker = None
        err = None
        while err is None:
            ret, err = rs.list_prefix(bucket, prefix=prefix, limit=limit, marker=marker)
            if not ret:
                return []
            marker = ret.get('marker', None)
            file_list = []
            for item in ret['items']:
                file_list.append(item['key'])
            return file_list
        if err is not qiniu.rsf.EOF:
            # error operation
            pass

    def get_file_info(self, bucket, filename):
        return qiniu.rs.Client().stat(bucket, filename)


if __name__ == '__main__':
    import requests
    url = "http://file.api.weixin.qq.com/cgi-bin/media/get?access_token=g-Cb10GtAgbZM7kHqLKK-ZJ4lMhfX4zHgXsSwrjqO0FrVrIAUAn4xW310psf5RI9ax-aJP--uLD7KdWB41Sfaevhqd8iGW80Sybk9mORlqURVckAweduGPVY48qK5QfPOHJfAJAZSU&media_id=XinYaXTybqtPtDGEhXN-Qgn4tta0TTc2StzUukDvVGsPqXBfHlHzgu7Q5dCnUF2b"
    img_file = requests.get(url)
    upload = qiniu_lib(access_key="3tp3FnwQn_jamkXiQE3HlOwHnItkyd2b_N6i2BMH",
                    secret_key="xogHUWGjKMKaQ5BY8ULNuSglPVYLCgICp9hDR7tT")

    result = upload.upload(upload_file=img_file.content,
                    bucket_name='qipai-activity',file_type='img')
    print result
