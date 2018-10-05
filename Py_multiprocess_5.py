import multiprocessing as mp
value1 = mp.Value('i',0)
value2 = mp.Value('d',3.14)

array = mp.Array('i', [1,2,3,4])

