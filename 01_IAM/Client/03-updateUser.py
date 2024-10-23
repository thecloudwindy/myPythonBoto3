import boto3

def iam_client():
    client = boto3.client('iam')
    return client

def updateUser(oldUserName, newUserName):
    response = iam_client().update_user(
        UserName = oldUserName,
        NewUserName = newUserName
    )

if __name__ == '__main__':
    oldUserName = input("Enter the User Name: ")
    newUserName = input("Enter the New User Name: ")
    result = updateUser(oldUserName, newUserName)
    print(result)
    