import time
from threading import Thread

#-----------------------------------------------------Sort Class------------------------------------------------------

class Sort(Thread):

    def __init__(self, func, name):
        Thread.__init__(self)
        self.func = func
        self.name = name

    def read_from_file(self):
        for i in range(1, 1000, 100):
            min_num = i
            max_num = i + 100 - 1
            my_list = list()
            with open("Random.txt") as f:
                reader = f.readline()
                while reader is not None and len(reader) != 0:
                    reader_int = int(reader)
                    if min_num <= reader_int <= max_num:
                        my_list.append(reader_int)
                    reader = f.readline()
            yield my_list

    def write_to_file(self, elements, alg_name):
        direct = alg_name + ".txt"
        with open(direct, mode="a") as f:
            for i in elements:
                f.write(str(i) + "\n")

    def iterate_and_sort(self):
        global init_time
        for elements in self.read_from_file():
            self.func(elements)
            self.write_to_file(elements, self.name)
        with open("duration.txt", mode="a") as f:
            final_time = time.perf_counter()
            duration = final_time - init_time
            f.write("Algorithm <" + self.name + "> took " + str(duration) + " seconds to finish\n")

    def run(self):
        self.iterate_and_sort()

#-----------------------------------------------------------Merge Sort--------------------------------------------------

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

#-----------------------------------------------------------Shell Sort--------------------------------------------------

def shell_sort(elements):
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

#-----------------------------------------------------------Bubble Sort-------------------------------------------------

def bubble_sort(elements):
    for i in range(0,len(elements)):
        for j in range(0,len(elements)-i-1):
            try:
                if not(elements[j]<elements[j+1]):
                    elements[j] , elements[j+1] = elements[j+1] , elements[j]
            except:
                continue

#-----------------------------------------------------------Selection Sort----------------------------------------------

def selection_sort(elements):
    for i in range(0, len(elements)):
        min_index = i
        for j in range(i + 1, len(elements)):
            if elements[min_index] > elements[j]:
                min_index = j
        elements[i], elements[min_index] = elements[min_index], elements[i]

#-----------------------------------------------------------Comb Sort-------------------------------------------------

def comb_sort(elements):

    def getNextGap(gap):
        # Shrink gap by Shrink factor
        gap = (gap * 10) / 13
        if gap < 1:
            return 1
        return gap

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

#-----------------------------------------------------------Main--------------------------------------------------------

def main():
    global init_time
    init_time=time.perf_counter()
    t1=Sort(merge_sort,"Merge_Sort")
    t2=Sort(shell_sort,"Shell_Sort")
    t3=Sort(comb_sort,"Comb_Sort")
    t4=Sort(selection_sort,"Selection_Sort")
    t1.start()
    t2.start()
    t3.start()
    t4.start()

if __name__ == '__main__':
    main()