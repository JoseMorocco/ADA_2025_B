public class ProblemaDeEficiencia {

    public int sumaConBucle(int n) {
        int suma = 0;
        for (int i = 1; i <= n; i++) {
            suma += i;
        }
        return suma;
    }

    public int sumaConFormula(int n) {
        return n * (n + 1) / 2;
    }
}
