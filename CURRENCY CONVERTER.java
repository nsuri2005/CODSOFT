import java.util.Scanner;

public class CurrencyConverter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] currencies = {"USD", "INR", "EUR", "JPY"};
        double[][] rates = {
            // USD,   INR,    EUR,    JPY
            {1.0,   83.2,   0.91,  153.5},
            {0.012, 1.0,   0.011,  1.85},
            {1.10, 91.2,   1.0,   169.1},  
            {0.0065, 0.54, 0.0059, 1.0}   
        };

        System.out.println("Available Currencies:");
        for (int i = 0; i < currencies.length; i++) {
            System.out.println((i + 1) + ". " + currencies[i]);
        }

        System.out.print("Choose base currency (1-4): ");
        int baseIndex = sc.nextInt() - 1;

        System.out.print("Choose target currency (1-4): ");
        int targetIndex = sc.nextInt() - 1;

        System.out.print("Enter amount in " + currencies[baseIndex] + ": ");
        double amount = sc.nextDouble();

        double converted = amount * rates[baseIndex][targetIndex];
        System.out.println("Converted Amount: " + currencies[targetIndex] + " " + converted);
    }
}
