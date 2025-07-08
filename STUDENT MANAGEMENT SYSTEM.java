import java.util.ArrayList;
import java.util.Scanner;

// Student class
class Student {
    String name;
    int rollNumber;
    String grade;

    public Student(String name, int rollNumber, String grade) {
        this.name = name;
        this.rollNumber = rollNumber;
        this.grade = grade;
    }

    public void display() {
        System.out.println("Name: " + name + ", Roll No: " + rollNumber + ", Grade: " + grade);
    }
}

// StudentManagementSystem class
class StudentManagementSystem {
    ArrayList<Student> students = new ArrayList<>();
    Scanner sc = new Scanner(System.in);

    public void addStudent() {
        System.out.print("Enter Name: ");
        String name = sc.nextLine();
        System.out.print("Enter Roll Number: ");
        int roll = sc.nextInt();
        sc.nextLine(); // Consume newline
        System.out.print("Enter Grade: ");
        String grade = sc.nextLine();

        students.add(new Student(name, roll, grade));
        System.out.println(" Student added successfully.");
    }

    public void removeStudent() {
        System.out.print("Enter Roll Number to remove: ");
        int roll = sc.nextInt();
        sc.nextLine(); // Consume newline
        boolean found = false;

        for (Student s : students) {
            if (s.rollNumber == roll) {
                students.remove(s);
                System.out.println(" Student removed.");
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println(" Student not found.");
        }
    }

    public void searchStudent() {
        System.out.print("Enter Roll Number to search: ");
        int roll = sc.nextInt();
        sc.nextLine(); // Consume newline
        boolean found = false;

        for (Student s : students) {
            if (s.rollNumber == roll) {
                System.out.println(" Student Found:");
                s.display();
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println(" Student not found.");
        }
    }

    public void displayAllStudents() {
        if (students.isEmpty()) {
            System.out.println("No students in the system.");
        } else {
            System.out.println("\n--- All Students ---");
            for (Student s : students) {
                s.display();
            }
        }
    }
}

// Main class
public class StudentManagementApp {
    public static void main(String[] args) {
        StudentManagementSystem sms = new StudentManagementSystem();
        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\n=== Student Management System ===");
            System.out.println("1. Add Student");
            System.out.println("2. Remove Student");
            System.out.println("3. Search Student");
            System.out.println("4. Display All Students");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    sms.addStudent();
                    break;
                case 2:
                    sms.removeStudent();
                    break;
                case 3:
                    sms.searchStudent();
                    break;
                case 4:
                    sms.displayAllStudents();
                    break;
                case 5:
                    System.out.println(" Exiting Student Management System.");
                    break;
                default:
                    System.out.println(" Invalid choice. Try again.");
            }
        } while (choice != 5);
    }
}
