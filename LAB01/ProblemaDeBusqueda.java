import java.util.Arrays;

public class ProblemaDeBusqueda {

    // Búsqueda de palabra en texto (búsqueda simple)
    public boolean buscarPalabraEnTexto(String texto, String palabra) {
        if (palabra == null || palabra.isEmpty()) return false;
        int n = texto.length();
        int m = palabra.length();

        for (int i = 0; i <= n - m; i++) {
            int j = 0;
            while (j < m && texto.charAt(i + j) == palabra.charAt(j)) {
                j++;
            }
            if (j == m) {
                return true; 
            }
        }
        return false;
    }

    // Búsqueda de palabra en lista ordenada (búsqueda binaria)
    public boolean buscarPalabraEnListaOrdenada(String[] lista, String palabra) {
        int izquierda = 0, derecha = lista.length - 1;
        while (izquierda <= derecha) {
            int medio = (izquierda + derecha) / 2;
            int cmp = lista[medio].compareTo(palabra);
            if (cmp == 0) return true;
            if (cmp < 0) izquierda = medio + 1;
            else derecha = medio - 1;
        }
        return false;
    }

    public static void main(String[] args) {
        ProblemaDeBusqueda pb = new ProblemaDeBusqueda();
        String texto = "Este es un ejemplo de búsqueda en un texto";
        String palabra = "ejemplo";

        System.out.println("¿La palabra '" + palabra + "' está en el texto? " +
                pb.buscarPalabraEnTexto(texto, palabra));

        String[] lista = {"algoritmo", "busqueda", "ejemplo", "palabra", "texto"};
        Arrays.sort(lista); // lista debe estar ordenada
        System.out.println("¿La palabra '" + palabra + "' está en la lista ordenada? " +
                pb.buscarPalabraEnListaOrdenada(lista, palabra));
    }
}
