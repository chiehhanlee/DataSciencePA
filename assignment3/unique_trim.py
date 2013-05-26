import sys
import MapReduce 

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    seq_id = record[0]
    nucleo =  record[1]
    nucleo = nucleo[:-10]
    mr.emit_intermediate(nucleo,1)

# Part 3
def reducer(key, relations):
    mr.emit(key)

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
