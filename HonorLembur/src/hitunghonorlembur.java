import java.util.Scanner;

public class hitunghonorlembur {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 3; i++) {
            System.out.println("Percobaan " + (i + 1));
            System.out.print("Apakah karyawan tetap? (ya/tidak): ");
            String jenisKaryawan = scanner.nextLine();

            System.out.print("Masukkan jam lembur: ");
            int jamLembur = scanner.nextInt();
            scanner.nextLine(); // Mengonsumsi newline agar tidak terjadi masalah pada input berikutnya

            int gajiLembur = hitungHonorLembur(jenisKaryawan, jamLembur);

            if (gajiLembur > 0) {
                System.out.println("Gaji lembur: Rp. " + gajiLembur);
            } else {
                System.out.println("Input tidak valid");
            }

            System.out.println(); // Tambahkan baris kosong untuk pemisah antar percobaan
        }

        scanner.close();
    }

    private static int hitungHonorLembur(String jenisKaryawan, int jamLembur) {
        int gajiLembur = 0;

        if (jenisKaryawan.equalsIgnoreCase("ya")) {
            if (jamLembur >= 12) {
                gajiLembur = 200000;
            } else if (jamLembur >= 8) {
                gajiLembur = 100000;
            }
        } else if (jenisKaryawan.equalsIgnoreCase("tidak")) {
            if (jamLembur >= 8) {
                gajiLembur = 75000;
            }
        }

        return gajiLembur;
    }
}