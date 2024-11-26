lp_list = list(filter(lambda x:(x%400 == 0) or (x%100 != 0 and x%4 == 0),range(2024,3010)))
print(f"All leap year between 2024 to 3010 are :{lp_list}")
