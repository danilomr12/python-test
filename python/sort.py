from ast import arg
import functools


class Sort():
    """_summary_
    Sort class is a base class for sorting algorithm
    """
    def __init__(self, arr: list, debug = True):
        """
        Sort object constructor
        :param arr: list of numbers, must be numbers
        :param debug: boolean for printing or not traces of the operations
        """
        self.arr = arr
        self.ordered_array = []
        self.debug = debug
    
    def log(func):
        @functools.wraps(func)
        def wrapper_do_twice(*args, **kwargs):
            value = func(*args, **kwargs)
            print(f"array is  {args[0].arr}")
            return value
        return wrapper_do_twice
    
    def debug(func):
        """Print the function signature and return value"""
        @functools.wraps(func)
        def wrapper_debug(*args, **kwargs):
            args_repr = [repr(a) for a in args]                      # 1
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
            signature = ", ".join(args_repr + kwargs_repr)           # 3
            print(f"Calling {func.__name__}({signature})")
            value = func(*args, **kwargs)
            print(f"{func.__name__!r} returned {value!r}")           # 4
            return value
        return wrapper_debug    
    
    @log
    def swap_items(self, j):
        """_summary_
        swaps item from index j with item from index j+1
        
        Args:
            j (int): index of an item in the internal arr list 
        """
        self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
 
    
class BubbleSort(Sort):
  
    def sort(self):
        last_arr_index = len(self.arr)-1
        for i in range(last_arr_index, -1, -1):
            #self.log("first loop")
            for j in range(0, i):
                if(self.arr[j] > self.arr[j+1]):
                    self.swap_items(j)
                    #self.log("i is " + str(i))
                    #self.log(self.arr)


        
arr = [76,55,45,34,6,2]
print(arr)
b= BubbleSort(arr, True)
b.sort()
print(b.arr)
