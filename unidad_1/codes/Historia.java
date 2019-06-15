public class Historia {

    static boolean matar(int bicho, int arma){
        if((bicho - arma) <= 0)
            return true;
        return false;
    }

    public static void main(string[] args){
        matar(100, "espada");
    }

}
