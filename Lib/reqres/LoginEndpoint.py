import requests
endpointUrl = "https://reqres.in/api/login"

def loginUser(email, password):
    myObj = {"email":email,
             "password":password}
    x = requests.post(endpointUrl, data=myObj)
    print("Execute post {}, with {}".format(endpointUrl, myObj))
    print("Returned token: {}".format(x.text))
    if not x.ok:
        raise Exception("Error: {}".format(x.text))
    if "token" not in x.text:
        raise Exception("token not returned")
    return x.json()