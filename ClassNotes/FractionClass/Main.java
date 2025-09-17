// Victoria Heredia
// Fraction Class
import java.util.*;

class Frac {
    private int num;
    private int den;

    // default constructor
    public Frac() {
        this.num = 1;
        this.den = 1;
    }

    // parameter constructor
    public Frac(int num1, int den1) {
        this.num = num1;
        this.den = den1;
    }

    // setters
    public void setNum(int num2) {
        this.num = num2;
    }

    public void setDen(int den2) {
        this.den = den2;
    }

    // getters
    public int getNum() {
        return this.num;
    }

    public int getDen() {
        return this.den;
    }

    // multiplication
    public Frac multiply(Frac f) {
        Frac temp = new Frac();
        temp.num = this.num * f.num;
        temp.den = this.den * f.den;
        return temp;
    }

    //addition
    public Frac add(Frac f){
        Frac temp = new Frac();
        temp.num = (this.num * f.den) + (f.num * this.den);
        temp.den = this.den * f.den;
        return temp;
    }

    //division
    public Frac divide(Frac f){
        Frac temp = new Frac();
        temp.num = this.num * f.den;
        temp.den = this.den * f.num;
        return temp;
    }

    // print fraction
    public void print() {
        System.out.println(this.num + " / " + this.den);
    }
}

public class Main {
    public static void main(String[] args) {
        Frac f1 = new Frac();
        Frac f2 = new Frac(2, 3);
        Frac f3 = new Frac(3, 4);

        f1.print(); // prints 1/1
        f2.print(); // prints 2/3
        f3.print(); // prints 3/4

        Frac product = f2.multiply(f3);
        product.print(); // prints 6/12

        Frac add = f2.add(f3);
        add.print();

        Frac divide = f2.divide(f3);
        divide.print();
    }
}
