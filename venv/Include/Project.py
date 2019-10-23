import time
from threading import Thread


def read_from_file(file_name):
    for i in range(1,1000,100):
        min_num=i
        max_num=i+100-1
        my_list=list()
        with open(file_name) as f:
            reader=f.readline()
            while reader is not None and len(reader)!=0:
                reader_int=int(reader)
                if min_num<=reader_int<=max_num:
                    my_list.append(reader_int)
                reader=f.readline()
        yield my_list


def write_to_file(elements,alg_name):
    direct=alg_name+".txt"
    with open(direct,mode="a") as f:
        for i in elements:
            f.write(str(i)+"\n")


def bubble_sort(elements):
    for i in range(0,len(elements)):
        for j in range(0,len(elements)-i-1):
            try:
                if not(elements[j]<elements[j+1]):
                    elements[j] , elements[j+1] = elements[j+1] , elements[j]
            except:
                continue
    write_to_file(elements,"Bubble_Sort")


def iterate_and_bubble_sort():
    global init_time
    for elements in read_from_file("Random.txt"):
        bubble_sort(elements)
    with open("duration.txt",mode="a") as f:
        final_time=time.perf_counter()
        duration=final_time-init_time
        f.write("Algorithm <Bubble_Sort> took "+str(duration)+" seconds to finish\n")


def main():
    global init_time
    init_time=time.perf_counter()
    t1=Thread(target=iterate_and_bubble_sort)
    t1.start()


if __name__ == '__main__':
    main()