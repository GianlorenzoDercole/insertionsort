def i_sort(li):

  index_range = range(1, len(li))

  for i in index_range:
    v = li[i]

    while li[i -1] > v and i > 0:
      li[i] , li[i-1] = li[i-1] , li[i]
      i = i - 1
  return li

print(i_sort([5,4,6,5,7]))
