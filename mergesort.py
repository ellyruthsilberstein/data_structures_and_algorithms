def mergesort(input):
  if len(input) == 1:
    return input
  else: 
    a = mergesort(input[:len(input)/2])
    b = mergesort(input[len(input/2:])
    
    output = []
    while len(a) > 0 or len(b) > 0:
      if len(a) == 0:
        output += b 
        break
      elif len(b) == 0:
        output += a
        break
      elif a[0] < b[0]:
        output.append(a.pop(0))
      else:
        output.append(b.pop(0))
    return output
    
print(mergesort(input))
