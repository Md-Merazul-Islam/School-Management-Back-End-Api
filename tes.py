 
username_or_email="meraz@gmai.com"
password ="meraz1234"
if "@" in username_or_email:
    user_obj = User.objects.get(email=username_or_email)
     user = authenticate(username=user_obj.username, password=password)
else:
    user = user = authenticate(username=username_or_email, password=password)
    
    
else:
    print("False")