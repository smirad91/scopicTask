import requests

endpointUrl = 'https://reqres.in/api/users'

def createUser(name, job):
    myObj = {"name":name,
             "job":job}
    x = requests.post(endpointUrl, data=myObj)
    print("Execute {}, with {}".format(endpointUrl, myObj))
    print("Created user {}".format(x.text))
    if not x.ok:
        raise Exception("Error: {}".format(x.text))
    return x.json()

def getUser(id):
    getUrl = endpointUrl+"/"+str(id)
    x = requests.get(getUrl)
    print("Execute: {}".format(getUrl))
    print("Get user with id {0} returned: {1}".format(id, x.text))
    return x.json()

def updateUserJob(id, job):
    putUrl = endpointUrl+"/"+str(id)
    data = {"job": job}
    x = requests.put(putUrl, data)
    print("Execute put: {}, with {}".format(putUrl, data))
    print("Updated user with id {0}, to {1}".format(id, x.text))
    if not x.ok:
        raise Exception("Error: {}".format(x.text))
    return x.json()

def deleteUser(id):
    deleteUrl = endpointUrl+"/"+str(id)
    x = requests.delete(deleteUrl)
    print("Execute delete: {}".format(deleteUrl))
    print(x.text)

def getUsersList():
    x = requests.get(endpointUrl)
    print("Get users list: {}".format(x))
    if not x.ok:
        raise Exception("Error: {}".format(x.text))
    return x.json()