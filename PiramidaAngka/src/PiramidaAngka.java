import java.util.Scanner;

public class PiramidaAngka {
    public static void main(String[] args) {
        // Membaca tinggi piramida dari pengguna
        Scanner scanner = new Scanner(System.in);
        System.out.print("Masukkan tinggi piramida: ");
        int tinggi = scanner.nextInt();

        // Loop untuk mengatur baris pada piramida
        for (int i = 1; i <= tinggi; i++) {
            // Loop untuk menampilkan angka pada setiap baris
            for (int j = 1; j <= i; j++) {
                System.out.print(j + " ");
            }

            // Pindah ke baris berikutnya setelah satu baris selesai
            System.out.println();
        }

        // Menutup scanner
        scanner.close();
    }
}
