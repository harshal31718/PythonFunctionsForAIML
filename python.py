# 1.Read CSV
# file_format: header + data
# handle_missing: convert null to 0
# return: [{header:value}]
def read_csv(path):
  result =[]
  with open(path,mode="r") as file1:
    lines=file1.readlines()
    headers = lines[0].strip().split(',')
    for data_line in lines[1:]:
      item_dict = {}
      values=[]
      for item in data_line.strip().split(','):
        if item == '': item = 0
        values.append(float(item))       
      for value,header in zip(values,headers):
        item_dict[header]=value     
      result.append(item_dict)
  return result

# 2.Emi Calculator
def emi_calculator(amount,duration,rate,down_payement):
  loan_amount=amount-down_payment
  try:
    emi= loan_amount * rate * ((1+rate)**duration)/ (((1+rate)**duration)-1)
  except ZeroDivisionError:
    emi =loan_amount/duration
  emi= math.ceil(emi)
  return emi
