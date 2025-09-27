import java.util.Arrays;

public class ProblemaDeClasificacion {

    public void ordenarNombresStandard(String[] nombres) {
        Arrays.sort(nombres);
    }

    public void ordenarNombresSelectionSort(String[] nombres) {
        int n = nombres.length;
        for (int i = 0; i < n - 1; i++) {
            int min_idx = i;
            for (int j = i + 1; j < n; j++) {
                if (nombres[j].compareTo(nombres[min_idx]) < 0) {
                    min_idx = j;
                }
            }
            String temp = nombres[min_idx];
            nombres[min_idx] = nombres[i];
            nombres[i] = temp;
        }
    }

    public static void main(String[] args) {
        ProblemaDeClasificacion problema = new ProblemaDeClasificacion();

        String[] nombresStandard = {"Carlos", "Ana", "David", "Beatriz", "Eva"};
        String[] nombresSelection = {"Carlos", "Ana", "David", "Beatriz", "Eva"};
        
        System.out.println("Lista de nombres original: " + Arrays.toString(nombresStandard));

        long inicioStandard = System.nanoTime();
        problema.ordenarNombresStandard(nombresStandard);
        long finStandard = System.nanoTime();
        long duracionStandard = finStandard - inicioStandard;

        System.out.println("\nLista ordenada con Arrays.sort(): " + Arrays.toString(nombresStandard));
        System.out.println("Tiempo de ejecución (Arrays.sort()): " + duracionStandard + " nanosegundos");

        long inicioSelection = System.nanoTime();
        problema.ordenarNombresSelectionSort(nombresSelection);
        long finSelection = System.nanoTime();
        long duracionSelection = finSelection - inicioSelection;
        
        System.out.println("\nLista ordenada con Selection Sort: " + Arrays.toString(nombresSelection));
        System.out.println("Tiempo de ejecución (Selection Sort): " + duracionSelection + " nanosegundos");
    }
}