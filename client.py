class SIMDVectorEngine:
    """
    AVX-512 / NEON-style vector lane emulation.
    Lanes: 8x 32-bit floats.
    Supports Masked FMA (Fused Multiply Add), Horizontal Reduction, and Blend.
    """
    LANES = 8

    def fma(self, a, b, c, mask=None):
        if mask is None:
            mask = [True] * self.LANES
        res = [0.0] * self.LANES
        for i in range(self.LANES):
            if mask[i]:
                res[i] = a[i] * b[i] + c[i]
            else:
                res[i] = c[i]
        return res

    def horizontal_add(self, vec):
        return sum(vec)

    def blend(self, a, b, mask):
        return [b[i] if mask[i] else a[i] for i in range(self.LANES)]
