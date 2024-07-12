def bubble_sort(collection: list[int]) -> list[int]:
    return collection


def test_bubble_sort():
    example_1 = [0, 1, 2, 3, 4, 5]
    anwser_1 = [0, 1, 2, 3, 4, 5]
    assert bubble_sort(example_1) == anwser_1


if __name__ == "__main__":
    example_1 = [0, 1, 2, 3, 4, 5]
    anwser_1 = [0, 1, 2, 3, 4, 5]
    assert bubble_sort(example_1) == anwser_1

    print("Run...")
