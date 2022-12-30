def trs(n, source, destination, spare): # A => Source, B => Destination, C => spare
    if n == 1:
        print("Move " + str(n) + " disk directly from " + source + " to " + destination)
    else:
        trs(n-1, source, spare, destination)
        trs(1, source, destination, spare)
        trs(n-1, spare, destination, source)
    
print(trs(3, "A", "B", "C")) # A => Source, B => Destination, C => spare
    