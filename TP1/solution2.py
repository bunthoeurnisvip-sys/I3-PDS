total_second = 10155
hour = total_second // 3600
minute = (total_second % 3600) // 60
second = total_second % 60
print(f"\n{total_second} seconds", " = ", f"{hour} hours, {minute} minutes, {second} seconds")
print((hour * 3600) + (minute * 60) + second == total_second)
print("=========================================\n")