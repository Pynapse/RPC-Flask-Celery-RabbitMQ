import requests

def post_req(url):
    r_post = requests.post("http://127.0.0.1:5000/tags", data=url)
    return {'STATUS':r_post.status_code , 'REASON':r_post.reason , 'task_id':r_post.text}

def get_req(task_id):
    params={'taskn':task_id}
    r_get = requests.get("http://127.0.0.1:5000/tags", params=params)
    return {'STATUS':r_get.status_code ,'REASON':r_get.reason ,'RESULT':r_get.text}

taskid=post_req('http://www.google.com')['task_id']
result=get_req(taskid)

#stop server:
r = requests.post("http://127.0.0.1:5000/shutdown") #for flask
r = requests.post("http://127.0.0.1:5000/shutdown_g") #for gunicorn
