def cel_to_fahr(c):
    if(c < -273.15):
        return "Sorry, the lowest possible temperature that physical matter can reach is -273.15 °C."
    else:
        f = c * 9 / 5 + 32
        return f
temperatures=[10,-20,-289,100]
for item in temperatures:
    print(cel_to_fahr(item))
