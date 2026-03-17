
def zalg(string: str) -> list[int]:
    n = len(string) # 18
    z = [0] * n
    z[0] = n

    left, right = 0, 0

    for k in range(1,n):
        k_mirror = k - left
        zbox_offset = right - k
        
        # case 1 (k > r)
        if k > right:
            i = 0
            while k + i < n and string[i] == string[k + i]:
                i += 1
            z[k] = i
            if z[k] > 0:
                left = k
                right = z[k]
        # case 2 (k <= r)
        elif k <= right:
            # 2a
            if z[k_mirror] < zbox_offset:
                z[k] = z[k - left]

            # 2b: 
            elif z[k_mirror] > zbox_offset:
                z[k] = right - k
                # 2c: extend past right of zbox
                if z[k_mirror] == zbox_offset:
                    i = 0
                    while k - i < n and string[right + i] == string[right - k + i]:
                        i += 1
                    z[k] += i
                    if z[k] > 0:
                        left = k
                        right = k + z[k]
    
    return z

if __name__ == '__main__':
    z = zalg("aabcaabxaabcaabcay")
    print(z)

    assert z[0] == 18
    assert z == [18,1,0,0,3,1,0,0,7,1,0,0,5,1,0,0,1,0]