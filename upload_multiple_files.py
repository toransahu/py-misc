import requests

url = 'http://127.0.0.1:8000/api/v1/posts/19/'
with open('/home/toran/Desktop/FB_IMG_1475551548845.jpeg', 'rb') as f:
    files = {'thumbnail': ('fb.jpeg', f)}
    f_aws = open('/home/toran/Pictures/aws-https.png', 'rb')

    files = {'thumbnail': ('aws.png', f_aws)}
    multiple_files = [
        ('images', ('foo.png', f)),
        ('images', ('bar.png', f)),
        ('thumbnail', ('aws.png', f_aws)),
    ]

    data = {'content': 'abcd'}
    
    res = requests.patch(url, data, files=multiple_files, headers={'content_type': 'multipart/form-data'})
    print(res.text)


# blog_url = 'http://127.0.0.1:8000/api/v1/blogs/1/'
# files = {'thumbnail': ('aws.png', open('/home/toran/Pictures/aws-https.png', 'rb'))}
# res = requests.patch(blog_url, files=files, headers={'content_type': 'multipart/form-data'})
# print(res.text)