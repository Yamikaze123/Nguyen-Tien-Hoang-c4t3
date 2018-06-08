sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hoang and these are my sheep sizes")
print(*sizes)

print("My biggest sheep has size", max(sizes),", let's shear it")

sizes[sizes.index(max(sizes))]=8
print("After shearing, here is my flock")
print(*sizes)

sizes = [size + 50 for size in sizes]
print("A month has passed, now here is my flock")
print(*sizes)

for i in range(3):
    print("MONTH",i+1,":")
    print("One month has passed, now here is my flock")
    sizes = [size + 50 for size in sizes]
    print(*sizes)
    print("The biggest sheep has size",max(sizes),"let's shear it")
    sizes[sizes.index(max(sizes))] = 8
    print("After shearing, here is my flock")
    print(*sizes)

print("My flock has size in total", sum(sizes))
print("I would have",sum(sizes),"* 2$ =",sum(sizes)*2)