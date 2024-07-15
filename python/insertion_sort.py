def insertion_sort(values: list[int]) -> list[int]:
    return values


def test_insertion_sort():
    unsorted_list = [5, 1, 0, 3, 4, 2]
    sorted_list = [0, 1, 2, 3, 4, 5]
    assert insertion_sort(unsorted_list) == sorted_list
    assert insertion_sort(unsorted_list) == sorted(unsorted_list)


if __name__ == "__main__":
    from timeit import timeit
    unsorted_list = [0, 3, 2, 1, 4, 5][::-1]
    sorted_list = [0, 1, 2, 3, 4, 5]
    after_sort = insertion_sort(unsorted_list)
    assert after_sort == sorted_list

    n_times = 10_000
    timed = timeit(
        "insertion_sort(unsorted_list)",
        globals=globals(),
        number=n_times
    )
    print(" Bubble Sort ".center(50, "="))
    print(f"Runned {n_times} times, timed in {timed:.5f}")
    print("".center(50, "="))
