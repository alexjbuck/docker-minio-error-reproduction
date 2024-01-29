import multiprocessing
from lib import boto3_read, boto3_write

if __name__ == "__main__":
    N = 7
    # Writing large file
    boto3_write(1_900_000_000)

    # Reading large file
    for i in range(10):
        with multiprocessing.Pool(processes=N) as pool:
            pool.map(boto3_read, range(N))
