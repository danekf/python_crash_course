#basic logic refresher examples

has_high_income = True
has_good_credit = True
has_defaulted_before = False


#and operator
if has_high_income and has_good_credit:
  print("eligible for loan")

#or operator
elif has_high_income or has_good_credit:
  print("eligible for small loan")

##example 2, adding NOT operator
if has_defaulted_before:
  print("Sorry, nbot eligible for a loan")
elif has_high_income and has_good_credit and not has_defaulted_before:
  print("eligible for loan")
elif has_high_income or has_good_credit and not has_defaulted_before:
  print("eligible for small loan")


