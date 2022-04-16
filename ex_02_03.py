xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
xp = float(xh) * float(xr)
print("Pay:",xp)


hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
gp = float(h * r)
if h <= 40:
    gp = float(h * r)
else:
    gp = float(40 * r + (h-40) * (1.5 * r))

print(gp)
