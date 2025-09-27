public class ProblemaNumerico {

    public int mcdEuclides(int a, int b){
        if (b == 0) {
            return a;
        }
        return mcdEuclides(b, a % b);
    }

    public int mcdBucles(int a, int b) {
        int mcd = 1;
        int limite = Math.min(a, b);
        for (int i = 1; i <= limite; i++) {
            if (a % i == 0 && b % i == 0) {
                mcd = i;
            }
        }
        return mcd;
    }

    public static void main(String[] args){
        int a=18;
        int b=48;
        ProblemaNumerico problema=new ProblemaNumerico();


        // Medición del tiempo para el método de Euclides
        long comienzoEuclides = System.nanoTime();
        int Euclides=problema.mcdEuclides(a,b);
        long finalEuclides = System.nanoTime();
        long duracionEuclides = comienzoEuclides - finalEuclides;

        // Medición del tiempo para el método de Bucles
        long ComienzoBucles = System.nanoTime();
        int Bucles=problema.mcdBucles(a,b);
        long finalBucles = System.nanoTime();
        long duracionBucles = ComienzoBucles - finalBucles;

        System.out.println("MCD de "+a+" y "+b);

        System.out.println("MCD Euclides: "+Euclides);
        System.out.println("Tiempo de ejecución del método de Euclides: " + duracionEuclides + " nanosegundos");

        System.out.println("MCD Bucles: "+Bucles);
        System.out.println("Tiempo de ejecución del método de Bucles: " + duracionBucles + " nanosegundos");

    }   

}