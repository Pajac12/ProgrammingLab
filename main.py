def sum_list(my_list):
  if (not any(my_list)):
    return None
  else:
    return sum(my_list)


my_list = []
print("Il risultato è: {}".format(sum_list(my_list)))
