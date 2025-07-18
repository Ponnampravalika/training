print("Using iter():")
fruits = ["apple", "banana", "cherry"]
fruit_iter = iter(fruits)

print(next(fruit_iter))  
print(next(fruit_iter))  
print(next(fruit_iter))  
print("\nUsing enumerate():")
for index, fruit in enumerate(fruits):
    print(f"Index {index} -> {fruit}")
