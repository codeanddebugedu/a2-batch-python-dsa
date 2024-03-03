"""
Write a Python code to find the occurrence of each element in a list 
and print the element with the highest occurrence.
"""
my_list = ["Anirudh", 1, 1, 1, 2, 3, 154, 65, 2, 2, 1, 44, 5, 154, 154, "Anirudh"]

unique_elements = []

for i in my_list:
    if i not in unique_elements:
        unique_elements.append(i)

# Print the frequencies and keep track of the largest frequency and that element
highest_frequency = 0
highest_frequency_element = 0

for i in unique_elements:
    freq = my_list.count(i)
    print(f"{i} occurs {freq} times")
    if freq > highest_frequency:
        highest_frequency = freq
        highest_frequency_element = i

print(f"Highest frequency = {highest_frequency}")
print(f"Highest frequency element = {highest_frequency_element}")
