public class ProblemaDeDecision {

    public boolean esPalindromo(int numero) {
        String s = Integer.toString(numero);
        int d = s.length();
        for (int i = 0; i < d / 2; i++) {
            if (s.charAt(i) != s.charAt(d - i - 1)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        ProblemaDeDecision problema = new ProblemaDeDecision();

        // Prueba 1: Un número palíndromo
        int numero1 = 12321;
        System.out.println("¿Es " + numero1 + " un número palíndromo? " + problema.esPalindromo(numero1)); // true

        // Prueba 2: Un número que no es palíndromo
        int numero2 = 12345;
        System.out.println("¿Es " + numero2 + " un número palíndromo? " + problema.esPalindromo(numero2)); // false

        // Prueba 3: Un número palíndromo con un número par de dígitos
        int numero3 = 4554;
        System.out.println("¿Es " + numero3 + " un número palíndromo? " + problema.esPalindromo(numero3)); // true

        // Prueba 4: Un solo dígito
        int numero4 = 7;
        System.out.println("¿Es " + numero4 + " un número palíndromo? " + problema.esPalindromo(numero4)); // true
    }
}