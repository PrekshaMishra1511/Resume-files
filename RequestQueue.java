import Includes.*;

public class RequestQueue {
    private Node<RequestData> front; //: Reference to the front of the queue
    private Node<RequestData> back; // Reference to the back of the queue.
    private int length = 0;// Number of requests in the queue.

    public RequestData getFront() {// Returns the front of the queue.
        return this.front.data;
    }

    public int getLength() {// Returns the length of the queue.
        return this.length;
    }

    public void push(int ISBN, int UserID) {//Adds new request to the back of the queue.
        RequestData r=new RequestData();
        r.ISBN=ISBN;
        r.UserID=UserID;
        MyDate m=new MyDate();
        m.month=1;
        m.year=1;
        r.RequestDate=m;
        Node<RequestData> nigga = new Node<RequestData>();
        nigga.data=r;
        if(front==null)
        {
            front=nigga;
            back = nigga;
        }
        else{
            back.next = nigga;
            nigga.previous=back;
            back = nigga;
        }
        length++;
        return;
    }

    public void pop() { //Removes request from the front of the queue.     // processing needs to be done before popping, 
        if(front == null)
        {
            System.out.println("Teri maa ki choot");
            return;
        }
        else{
            if(front==back){
                front=null;
                back=null;
            }
            else{
                Node<RequestData> n= front.next;
                
                n.previous=null;
                front.next=null;
                front= n;
            }
            length--;
            return;
        }
        
    }

    public String toString(){//Returns a string containing length and data in queue.
        Node<RequestData> temp = front;
        String s = "Length: " + length + "\n";
        while(temp != null){
            s+=temp.data.toString();
            temp = temp.next;
        }
        return s;
    }
}
