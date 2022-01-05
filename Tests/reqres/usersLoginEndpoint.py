from Lib.reqres import LoginEndpoint, UsersEndpoint



user = UsersEndpoint.getUsersList()[0]
LoginEndpoint.loginUser(user["email"], user["password"])