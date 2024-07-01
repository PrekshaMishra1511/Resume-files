import Includes.*;

public class PendingRequests {
    private int length = 0; //Number of requests in the linked list.
    private Node<RequestData> front;// Reference to the front of the linked list.
    private Node<RequestData> back;//Reference to the back of the linked list.

    public boolean insert(Node<RequestData> insnode) {//adds request to the end of the list
        if(insnode == null)
        {
            return false;
        }
        else if(front ==null)
        {
            front=insnode;
            back=insnode;
        }
        else{
            Node<RequestData> x=back;
            back=insnode;
            back.previous=x;
        }
        length++;
        return true;
    }

    public boolean delete(Node<RequestData> delnode) {//delets the given request from the linked list
        if(delnode == null)
        {
            return false;
        }
        if(front == null)
        {
            return false;
        }
    
        else{
            Node<RequestData> x = front;
            while(x.data.ISBN!=delnode.data.ISBN && x!=null){
                x=x.next;
            }
            if(x!=null)
            {
                if(x==front)
                {
                    front=x.next;
                    x=null;
                }
                else if(x==back)
                {
                    x.previous.next=null;
                    x=null;
                }
                else{
                    x.previous.next=x.next;
                    x.next.previous=x.previous;
                    x=null;
                }
            }

        }
        return true;
    }

    public Node<RequestData> find(int ISBN) {//returns the first node with the given ISBN
        Node<RequestData> nrd = null;
        nrd=front;
        while(nrd!=null && nrd.data.ISBN != ISBN)
        {
            nrd=nrd.next;
        }
        return nrd;
    }

    public String toString(){
        Node<RequestData> temp = front;
        String s = "Length: " + length + "\n";
        while(temp != null){
            s+=temp.data.toString();
            temp = temp.next;
        }
        return s;
    }
}
