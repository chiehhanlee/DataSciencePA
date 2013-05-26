import sys
import MapReduce 

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(entry):
    m_id=entry[0]
    m_row=entry[1]
    m_col=entry[2]
    m_val=entry[3]

    if(m_id=='a'):
        mr.emit_intermediate((m_row,0),entry)
        mr.emit_intermediate((m_row,1),entry)
        mr.emit_intermediate((m_row,2),entry)
        mr.emit_intermediate((m_row,3),entry)
        mr.emit_intermediate((m_row,4),entry)
    else:
        mr.emit_intermediate((0,m_col),entry)
        mr.emit_intermediate((1,m_col),entry)
        mr.emit_intermediate((2,m_col),entry)
        mr.emit_intermediate((3,m_col),entry)
        mr.emit_intermediate((4,m_col),entry)

# Part 3
def reducer(key, entries):
    val = 0
    for itm in entries:
        if itm[0]=='a':
            for col in entries:
                if col[0]=='b' and itm[2]==col[1]:
                    val += itm[3]*col[3]
    if val!= 0:
        mr.emit((key[0],key[1],val))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
