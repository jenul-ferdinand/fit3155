"""
Write psuedocode for an algorithm that takes two strings S[1..M] and T[1..N] and
returns the length of the longest suffix of S that exactly matches a prefix 
of T. 

+ What is the worst case time complexity of your algorithm.
"""

def zalg(string: str) -> list[int]:
    n = len(string)
    z = [0] * n
    z[0] = n
    left, right = -1, -1
    for k in range(1, n):
        if k > right:
            i = 0
            while k + i < n and string[i] == string[k + i]:
                i += 1
            z[k] = i
            if z[k] > 0:
                left = z[k]
                right = z[k] + i
        elif k <= right:
            z[k] = min(z[k - left], right - k)

            if z[k - left] == right - k:
                i = 0
                while right + i < n and string[right + i] == string[right - k + i]:
                    i += 1
                z[k] += i
                if z[k] > 0:
                    left = z[k]
                    right = z[k] + i
    return z


def get_suffix_prefix_length(suffstring: str, prestring: str) -> int:
    string = prestring + '$' + suffstring
    n = len(string)

    z = zalg(string)
    z[0] = 0

    # Return the match starting position z value that reaches the end of the 
    # whole string we inputted into zalg.
    return next((z[k] for k in range(n) if k + z[k] == n), 0)

if __name__ == '__main__':
    length = get_suffix_prefix_length(suffstring='aab', prestring='baa')
    correct = 1
    assert length == correct, f'\nExpected {correct},\nGot {length}'

    del length; del correct

    length = get_suffix_prefix_length(suffstring='aab', prestring='aab')
    correct = 3
    assert length == correct, f'\nExpected {correct},\nGot {length}'

    del length; del correct

    length = get_suffix_prefix_length(suffstring='aab', prestring='abaa')
    correct = 2
    assert length == correct, f'\nExpected {correct},\nGot {length}'

    del length; del correct

    length = get_suffix_prefix_length(suffstring='abab', prestring='abab')
    correct = 4
    assert length == correct, f'\nExpected {correct},\nGot {length}'

    del length; del correct

    length = get_suffix_prefix_length(suffstring='aab', prestring='xyz')
    correct = 0
    assert length == correct, f'\nExpected {correct},\nGot {length}'

    del length; del correct

    length = get_suffix_prefix_length(suffstring='abcabc', prestring='abcx')
    correct = 3
    assert length == correct, f'\nExpected {correct},\nGot {length}'

    

    
    