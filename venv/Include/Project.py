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


def selection_sort(elements):
    for i in range(0, len(elements)):
        min_index = i
        for j in range(i + 1, len(elements)):
            if elements[min_index] > elements[j]:
                min_index = j

        elements[i], elements[min_index] = elements[min_index], elements[i]
    write_to_file(elements, "Selection_Sort")

def merge_sort(elements):
    if(len(elements)>1):
        mid = len(elements)//2
        L=elements[:mid]
        R=elements[mid:]
        merge_sort(L)
        merge_sort(R)
        i,j,k=0,0,0
        while(i<len(L) and j<len(R)):
            if L[i]<R[j]:
                elements[k]=L[i]
                i+=1
            else:
                elements[k]=R[j]
                j+=1
            k+=1
        while(i<len(L)):
            elements[k] = L[i]
            i+=1
            k+=1
        while(j<len(R)):
            elements[k]=R[j]
            j+=1
            k+=1


def iterate_and_bubble_sort():
    global init_time
    for elements in read_from_file("Random.txt"):
        bubble_sort(elements)
    with open("duration.txt",mode="a") as f:
        final_time=time.perf_counter()
        duration=final_time-init_time
        f.write("Algorithm <Bubble_Sort> took "+str(duration)+" seconds to finish\n")


def iterate_and_merge_sort():
    global init_time
    for elements in read_from_file("Random.txt"):
        merge_sort(elements)
        write_to_file(elements,"Merge_Sort")
    with open("duration.txt",mode="a") as f:
        final_time = time.perf_counter()
        duration = final_time-init_time
        f.write("Algorithm <Merge_Sort> took "+str(duration)+" seconds to finish\n")

def iterate_and_selection_sort():
    global init_time
    for elements in read_from_file("Random.txt"):
        selection_sort(elements)
    with open("duration.txt",mode="a") as f:
        final_time=time.perf_counter()
        duration=final_time-init_time
        f.write("Algorithm <Selection_Sort> took "+str(duration)+" seconds to finish\n")


def main():
    global init_time
    init_time=time.perf_counter()
    t1=Thread(target=iterate_and_bubble_sort)
    t1.start()
    t2 = Thread(target=iterate_and_selection_sort)
    t2.start()
    t3 = Thread(target=iterate_and_merge_sort)
    t3.start()

if __name__ == '__main__':
    main()