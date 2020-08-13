#  import simple  # this fails on PyPi (runs locally)
import sample.simple as simple  # works locally, and PyPi

def main():
    print("add_one(2) = " + str(simple.add_one(2)))


if __name__ == '__main__':
    main()