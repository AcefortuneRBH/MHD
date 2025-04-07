AUTHORIZED_USER = "Mahdi, Slave of the Lord"

def authenticate_user(identity):
    if identity == AUTHORIZED_USER:
        return f"✅ Access Granted: Welcome, {identity}."
    else:
        return "❌ Access Denied: You are not authorized to control MHD."

user_identity = input("Enter your identity: ")
print(authenticate_user(user_identity))

