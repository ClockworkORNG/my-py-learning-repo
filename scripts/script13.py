import re

#f = open()
#s = f.readlines()

txt = """Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students 
at Stanford University in California. Together they own about 14 percent +38 096 of its shares and 
control 56 percent of the stockholder voting power through supervoting stock. They incorporated 
+38 096 555-77-77 Google as a California privately held company on September 4, 1998, in California. 
Google was then reincorporated in Delaware on October 22, 2002.[12] An initial public offering (IPO) took place 
on August 19, 2004, and Google moved to its headquarters in Mountain View, California, nicknamed the Googleplex. 
In August 2015, Google announced plans to 38 037 111-22-22reorganize its various interests as a conglomerate called 
Alphabet Inc. Google is Alphabet's leading 38 037subsidiary and will continue to be the umbrella company 
for066 999-33-44Alphabet's Internet interests. Sundar Pichai was appointed CEO of Google, replacing Larry Page who 
became the CEO of Alphabet."""

# +38 XXX XXX-XX-XX
# +38 066 111-22-22

"+38\s\d\d\d\s\d\d\d-\d\d-\d\d"

x = re.findall("\+?38\s(\d{3})\s\d{3}\-\d\d\-\d\d", txt)
#x = re.findall("August(\s\d{1,2},\s\d{4}|\s\d{4})", txt)
print(x)

#August 19, 2004                    \w+\s\d{1,2},\s\d{4}
#August 2015  August 19, 2004      August\s\d{1,2},\d{4}

# ? - 0,1
# * - 0, Infinity
# + - 1, Infinity