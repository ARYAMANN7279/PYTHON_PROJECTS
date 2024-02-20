def format_name(a,b):
  a=a[0].upper()+a[1:].lower()
  b=b[0].upper()+b[1:].lower()
  return(a+" "+b)
f_name=input("enter your first name ")
l_name=input("enter your last name ")
print(f"Your name in title format is {format_name(f_name,l_name)}")     