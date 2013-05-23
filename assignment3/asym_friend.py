import sys
import MapReduce 

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    a = record[0]
    b = record[1]
    mr.emit_intermediate(a,(b,True))
    mr.emit_intermediate(b,(a,False))

# Part 3
def reducer(key, relations):
    frs = set()
    bfrs = set()
    for r in relations:
        if r[1] == True:
            frs.add(r[0])
        else:
            bfrs.add(r[0])
    for fr in frs:
        if not fr in bfrs:
            mr.emit((key,fr))
    for fr in bfrs:
        if not fr in frs:
            mr.emit((key,fr))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
