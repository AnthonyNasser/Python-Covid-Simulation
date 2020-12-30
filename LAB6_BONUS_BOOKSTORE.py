import Book
import SortableBook
import ArrayList
import ArrayQueue
import RandomQueue
import MaxQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
import AdjacencyList
import time
from algorithms import *
import pdb


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart.
    '''

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = ArrayQueue.ArrayQueue()
        self.bookSortedCatalog = DLList.DLList()
        self.bestSellers = BinaryHeap.BinaryHeap()
        self.indexSortedTitle = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key,
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookSortedCatalog = DLList.DLList()
        with open(fileName, encoding='utf-8') as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = SortableBook.SortableBook(key, title, group, rank, similar)
                self.bookSortedCatalog.append(s)
            # The following line is used to calculate the total time
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookSortedCatalog.size()} books in {elapsed_time} seconds")

    def merge_sort_catalog(self):
        temp = []  # create a temp array that can be passed into merge function
        # add everything in bookSortedCatalog into temp
        for i in range(self.bookSortedCatalog.size()):
            temp.append(self.bookSortedCatalog.get(i).title)
        # merge sort temp
        merge_sort(temp)
        return temp

    def quick_sort_catalog(self):
        temp = []  # create a temp array that can be passed into quick_sort function
        # add everything in bookSortedCatalog into temp
        for i in range(self.bookSortedCatalog.size()):
            temp.append(self.bookSortedCatalog.get(i).title)
        # merge sort temp
        quick_sort(temp)
        return temp

    def binarySearchByTitle(self, prefix: str):
        # store indexes of self.bookSortedCatalog
        indexes = {}
        if prefix == '':
            print("None found")
            return None
        sorted_catalog = self.quick_sort_catalog()
        for i in range(len(sorted_catalog)):
            indexes[i] = sorted_catalog[i]
        search = binary_search(sorted_catalog, prefix)
        if search is not None:
            for i in range(len(sorted_catalog)):
                if search is not None and (indexes[i] in sorted_catalog[search]):
                    print(f'{i} : {sorted_catalog[search]}')
                    sorted_catalog.remove(sorted_catalog[search])
                    search = binary_search(sorted_catalog, prefix)
        else:
            print(f"{prefix} was not found in the catalog.")


    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input:
            i: positive integer
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i
        input:
            i: positive integer
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str):
        '''
        searchBookByInfix: Search all the books that contains infix
        input:
            infix: A string
        '''
        books = []
        indexes = []
        start_time = time.time()
        # Loop through all elements in the book catalog
        sizeOfCatalog = self.bookCatalog.size()
        for i in range(sizeOfCatalog):
            # for the ones that start with the given string, add them to the books array
            if (infix in self.bookCatalog.get(i).title):
                books.append(self.bookCatalog.get(i))
                indexes.append(i)
        # # using the books array, get the title and index of every book that was given
        # for i in range(len(books)-1):
        #     print(f"'{books[i].title}' is at index {indexes[i]}")

        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")
        return books

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shopping cart
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")