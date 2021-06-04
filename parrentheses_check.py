open = ["[","{","("]
close = ["]","}",")"]

def check(msStr):
  stack =[]
  for i in msStr:
    if i in open:
      stack.append(i)
    elif i in close:
      pos = close.index(i)
      if ((len(stack)>0) and (open[pos] == stack[len(stack)-1])):
        stack.pop()
      else:
        return "no"
  if len(stack) == 0:
    return "yes"
  else:
    return "no"

string = "{{[[(()]]}}"
print(check(string))
  
