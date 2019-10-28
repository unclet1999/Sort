import time
from threading import Thread


#**********************************************READ_FROM_FILE***********************************************************


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


#**********************************************WRITE_TO_FILE************************************************************


def write_to_file(elements,alg_name):
    direct=alg_name+".txt"
    with open(direct,mode="a") as f:
        for i in elements:
            f.write(str(i)+"\n")


#______________________________________________shellSort


def shellSort(elements):
    n = len(elements)
    gap = n//2

    while gap > 0:
        for i in range(gap,n):
            temp = elements[i]
            j = i
            while  j >= gap and elements[j-gap] >temp:
                elements[j] = elements[j-gap]
                j -= gap
            elements[j] = temp
        gap //= 2

    write_to_file(elements, "shellSort")


#**************************************************BUBBLE_SORT**********************************************************


def bubble_sort(elements):
    for i in range(0,len(elements)):
        for j in range(0,len(elements)-i-1):
            try:
                if not(elements[j]<elements[j+1]):
                    elements[j] , elements[j+1] = elements[j+1] , elements[j]
            except:
                continue
    write_to_file(elements,"Bubble_Sort")


#*************************************************SELECTION_SORT********************************************************


def selection_sort(elements):
    for i in range(0, len(elements)):
        min_index = i
        for j in range(i + 1, len(elements)):
            if elements[min_index] > elements[j]:
                min_index = j

        elements[i], elements[min_index] = elements[min_index], elements[i]
    write_to_file(elements, "Selection_Sort")


#**************************************************MERGE_SORT***********************************************************


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


#********************************************Function_related to comb_sort**********************************************


def getNextGap(gap):
    # Shrink gap by Shrink factor
    gap = (gap * 10) / 13
    if gap < 1:
        return 1
    return gap


#**************************************************COMB_SORT************************************************************


def comb_sort(elements):
    n = len(elements)

    # Initialize gap
    gap = n

    # Initialize swapped as true to make sure that
    # loop runs
    swapped = True

    # Keep running while gap is more than 1 and last
    # iteration caused a swap
    while gap != 1 or swapped == 1:

        # Find next gap
        gap = int(getNextGap(gap))

        # Initialize swapped as false so that we can
        # check if swap happened or not
        swapped = False

        # Compare all elements with current gap
        for i in range(0, n - gap):
            if elements[i] > elements[i + gap]:
                elements[i], elements[i + gap] = elements[i + gap], elements[i]
                swapped = True
    write_to_file(elements, "Comb_sort")


#______________________________________________iterateAndShellSort


def iterateAndShellSort():
    global init_time

    for elements in read_from_file("random.txt"):
        shellSort(elements)

    with open("duration.txt",mode="a") as f:
        final_time=time.perf_counter()
        duration=final_time-init_time
        f.write("Algorithm <shellSort> took "+str(duration)+" seconds to finish\n")


#***********************************************ITERATE_AND_BUBBLE_SORT*************************************************


def iterate_and_bubble_sort():
    global init_time
    for elements in read_from_file("Random.txt"):
        bubble_sort(elements)
    with open("duration.txt",mode="a") as f:
        final_time=time.perf_counter()
        duration=final_time-init_time
        f.write("Algorithm <Bubble_Sort> took "+str(duration)+" seconds to finish\n")


#**********************************************ITERATE_AND_MERGE********************************************************


def iterate_and_merge_sort():
    global init_time
    for elements in read_from_file("Random.txt"):
        merge_sort(elements)
        write_to_file(elements,"Merge_Sort")
    with open("duration.txt",mode="a") as f:
        final_time = time.perf_counter()
        duration = final_time-init_time
        f.write("Algorithm <Merge_Sort> took "+str(duration)+" seconds to finish\n")


#***********************************************ITERATE_AND_SELECTION_SORT**********************************************


def iterate_and_selection_sort():
    global init_time
    for elements in read_from_file("Random.txt"):
        selection_sort(elements)
    with open("duration.txt",mode="a") as f:
        final_time=time.perf_counter()
        duration=final_time-init_time
        f.write("Algorithm <Selection_Sort> took "+str(duration)+" seconds to finish\n")


#********************************************ITERATE_AND_COMB_SORT******************************************************


def iterate_and_comb_sort():
    global init_time
    for elements in read_from_file("Random.txt"):
        comb_sort(elements)
    with open("duration.txt",mode="a") as f:
        final_time=time.perf_counter()
        duration=final_time-init_time
        f.write("Algorithm <Comb_sort> took "+str(duration)+" seconds to finish\n")


#***************************************************MAIN_FUNCTION*******************************************************


def main():
    global init_time
    init_time=time.perf_counter()

    t1=Thread(target=iterate_and_bubble_sort)
    t1.start()
    
    t2 = Thread(target=iterate_and_selection_sort)
    t2.start()
    
    t3 = Thread(target=iterate_and_merge_sort)
    t3.start()
    
    t4=Thread(target=iterate_and_comb_sort)
    t4.start()
    
    t5 = Thread(target = iterateAndShellSort)
    t5.start()


if __name__ == '__main__':
    main()
