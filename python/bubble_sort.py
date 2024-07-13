def bubble_sort(values: list[int]) -> list[int]:
    for i in range(len(values)):
        for ii in range(i, len(values)):
            if values[i] > values[ii]:
                values[i], values[ii] = values[ii], values[i]
    return values


def test_bubble_sort():
    unsorted_list = [5, 1, 0, 3, 4, 2]
    sorted_list = [0, 1, 2, 3, 4, 5]
    assert bubble_sort(unsorted_list) == sorted_list
    assert bubble_sort(unsorted_list) == sorted(unsorted_list)


if __name__ == "__main__":
    from timeit import timeit
    unsorted_list = [0, 3, 2, 1, 4, 5][::-1]
    sorted_list = [0, 1, 2, 3, 4, 5]
    after_sort = bubble_sort(unsorted_list)
    assert after_sort == sorted_list

    n_times = 10_000
    timed = timeit(
        "bubble_sort(unsorted_list)",
        globals=globals(),
        number=n_times
    )
    print(" Bubble Sort ".center(50, "="))
    print(f"Runned {n_times} times, timed in {timed:.5f}")
    print("".center(50, "="))
