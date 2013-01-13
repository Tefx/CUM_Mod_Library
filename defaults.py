from math import sqrt

mean = lambda l: sum(l)/len(l)

sqrt_3 = 1.73205080757

m0 = lambda p, v, t, m: p * v * t /m

m1 = lambda mpe, k, m: mpe / k / m

m2 = lambda m, k, l:(max(l) - min(l)) / k / m

m3 = lambda t, n, k, w: t * w / k * sqrt(n)

m4 = lambda k, m, v: sqrt(sum([m1(m0, k, v0)**2 for m0, v0 in zip(m, v)]))

def m5(P, p, A, p_0):
    n = len(A)
    p = p * (n/len(p))
    p_ = mean(p)
    A_= mean(A)
    Sxy = sum([(p0-p_)*(A0-A_) for p0, A0 in zip(p, A)])
    Sxx = sum([(p0-p_)**2 for p0 in p])
    b = Sxy/Sxx
    a = A_ - b*p_
    s = sqrt(sum([(A0-a-b*p0)**2 for A0, p0 in zip(A, p)])/(n-2))
    u_p0 = s/b*sqrt(1.0/P+1.0/n+((p_0-p_)**2)/Sxx)
    return u_p0/p_0

def mf(us, w, k): 
    return sqrt(sum([u**2 for u in us]))*w*k

EXPORTS = {
    "mode0": m0,
    "mode1": m1,
    "mode2": m2,
    "mode3": m3,
    "mode4": m4,
    "mode5": m5,
    "modef": mf,
}