import re
print("6. Quantifiers")
text = "ab abb abbb abbbb a"
print("ab*  →", re.findall(r'ab*', text))
print("ab+  →", re.findall(r'ab+', text))
print("ab?  →", re.findall(r'ab?', text))
print("ab{2}→", re.findall(r'ab{2}', text))
print("ab{2,3}→", re.findall(r'ab{2,3}', text))

