import pandas
import random
import string
import time


# iteration range
NUM_RANGE = 10000000

# list of char a..z
CHAR_LIST = [c for c in string.ascii_lowercase]

# count of columns of DataFrame
COLUMN_COUNT = 100

# count of rows of DataFrame
ROW_COUNT = 10000


def list_int_with_iteration(num_range):
    """
    Generate int list with iteration

    Parameters
    ----------
    num_range : int
        iteration count
    """
    print("--------------------------------------------------")
    print("List int with iteration")
    ret = []
    start_time = time.time()
    for i in range(num_range):
        ret.append(i)
    end_time = time.time()
    print(f"time: {(end_time - start_time) * 1000} ms")
    print("--------------------------------------------------")


def list_int_with_comprehension(num_range):
    """
    Generate int list with comprehension

    Parameters
    ----------
    num_range : int
        iteration count
    """
    print("--------------------------------------------------")
    print("List int with comprehension")
    start_time = time.time()
    ret = [i for i in range(num_range)]
    end_time = time.time()
    print(f"time: {(end_time - start_time) * 1000} ms")
    print("--------------------------------------------------")


def list_char_with_iteration(num_range):
    """
    Generate str list with iteration

    Parameters
    ----------
    num_range : int
        iteration count
    """
    print("--------------------------------------------------")
    print("List str with iteration")
    ret = []
    start_time = time.time()
    for _ in range(num_range):
        ret.append(random.choice(CHAR_LIST))
    end_time = time.time()
    print(f"time: {(end_time - start_time) * 1000} ms")
    print("--------------------------------------------------")


def list_char_with_comprehension(num_range):
    """
    Generate str list with comprehension

    Parameters
    ----------
    num_range : int
        iteration count
    """
    print("--------------------------------------------------")
    print("List str with comprehension")
    start_time = time.time()
    ret = [random.choice(CHAR_LIST) for _ in range(num_range)]
    end_time = time.time()
    print(f"time: {(end_time - start_time) * 1000} ms")
    print("--------------------------------------------------")


def df_with_iteration(col_count, row_count):
    print("--------------------------------------------------")
    print("df with iteration")
    start_time = time.time()
    ret = pandas.DataFrame(index={}, columns=[col for col in range(col_count)])
    for _ in range(row_count):
        series = []
        for _ in range(col_count):
            series.append(random.randrange(100))
        ret = ret.append(pandas.Series(series), ignore_index=True)
    end_time = time.time()
    print(f"time: {(end_time - start_time) * 1000} ms")
    print("--------------------------------------------------")


def df_with_comprehension(col_count, row_count):
    print("--------------------------------------------------")
    print("df with comprehension")
    start_time = time.time()
    ret = pandas.DataFrame([[random.randrange(100) for _ in range(col_count)] for _ in range(row_count)])
    end_time = time.time()
    print(f"time: {(end_time - start_time) * 1000} ms")
    print("--------------------------------------------------")


def main():
    list_int_with_iteration(NUM_RANGE)
    list_int_with_comprehension(NUM_RANGE)

    list_char_with_iteration(NUM_RANGE)
    list_char_with_comprehension(NUM_RANGE)

    df_with_iteration(COLUMN_COUNT, ROW_COUNT)
    df_with_comprehension(COLUMN_COUNT, ROW_COUNT)

if __name__ == '__main__':
    main()
