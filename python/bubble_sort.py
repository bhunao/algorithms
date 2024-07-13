def bubble_sort(collection: list[int]) -> list[int]:
    return collection


def test_bubble_sort():
    unsorted_list = [0, 1, 2, 3, 4, 5]
    sorted_list = [0, 1, 2, 3, 4, 5]
    assert bubble_sort(unsorted_list) == sorted_list


if __name__ == "__main__":
    from timeit import timeit
    unsorted_list = [0, 1, 2, 3, 4, 5]
    sorted_list = [0, 1, 2, 3, 4, 5]
    assert bubble_sort(unsorted_list) == sorted_list

    n_times = 10_000
    timed = timeit(
        "bubble_sort(unsorted_list)",
        globals=globals(),
        number=n_times
    )
    print(" Bubble Sort ".center(50, "="))
    print(f"bubble_sort runned {n_times} times, timed in {timed:.5f}")
    print("".center(50, "="))
    print("Finished")
