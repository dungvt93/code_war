import re

test = "[+05621]"
mod4 = re.compile("(\[[\+,\-]*\d*00\]|04\]|08\]|12\]|16\]|20\]|24\]|28\]|32\]|36\]|40\]|44\]|48\]|52\]|56\]|60\]|64\]|68\]|72\]|76\]|80\]|84\]|88\]|92\]|96\])|(\[[\+,\-]*0\]|4\]|8\])")
mod4.match(test)
