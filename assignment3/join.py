import sys
import MapReduce 

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

# Part 3
def reducer(key, records):
    if(len(records)>1):	
        os = []
        ls = []
        #Find Order
        for r in records:
            if r[0]=="order":
                os.append(r)
            else:
                ls.append(r)
        for o in os:
            for i in ls:
                mr.emit(o+i)

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
