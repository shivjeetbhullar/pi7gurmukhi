chars = {
  u"\u0a4d\u0a30":u"\u0A0B",
  u"\u0a4d\u0a35":u"\u0A00",
  u"\u0a4d\u0a39":u"\u0a11",
  u"\u0a4d\u0a2f":u"\u0204"
}

def Fix_0a3f(Gurmukhi_string):
  char_list = []
  for x in Gurmukhi_string.replace("\u0a3f","*$*&**").split("&**"):
   if x != "":
    if "*$*" in x:
     char_count = -1
     x = x.replace("*$*","")
     while not x[char_count].isalnum():char_count -= 1
     if x[char_count].isalnum():x = x[:char_count]+'\u0a3f'+x[char_count:]
     char_list.append(x)
    else:char_list.append(x)
  return "".join(char_list)

def Fix_chars(G_string):
  for x in chars:G_string=G_string.replace(x,chars[x])
  return Fix_0a3f(G_string)

