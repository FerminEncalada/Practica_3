from controls.tda.linked.node import Node
from controls.exception.arrayPositionException import ArrayPositionException
from controls.exception.linkedEmpty import LinkedEmpty
from numbers import Number
from controls.tda.linked.burbuja import Burbuja
from controls.tda.linked.insercion import Insercion
from controls.tda.linked.merge import MergeSort
from controls.tda.linked.quick import QuickSort 
from controls.tda.linked.shell import ShellSort 
from controls.tda.linked.tdaArray import TDAArray

class Linked_List(object):
    def __init__(self):
        self.__head = None  
        self.__last = None
        self.__lenght = 0

    @property
    def _lenght(self):
        return self.__lenght

    @_lenght.setter
    def _lenght(self, value):
        self.__lenght = value
        
        
    def is_empty(self):
        return self.__head is None 
    
    def size(self):
        current = self.__head
        count = 0
        while current:
            count += 1
            current = current._next
        return count
    
    
    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node  
            self.__last = node
            self.__lenght += 1
        else:
            headOld = self.__head  
            node = Node(data, headOld)
            self.__head = node  
            self.__lenght += 1
            
            
    def __addLast__(self, data):
        if self.isEmpty:
           self.__addFirst__(data)
        else:
            node = Node(data)
            self.__last._next = node
            self.__last = node
            self.__lenght += 1

    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__lenght = 0


    def getNode(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._lenght:
            print ("FUERA DE RANGO")
        elif pos == 0:
            return self.__head
        elif pos == (self.__lenght - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
        
        
    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__lenght:
            self.__addLast__(data)
        else:
            node_preview = self.getNode(pos - 1)
            node_last = node_preview._next #self.getNode(pos)
            node = Node(data, node_last)
            node_preview._next = node
            self.__lenght += 1
    
    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data 
        elif pos == self.__lenght:
            self.__last._data = data
        else:
            node = self.getNode(pos)  
            node._data = data

    def delete(self, pos = 0):
        if pos == 0:
            self._head = self.head._next if self._head else None
            self._last = None if self.head is None else self._last
        else:
            node = self.__head
            for _ in range(pos - 1):
                if node:
                    node = node._next
            if node and node._next:
                node._next = node._next._next
            if pos == self.__lenght - 1:
                self.__last = node
        self.__lenght -= 1
    
        
    def get(self, pos):
        
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._lenght:
            print ("FUERA DE RANGO")
        elif pos == 0:
            return self.__head._data
        elif pos == (self.__lenght - 1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node._data
    
    @property
    def print(self):
        node = self.__head
        data = ""
        while node != None:
            data += str(node._data)+"    "
            node = node._next
        print("Lista de datos")
        print(data)

    @property
    def isEmpty(self):
        return self.__head == None or self.__lenght == 0  
    
    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            return "List is Empty"
        else:
            node = self.__head 
            while node != None:
                out += str(node._data) + "\t"
                node = node._next          
        return out
    
    # #Pasar la lista a arreglo
    # @property
    # def toArray(self):
    #     array = []
    #     if not self.isEmpty:
    #         node = self.__head
    #         cont = 0
    #         while cont < self._lenght:
    #             array.append(node._data)
    #             cont += 1
    #             node = node._next

    #     return array
    
    #Pasar la lista a arreglo
    @property
    def toArray(self):
        array = TDAArray(self._lenght)
        if not self.isEmpty:
            node = self.__head
            cont = 0 
            while cont < self._lenght:
                array.insert(node._data, cont)
                cont += 1
                node = node._next
        return array
                

    def toList(self, array):
        self.clear
        for i in range(0, len(array)):
            self.__addLast__(array[i])

    def sort(self, sort_method="merge", type=1):
        if self.isEmpty:
            raise LinkedEmpty("Lista vacía")
        else:
            array = self.toArray

            if isinstance(array[0], (Number, str)):  
                if sort_method == "quick":
                    order = QuickSort()
                elif sort_method == "shell":
                    order = ShellSort()
                else:  # Por defecto usa MergeSort
                    order = MergeSort()
                
                if type == 1: #Menor a mayor
                    array = order.sort_primitive_ascendent(array)
                else:  # Mayor a menor
                    array = order.sort_primitive_descendent(array)
            
            self.toList(array)
            return self

    def sort_models(self, sort_method="merge", attribute=None, type=1):
        if self.isEmpty:
            raise LinkedEmpty("Lista vacía")
        else:
            array = self.toArray

            if isinstance(array[0], object): 
                if sort_method == "quick":
                    order = QuickSort()
                elif sort_method == "shell":
                    order = ShellSort()
                else:  # Por defecto usa MergeSort
                    order = MergeSort()

                if type == 1:  # Menor a mayor
                    array = order.sort_models_ascendent(array, attribute)
                else:  # Mayor a
                    array = order.sort_models_descendent(array, attribute)
                
            self.toList(array)
            return self

    def search_equals(self, data):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            #print(array[i])
            for i in range(0, len(array)):
                #print(type(array[i]))
                if(array[i].lower().__contains__ (data.lower())):    #startswith
                    list.add(array[i], list._lenght)
        return list

##############################################################
            #En caso de los datos numéricos 
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def generate_random_array(size):
    return [random.randint(1, 1000000) for _ in range(size)]
    