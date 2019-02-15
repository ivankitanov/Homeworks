def avg_grades(list, *argv):
  for arg in argv:
    list.append(arg)
  return float(sum(list))/float(len(list))