from user import User

check = User()
check.email = "email"
check.hashed_password = "paswd"

print(check)
print(check.__dict__)
