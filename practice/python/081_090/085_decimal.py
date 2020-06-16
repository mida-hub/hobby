
from decimal import Decimal, ROUND_DOWN, ROUND_UP, ROUND_HALF_UP

float_num = 1.01
float_sum = 0.0

for _ in range(100):
    float_sum += float_num

print(f'float_sum = {float_sum}')

decimal_num = Decimal("1.01")
decimal_sum = Decimal("0.0")

for _ in range(100):
    decimal_sum += decimal_num

print(f'decimal_sum = {decimal_sum}')

# 四則演算

print('-'*50)
decimal_val = Decimal("2.02")
print(decimal_num / decimal_val)
print(decimal_num * decimal_val)
print(decimal_num + decimal_val)
print(decimal_num - decimal_val)

# 切り捨て、四捨五入、切り上げ

print('-'*50)
decimal_val = Decimal("87.325")
print(decimal_val)
print(decimal_val.quantize(Decimal("0.00"), rounding=ROUND_DOWN))
print(decimal_val.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP))
print(decimal_val.quantize(Decimal("0.00"), rounding=ROUND_UP))

print('-'*50)
decimal_val = Decimal("87.321")
print(decimal_val)
print(decimal_val.quantize(Decimal("0.00"), rounding=ROUND_DOWN))
print(decimal_val.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP))
print(decimal_val.quantize(Decimal("0.00"), rounding=ROUND_UP))
