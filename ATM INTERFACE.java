import java.util.Scanner;

class BankAccount {
    double balance = 0;

    void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited: ₹" + amount);
    }

    void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: ₹" + amount);
        } else {
            System.out.println("Insufficient balance");
        }
    }

    void checkBalance() {
        System.out.println("Balance: ₹" + balance);
    }
}

public class ATMSimple {
    public static void main(String[] args) {
        BankAccount account = new BankAccount();
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit");
            int choice = sc.nextInt();

            if (choice == 1) {
                account.checkBalance();
            } else if (choice == 2) {
                System.out.print("Enter deposit amount: ");
                account.deposit(sc.nextDouble());
            } else if (choice == 3) {
                System.out.print("Enter withdrawal amount: ");
                account.withdraw(sc.nextDouble());
            } else if (choice == 4) {
                System.out.println("Thank you");
                break;
            } else {
                System.out.println("Invalid choice");
            }
        }
    }
}
