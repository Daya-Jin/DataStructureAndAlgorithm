from bitarray import bitarray    # 提供list-like的bit数据结构
import mmh3    # 实现了MurmurHash3算法


class BloomFilter(set):
    def __init__(self, m, k):
        super(BloomFilter, self).__init__()
        self.bit_array = bitarray(m)
        self.bit_array.setall(0)
        self.m = m
        self.k = k

    def __len__(self):
        return self.m

    def __iter__(self):
        return iter(self.bit_array)

    def add(self, item):
        for i in range(self.k):
            index = mmh3.hash(item, i) % self.m
            self.bit_array[index] = 1

    def __contains__(self, item):
        res = True
        for i in range(self.k):
            index = mmh3.hash(item, i) % self.m
            if self.bit_array[index] == 0:
                res = False

        return res


def main():
    bloom = BloomFilter(100, 10)
    animals = ['dog', 'cat', 'giraffe', 'fly', 'mosquito', 'horse', 'eagle',
               'bird', 'bison', 'boar', 'butterfly', 'ant', 'anaconda', 'bear',
               'chicken', 'dolphin', 'donkey', 'crow', 'crocodile']
    # First insertion of animals into the bloom filter
    for animal in animals:
        bloom.add(animal)

    for animal in animals:    # 已存在元素的查找
        if animal in bloom:
            print('{} is in bloom filter as expected'.format(animal))
        else:    # 已存在元素不应该存在误判，否则就是出现严重错误
            print('Something is terribly went wrong for {}'.format(animal))
            print('FALSE NEGATIVE!')

    # Membership existence for not inserted animals
    # There could be false positives
    other_animals = ['badger', 'cow', 'pig', 'sheep', 'bee', 'wolf', 'fox',
                     'whale', 'shark', 'fish', 'turkey', 'duck', 'dove',
                     'deer', 'elephant', 'frog', 'falcon', 'goat', 'gorilla',
                     'hawk']
    for other_animal in other_animals:
        if other_animal in bloom:
            print('{} is not in the bloom, but a false positive'.format(other_animal))
        else:
            print('{} is not in the bloom filter as expected'.format(other_animal))


if __name__ == '__main__':
    main()
