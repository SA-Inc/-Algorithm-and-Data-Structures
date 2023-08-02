def excell_col_to_number(column_title: str) -> int:
  number = 0

  for i in range(0, len(column_title), 1):
    # get alphabet position from ascii upper case
    digit = ord(column_title[i].upper()) - 65 + 1
    number = number * 26 + digit

  return number

print(excell_col_to_number('AG'))
