chdd=[]
layer = 0
for a in range(0, ncol):
    chdd.append(((layer, 1, ncol-14), 100))
    chdd.append(((layer, 1, ncol-3), 100))
    if a != ncol-14 and a != ncol:
        chdd.append(((layer, 23, 1),95))
        chdd.append(((layer, 23, 18), 95))
chd=f.mf6.ModflowGwfchd(gwf, stress_period_data=chdd)