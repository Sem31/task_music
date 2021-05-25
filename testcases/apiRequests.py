import requests

def post(data, files):
    # headers = {'Content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'}
    response = requests.post("http://127.0.0.1:8000/songs_api/",files=files, data=data)
    return response

def get() :
    response = requests.get("http://127.0.0.1:8000/songs_api/")
    return response

def delete(id):
    response = requests.delete("http://127.0.0.1:8000/songs_api/"+str(id))
    return response

def put(id, data):
    response = requests.put("http://127.0.0.1:8000/songs_api/"+str(id), data= data)
    return response

def patch(id, data):
    response = requests.patch("http://127.0.0.1:8000/songs_api/"+str(id), data= data)
    return response

