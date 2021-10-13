def main():
    v1 = int(input())
    w1 = int(input())
    z1 = int(input())

    v2 = int(input())
    w2 = int(input())
    z2 = int(input())
    answer_found = False

    for v in range(-10, 11):
        for w in range(-10,11):
            if v1 * v+w1 * w == z1 and v2 * v + w2 * w == z2:
                print(v,w)
                answer_found = True

    if not answer_found:
        print("No solution")

if __name__ =="__main__":
    main()