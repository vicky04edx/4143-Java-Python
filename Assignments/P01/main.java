/*****************************************************************************
*                    
*  Author:           Victoria Heredia
*  Email:            vdheredia1128@my.msutexas.edu
*  Label:            P01
*  Title:            Program 1: Quadratic Formula
*  Course:           CMPS 4143 
*  Semester:         Fall 2025
* 
*   Description:
*        This program calculates the roots of a quadratic equation 
*        using the quadratic formula. It handles real and repeated roots,
*        and prints results to two decimal places.          
*****************************************************************************/
import java.util.Scanner;
class main {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Program 1: Quadratic Formula\nVictoria Heredia\nCMPS 4143\nDescription:This program calculates the roots of a quadratic equation using the quadratic formula.\n");
        System.out.println("Enter the coefficients a,b,c (enter 0 0 0 to quit)");

        //Variables
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();

        // Quit condition
        if (a == 0 && b == 0 && c==0)
        {
            System.out.println("Exiting program.");
            System.exit(0); 
        }

        //Check if the value of 'a' is 0 (invalid)
        else if(a==0) 
        {
            System.out.println("Invalid value for 'a', needs to be other than 0");
            System.exit(0); 
        }

        //Discriminant formula
        int resultDiscriminant= ((b * b) - (4 * a * c));

        // No real solutions
        if (resultDiscriminant < 0) 
        {
            System.out.println("There are no real solutions to this equation.");
            System.exit(0);
        }
        
        // One real root (repeated root)
        else if(resultDiscriminant == 0) 
        {
            double x = -b / (2 * a);
            System.out.printf("x = %.2f%n", x);
        }

        // Two distinct real roots
        else
        {
            double x1 = (-b + Math.sqrt(resultDiscriminant)) / (2 * a); //Calculate the quadratic formula for the 1st root 
            double x2 = (-b - Math.sqrt(resultDiscriminant)) / (2 * a); //Calculate the quadratic formula for the 2nd root 
            System.out.printf("x = %.2f or x = %.2f%n",x1,x2);
        }
     
    }
}
