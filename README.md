# RESTful Flask API using Celery and RabbitMQ

The service implements the process of determining the number of different types of tags on a Internet page .
The user transmits the page URL using a POST request, in response he receives the task identifier in the queue.
By the task identifier using a GET request, the user receives the task execution status, the user also receives the result of the task execution if the task is successfully completed.

The service is called according to the RPC template; Celery + RabbitMQ is used to implement the queue.
## Deploy service (2 options)

At the first, clone this code to your local and go to the directory
```
git clone
cd RPC_url_calc
```
### Run using docker-compose (recommended)
Install docker compose into a system-wide directory: [docker-compose](https://docs.docker.com/compose/install/);
Open ports 5672 and 15672;
Run docker-compose:
```
sudo docker-compose up --force-recreate --build
```
service available at: [http://0.0.0.0:5000/tags](http://0.0.0.0:5000/tags)
RabbitMQ management interface available at: [http://0.0.0.0:15672](http://0.0.0.0:15672)

### Run with virtual environment
deactivate your virtualenv,
delete .pyc files:
```
make clean-pyc
```
create virtualenv and activate it:
```
make create_venv
source venv/project_env/bin/activate
```
install dependencies from requirements.txt and run server:
```
make dep
make run-gunicorn
```
service available at: [http://0.0.0.0:5000/tags](http://0.0.0.0:5000/tags)
stop: POST request to [http://0.0.0.0:5000/shutdown_g](http://0.0.0.0:5000/shutdown_g)
## Using service:
Post request with URL to get task_id:
```python
def post_req(url):
    r_post = requests.post("http://0.0.0.0:5000/tags", data=json.dumps(url))
    return {'STATUS':r_post.status_code , 'REASON':r_post.reason , 'task_id':r_post.text}
url_json={'url':'http://www.dell.com'} #example url
taskid=post_req(url_json)['task_id']
print(taskid)
```
Get request with task_id to get result/state:
```python
def get_req(task_id):
    r_get = requests.get("http://0.0.0.0:5000/tags", params={'taskn':task_id})
    return {'STATUS':r_get.status_code ,'REASON':r_get.reason ,'RESULT':r_get.text}
result=get_req(taskid)
print(result)
```
