# Setting
fileName = 'ids.txt'
prefix = 'S-'
postfix = '-A'
start = 1
end = 50
step = 1
leadingZeros = len(str(end))


def gen_id():
  fileDesc = open(fileName, 'wt')

  if (start >= end):
    print('Start more than End')
    return
  elif (step <= 0):
    print('Step is too small')
    return
  else:
    for i in range(start, end + step, step):
      id = '{0}{1}{2}'.format(prefix, str(i).zfill(leadingZeros), postfix)
      print(id)

      if (i != end):
        fileDesc.write('{0}\n'.format(id))
      else:
        fileDesc.write('{0}'.format(id))
    print('File {0} was created'.format(fileName))
  fileDesc.close()


gen_id()
