interface Observer {
    void notify(String itemName);
}

class Customer implements Observer {
    private String name;
    private int notifications;

    public Customer(String name) {
        this.name = name;
        this.notifications = 0;
    }

    public void notify(String itemName) {
        this.notifications += 1;
    }

    public int countNotifications() {
        return this.notifications;
    }
}

class OnlineStoreItem {
    private String itemName;
    private int stock;
    List<Observer> observers = new ArrayList<>();
    public OnlineStoreItem(String itemName, int stock) {
        this.itemName = itemName;
        this.stock = stock;
    }

    public void subscribe(Observer observer) {
        this.observers.add(observer);
    }

    public void unsubscribe(Observer observer) {
        this.observers.remove(observer);
    }

    public void updateStock(int newStock) {
        if (this.stock==0 && newStock>0){
            for(int i=0;i<observers.size();i+=1){
                observers.get(i).notify(this.itemName);
            }
        }
        this.stock = newStock;
    }
}
