#1.1 Implement a recursiv function to calculatethe factoriyal of a given count .
def fact_rec(c):
  if c == 0 or c == 1:
    return 1
  else:
    return c * fact_rec(c - 1)


count = 2
res = fact_rec(count)

print("the factorial of {} is{}.".format(count, res))
