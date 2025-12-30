from auth import hash_password, verify_password

h = hash_password("mypassword")

print(verify_password("mypassword", h))   
print(verify_password("wrongpass", h))   
