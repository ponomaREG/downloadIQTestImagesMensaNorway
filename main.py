from bs4 import BeautifulSoup as bs
import os
import base64
import urllib3

f = open("forBS.txt",'r')
# url = 'http://test.mensa.no'
# http_pool = urllib3.connection_from_url(url)
# r = http_pool.urlopen('GET',url)
# food = r.data
food = f.read()
soup = bs(food,"html.parser")

id_answer = 'answer-'
for i in range(1,36):
    matrise_n = "matrise-"+str(i)
    os.mkdir(matrise_n)
    for j in range(1,7):
        id_answer = 'answer-'+str(i)+'-'+str(j)
        path = matrise_n+'/'+id_answer+'.png'
        answers = soup.find("img", {"class": "choice btn btn-default",'id':id_answer})
        print(answers)
        img_data = str(answers['src']).split("base64,")[1]
        # print(img_data)
        with open(path, "wb") as fh:
            fh.write(base64.b64decode(img_data))
        fh.close()

    tasks = soup.find("img",{"id":matrise_n})
    img_data = str(tasks['src']).split("base64,")[1]
    path = matrise_n+'/' + matrise_n + '.png'
    with open(path, "wb") as fh:
        fh.write(base64.b64decode(img_data))
    fh.close()

f.close()