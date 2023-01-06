new_list = [ 5, -12, 10, 1337, -1337, 98, ]
for i in new_list:
  if "" in new_list:
    new_list.remove("")
only_positives = list(filter(lambda x: (x > 0), new_list))
 
print("Positives: ", *only_positives)