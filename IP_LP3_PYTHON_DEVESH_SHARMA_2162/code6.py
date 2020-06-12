#code6
def code6(str):
  s_not = str.find('not')           #to find not in the string
  s_poor = str.find('poor')         #to find poor in the string
  

  if s_poor > s_not and s_not>0 and s_poor>0:
    str = str.replace(str[s_not:(s_poor+4)], 'good')    #replace not poor with good
    return str
  else:
    return str
print (code6 ('The lyrics is not that poor!'))
print(code6('The lyrics is poor!'))
 
