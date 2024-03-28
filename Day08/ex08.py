# 어노테이션

def greet(name: str) -> str:
    return "Hello, " + name

print(greet("Alice"))  # 출력: Hello, Alice
print(greet(123))      # 출력: TypeError: Argument 'name' must be str
