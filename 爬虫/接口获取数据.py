import requests
import re

headers = {
    'Accept': 'application / json, text / javascript, * / *; q = 0.01',
    'Host': 'vapi.51job.com',
    'Origin': 'https://jobs.51job.com',
    'Referer': 'https://jobs.51job.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

url = 'https://vapi.51job.com/job.php?apiversion=400&module=jobinfo&clientid=000005&type__1260=n4mx0DuD2DcDBDR2DxlEjDkDyG13A%2BIYI%2BD'
datas = {'data': '{"jobid":"145456195","usertoken":false,"hr":true}',
         'sign': 'fbd3cd48d1690e471398a147b09dc9a7'}
r = requests.post(url, headers=headers, data=datas, timeout=100)
r.encoding = 'utf8'
a = r.text
print(re.findall(r'[{](.*?)[}]',a, re.M|re.I))
b=zip(dict(a))
print(r)

