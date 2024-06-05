#program list
def get_names():
    names = []
    while True:
        name = input("Enter a name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        names.append(name)
    return names

def main():
    names = get_names()
    unique_names = sorted(set(names))
    print("\nSorted list of unique names:")
    for name in unique_names:
        print(name)
    print(f"\nTotal number of names entered: {len(names)}")

if __name__ == "__main__":
    main()
