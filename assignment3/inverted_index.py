import sys
import MapReduce 

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    doc= record[0]
    text = record[1]
    words = text.split()
    for w in words:
      mr.emit_intermediate(w, doc)

# Part 3
def reducer(w, docs):
    ds = list(set(docs))
    mr.emit((w, ds))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
