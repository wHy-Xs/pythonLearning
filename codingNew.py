'''
1.最大公约数：最大公因数，也称最大公约数、最大公因子，指两个或多个整数共有约数中最大的一个。
'''
def hcf(x, y):
   """该函数返回两个数的最大公约数"""
   # 获取最小值
   if x > y:
       smaller = y
   else:
       smaller = x
   for i in range(1,smaller + 1):
       if((x % i == 0) and (y % i == 0)):
           hcf = i
   return hcf
  
 '''
 辗转相除法:
  a可以表示成a = kb + r, 则r = a mod b
  假设d是a, b的一个公约数， 则有  d|a, d|b, 而r = a - kb, 因此d|r。
  因此，d是(b, a mod b)的公约数。
  加上d是(b，a mod b)的公约数，则d|b, d|r, 但是a = kb + r,因此d也是(a, b)的公约数。
  因此，(a, b) 和(a, a mod b)的公约数是一样的，其最大公约数也必然相等，得证。
 '''
 def gcd(a, b):
  if a < b:
    a, b = b, a
  while b != 0:
    temp = a % b
    a = b
    b = temp
  return a
  ###############################################################################
   '''
   判断一个字符串是否是回文结构
   1.方法1：用python的reverse方法
   2.就是遍历第i个是否等于len()-i-1个
'''
#方法1：
def isPalindrome1(s):
    for i in range(len(s))/2:
        if not s[i] == s[len(s)-i-1]:
            return False
    return True
#方法2：
def isPalindrome2(s):
    return s == s[::-1]
