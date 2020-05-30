width = 80
def center(s,width):
  if width < len(s):
    return s
  spaces = (width - len(s)) // 2
  result = " " * spaces + s
  return result
def main():
  print(center("A Famous Story", width))
  print(center("by:",width))
  print(center("Someone Famous", width))
  print()
  print("Once upon a time...")
main()