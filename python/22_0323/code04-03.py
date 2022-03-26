a = ord('A') #해당 문자의 유니코드 코드 포인트를 나타내는 정수를 돌려줍니다
mask = 0x0F

print("%x & %x = %x" %(a, mask, a & mask))
print("%x | %x = %x" %(a, mask, a | mask))

mask = ord('a') - ord('A')

b = a ^ mask
print("%c ^ %d = %c" %(a, mask, b))
a = b ^ mask
print("%c ^ %d = %c" %(b, mask, a))