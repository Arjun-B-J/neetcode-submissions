public enum Singleton {
    INSTANCE;
    private String value;
    public static Singleton getInstance() {
        return INSTANCE;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    
}
