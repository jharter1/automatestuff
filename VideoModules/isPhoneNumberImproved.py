import re


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Call me maybe at 312-867-5309 or maybe at 224-381-6465'))
