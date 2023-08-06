import random


def UpDownChk(com, user):
  if com>user :
    print("업")
    return False 
  elif com<user :
    print("다운")
    return False
  else :
    print("정답")
    return True
#
def compare_val(a, user):
  if a>user :
    print("업")
    return False 
  elif a<user :
    print("다운")
    return False
  else :
    print("정답")
    return True
def main(): 
  print("숫자를 맞춰보세요")
  chkVal = random.randint(1,20)
  print(chkVal)
  for i in range(0, 3):
    #print(str(i)+"번째")
    x = input()
    x = int(x)
    #chk = UpDownChk(chkVal, x)
    chk = compare_val(chkVal, x)
    if chk == True:
      break
    if i==2:
      print("실패")
#  if chkVal>x :
#    print("업")
#  elif chkVal<x :
#    print("다운")
#  else :
#    print("정답")
#    break
 
if __name__ == "__main__":
    main()