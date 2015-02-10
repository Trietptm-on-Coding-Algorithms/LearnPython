import re

pattern= 'test'
string1= 'this is a test or another test2 test3'
string2= 'test is a failure'
string3= 'success=1 and failure != 23'

"""
Search for the first occurence of a pattern in a string
"""
m1= re.search(pattern, string1)
print "First position and occurence of the pattern in the string"
print m1.start(), m1.end(), m1.group()

"""
Check if the string starts with a specific pattern
"""
m1= re.match(pattern, string2)
print "Regex using match()"
print m1.group()

"""
Create a pattern which can be used multiple times. It returns a regex object that can then be used in search() and match()
For anything complex it is probably good to use this instead of match or search. If its very simple matching though, compile isn't needed.
"""
variable= 'failure'
regex=re.compile(r'^(.*?=\d)\s{1}and\s{1}%s\s!=\s{1}\d[23]$'%variable,re.IGNORECASE|re.DOTALL|re.MULTILINE|re.X)
m1=regex.match(string3)
if m1:
    print "Regex using compile()"
    print m1.start(), m1.group()

"""
Split string by regex. This is useful in case you want to split strings using complex patterns. For normal strings the default Python split
call can be used.
"""
l1= []
l1= re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
print "Splitting a string using regex"
print l1

"""
Find all occurences of a pattern in a string
"""
flags= re.IGNORECASE|re.DOTALL
t1= re.findall(pattern, string1, flags) 
print t1

"""
Substitute a pattern in a string with a new pattern
"""
s2= re.sub('test','ball',string1)
print s2
