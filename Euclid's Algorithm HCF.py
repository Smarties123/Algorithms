def euclid_hcf(a,b):
    if b == 0:
        return a
    return euclid_hcf(b, a%b)

print(euclid_hcf(24,36))
    