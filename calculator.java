import java.util.Scanner;
public class calculator{
    public static void main(String[] args){
        
        Scanner userInput = new Scanner(System.in);

        System.out.println("What would you like to do today? (1) Add, (2) Subtract, (3) Multiply, (4) Divide");
        System.out.println(("Please enter the number that corrosponds: "));
        int calcMethod = userInput.nextInt();
        float firstNum;
        float secondNum;

        switch(calcMethod){
            case 1:
                System.out.println("Enter first # to add: ");
                firstNum = userInput.nextFloat();
                System.out.println("Enter second # to add: ");
                secondNum = userInput.nextFloat();
                System.out.println("Your results are: " + (firstNum + secondNum));
                break;
            case 2:
                System.out.println("Enter first # to subtract: ");
                firstNum = userInput.nextFloat();
                System.out.println("Enter second # to subtract: ");
                secondNum = userInput.nextFloat();
                System.out.println("Your results are: " + (firstNum - secondNum));
                break;
            case 3:
                System.out.println("Enter first # to multiply: ");
                firstNum = userInput.nextFloat();
                System.out.println("Enter second # to multiply: ");
                secondNum = userInput.nextFloat();
                System.out.println("Your results are: " + (firstNum * secondNum));
                break;
            case 4:
                System.out.println("Enter first # to divide: ");
                firstNum = userInput.nextFloat();
                System.out.println("Enter second # to divide: ");
                secondNum = userInput.nextFloat();
                System.out.println("Your results are: " + (firstNum / secondNum));
                break;
        }   
    }
}