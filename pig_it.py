# input "are here they"
# output "reay erehay heytay"
def pig_it(text):
    return " ".join( [s[1:]+s[0] + "ay" if s.isalpha() else s for s in text.split(" ")])

print(pig_it("are here they"))