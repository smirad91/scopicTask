from Lib.reqres import UsersEndpoint

### create user and check if created
createdUser = UsersEndpoint.createUser("randomnamesds", "randomjob")
getCreatedUser = UsersEndpoint.getUser(createdUser["id"])
if createdUser!=getCreatedUser:
    raise Exception("Created user not working properly")


### update user job and check if updated
userJob = createdUser["job"]
newJob="new job"
UsersEndpoint.updateUserJob(createdUser["id"], newJob)

updatedUser = UsersEndpoint.getUser(createdUser["id"])
if userJob==updatedUser["job"]:
    raise Exception("User not updated. Expected {0}, actual job {1}".format(newJob, updatedUser["job"]))


### delete user and check if deleted
UsersEndpoint.deleteUser(updatedUser["id"])

if UsersEndpoint.getUser(updatedUser["id"])!={}:
    raise Exception("User not deleted successfully")