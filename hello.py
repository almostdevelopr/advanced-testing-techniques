def addthis(x,y):
  import pdb;pdb.set_trace()
  print(f"X: {x} | Type: {type(x)} and Y: {y} | Type: {type(y)}")
  try:
    result=x+y
  except TypeError:
    print(f"The wrong type passed")
    result = int(x)+int(y)
  
  print(f"Result: {result}")
  return result

print(addthis('1',3))