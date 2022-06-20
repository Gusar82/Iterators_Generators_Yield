
import itertools

class FlatIterator1:
    def __init__(self, list_: list):
        self.list_ = list(itertools.chain(*list_))
        self.len_list = len(self.list_)

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= self.len_list:
            raise StopIteration
        return self.list_[self.cursor]


class FlatIterator2:
    def __init__(self, list_: list):
        self.iter = itertools.chain(*list_)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter)


def flat_generator(iterable):
    iter_ = iter(iterable)
    for element in iter_:
        if isinstance(element, list):
            for i in flat_generator(element):
                yield i
        else:
            yield element


def main():
    nested_list = [
        ['a', 'b', 'c', [1, 2]],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    for item in FlatIterator3(nested_list):
        print(item, end=" ")
    print()
    for item in flat_generator(nested_list):
        print(item, end=' ')


if __name__ == '__main__':
    main()
