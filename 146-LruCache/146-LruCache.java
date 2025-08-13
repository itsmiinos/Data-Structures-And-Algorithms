// Last updated: 8/13/2025, 8:22:06 PM
class LRUCache {

    HashMap<Integer,Node> hm;
    Node h = new Node();
    Node t = new Node();
    int cap;

    public LRUCache(int capacity) {
        this.cap = capacity;
        hm = new HashMap();
        h.next = t;
        t.prev = h;
    }
    
    public int get(int key) {
        if(hm.containsKey(key)==false){
            return -1;
        }
        else{
            int ans = hm.get(key).val;
            Node temp = delete(hm.get(key));
            add(h,t,temp);
            return ans;
        }
    }
    
    public void put(int key, int value) {
        Node res = hm.get(key);
        if(res==null){
            if(hm.size()==cap){
                Node temp = delete(h.next);
                hm.remove(temp.key);
            }
            Node n = new Node();
            n.key = key;
            n.val = value;
            hm.put(key,n);
            add(h,t,n);
        }
        else{
            Node temp = delete(res);
            temp.val = value;
            hm.put(key , temp);
            add(h,t,temp);
        }
    }

    public void add(Node h, Node t,Node n){
        Node temp = t.prev;
        temp.next = n;
        n.next = t;
        t.prev = n;
        n.prev = temp;
    }

    public Node delete(Node n){
        Node dm1 = n.prev;
        Node dp1 = n.next;

        dm1.next = dp1;
        dp1.prev = dm1;

        n.next = null;
        n.prev = null;

        return n;
    }
}

class Node{
    int val;
    Node prev;
    Node next;
    int key;

    void Node(){
       this.prev = null;
       this.next = null;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */