T = int(input())
for tc in range(1, T+1):
    word = input()

    print('..#.' * len(word) + '.')
    print('.#.#' * len(word) + '.')

    for i in range(len(word)):
        if i == len(word)-1:
            print('#.' + word[i] + '.#')
        else:
            print('#.' + word[i] + '.', end="")

    print('.#.#' * len(word) + '.')
    print('..#.' * len(word) + '.')
