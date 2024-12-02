import java.util.Scanner;

public class FutureDay{
  public static void main(String... args){
    String[] weekDays = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
    
    Scanner scan = new Scanner(System.in);
    
    System.out.print("Enter today's day: ");
    int today = scan.nextInt();    
    
    System.out.print("Enter the number of days elapsed since today: ");
    int daysElapsed = scan.nextInt();
    int futureDay = (today + daysElapsed) % 7;
    
    System.out.printf("Today is %s and the future day is %s %n", weekDays[today], weekDays[futureDay]);
  }
}
