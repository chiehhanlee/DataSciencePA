import sys
import MapReduce 

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    a = record[0]
    b = record[1]
    mr.emit_intermediate(a,1)

# Part 3
def reducer(key, counts):
    total=0
    for c in counts:
        total +=c
    mr.emit((key,total))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
