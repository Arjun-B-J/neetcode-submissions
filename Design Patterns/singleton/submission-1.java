static class Singleton {
    private static volatile Singleton uniqueinstance = null;
    private String value = null;
    private Singleton() {
        this.value = null;
    }

    public static Singleton getInstance() {
        if( uniqueinstance == null ){
            synchronized(Singleton.class) {
                if (uniqueinstance == null){
                    uniqueinstance = new Singleton();
                }
            }
        }
        return uniqueinstance;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    
}
