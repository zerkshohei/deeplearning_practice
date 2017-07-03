import re

rmine = re.compile("abc")
print rmine.search("waceabcae").group()
