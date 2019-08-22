l=["http://www.dasfk.com","www.try.com","www.google.com"]
ln=[(i if i[0:7]=="http://" else ("http://"+i)) for i in l]#"""if i[0:6]=="https://" i else "https://"+i """
print (ln)
"""
['http://www.dasfk.com', 'http://www.try.com', 'http://www.google.com']
"""
