from  flask import Flask
import json
app=Flask(__name__)
@app.route('/')
def index():
    with open('/home/shiyanlou/files/helloshiyanlou.json','r') as files:
        title1=json.loads(files.read())
        with open('/home/shiyanlou/files/helloworld.json','r') as files2:
            title2=json.loads(files2.read())   
    return title2['title']+title1['title']

@app.route('/files/<filename>')
def file(filename):
    with open('/home/shiyanlou/files/'+filename+'.json','r') as files3:
        content1=json.loads(files3.read())
    return content1['content'].split('\n')
     
