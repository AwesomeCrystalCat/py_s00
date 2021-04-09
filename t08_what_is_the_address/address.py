first_var = 1000
second_var = first_var
third_var = 999
ad_1 = id(first_var)
ad_2 = id(second_var)
ad_3 = id(third_var)

print(f"first_var = {first_var}, address is {ad_1}")
print(f"second_var = {second_var}, address is {ad_2}")
print(f"third_var = {third_var}, address is {ad_3}")
print(f"{first_var} is {second_var} = {first_var is second_var}")
print(f"{first_var} is {third_var} = {first_var is third_var}")
