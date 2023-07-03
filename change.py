print("Please enter an amount in cents less than a dollar.")
user_input = int(input())
print("Your change will be:")
print("Q:" + str(user_input // 25))
user_input = user_input % 25
print("D:" + str(user_input // 10))
user_input = user_input % 10
print("N:" + str(user_input // 5))
user_input = user_input % 5
print("P:" + str(user_input))

# :D