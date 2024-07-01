import java.util.*;
import Includes.*;
public class LibraryStorage {
    // HashMap
    // process return
    private HashMap<Integer, BookData> storage; //Map of ISBN and Bookdata for all the books in the library
    private RequestQueue rqQueue;//the queue of requests
    private PendingRequests prLinkedList;//the linkedlist of pending requests

    public LibraryStorage() {//constructor
        storage = new HashMap<Integer, BookData>();
        for (int i=100001; i<100011; i++) {
            BookData book = new BookData();
            MyDate dateor = new MyDate();
            dateor.month = 0;
            dateor.year = 0;
            book.BorrowedStatus = false;
            book.BorrowedByUserID = 0;
            book.ISBN = i;
            book.Publisher = "publisher";
            book.Author = "author";
            book.DateOfReturn = dateor;
            storage.put(i, book);
        }

        rqQueue = new RequestQueue();
        prLinkedList = new PendingRequests();
    }

    public void push(int ISBN, int UserID) {//calls push for queue of requests
        rqQueue.push(ISBN, UserID);
        return;
    }

    public boolean processQueue() {/*Processes the request at the front of the
        queue by checking if the book is available in the library (returns true) or
        adding request to pending requests if required (returns false). Updates
        storage and book details accordingly. */
        RequestData ra = rqQueue.getFront();
        if(ra==null)
        {
            return false;
        }
        if(storage.containsKey(ra.ISBN))
        {
            BookData request = storage.get(ra.ISBN);
            if(!request.BorrowedStatus)
            {
                request.BorrowedStatus=true;
                request.BorrowedByUserID=ra.UserID;
                rqQueue.pop();
                return true;
            }
            else
            {
                Node<RequestData> x= new Node<RequestData>();
                x.data = ra;
                prLinkedList.insert(x);
                rqQueue.pop();
                return false;
            }
        }
        else{
            rqQueue.pop();
            return false;
        }
    }

    public boolean processReturn(BookData book) {  /*Checks if the returned
        book has been requested in pending requests and updates the storage and
        book details accordingly. */        // I have assumed this takes BookData object as argument, can also work with ISBN perhaps
        /*
         * Your code here.
         */
        Node<RequestData> req = prLinkedList.find(book.ISBN);
        if(req!=null)
        {
            book.BorrowedStatus=true;
            book.BorrowedByUserID=req.data.UserID;
            prLinkedList.delete(req);
            return true;
        }
        else
        {
            book.BorrowedStatus=false;
            book.BorrowedByUserID=-1;
            storage.put(book.ISBN, book);
            return false;
        }
    }

    public String rqQueueToString(){//: Returns rqQueue’s toString().
        return rqQueue.toString();
    }

    public String prLinkedListToString(){//Returns prLinkedList’s toString().
        return prLinkedList.toString();
    }
}