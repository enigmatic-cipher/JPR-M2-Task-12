"""
Given a string as input, change the case of all the alphabets in the string.
Input-> "INDIA great"
Output-> india GREAT
"""

st = "INDIA great"
ln = len(st)
for i in range(0,ln):
  e = st[i]
  if(e.isupper()) == True:
    e = e.lower()
    st[i] = e
  elif(e.islower()) == True:
    e = e.upper()
    st[i] = e
print(st)

