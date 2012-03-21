from expression import Expression


def main():
    exp = Expression("2 / 3 * 4")
    print exp.solve(None)

if __name__ == '__main__':
    main()
