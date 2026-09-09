from client import SIMDVectorEngine

def main():
    print("=== Testing SIMD Vector Lane Engine ===")
    simd = SIMDVectorEngine()
    a = [2.0] * 8
    b = [3.0] * 8
    c = [1.0] * 8
    mask = [True, True, False, False, True, True, False, False]

    res = simd.fma(a, b, c, mask)
    print("Masked FMA (a * b + c):", res)
    assert res[0] == 7.0
    assert res[2] == 1.0 # unmasked preserved c

    h_sum = simd.horizontal_add(res)
    print("Horizontal reduction sum:", h_sum)
    assert h_sum == 32.0
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
