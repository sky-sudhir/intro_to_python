books=[]

def addBook(book):
    books.append(book)

def searchBook(search):
    searchItem=[]

    for item in books:
        print(item)
        if search in item["book"] or search in item["author"]:
            searchItem.append(item)
    return searchItem


def inventory():
    return len(books)


if __name__ == "__main__":
    addBook({"book":"Python Crash Course","author":"Eric Matthes"})
    addBook({"book":"Automate the Boring Stuff with Python","author":"Al Sweigart"})
    addBook({"book":"The Pragmatic Programmer","author":"Andrew Hunt and David Thomas"})

    print("Total books in inventory:", inventory())
    searchResults = searchBook("Python")
    print("Search results for 'Python':")
    print(searchResults)
    

    
