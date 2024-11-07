public class AlphabetDiamondPattern {
  public static void main(String[] args) {

    int rows = 7;
    
    for (int i = 1; i <= rows; i++) {
    
      for (int j = 1; j <= rows - i; j++) {
          System.out.print(" ");
      }

      for (int j = 1; j <= i; j++) {
          System.out.print(  j - 1) + "");
      }

      for (int j = i - 1; j >= 1; j--) {
          System.out.print((char) ('A' + j - 1) + "");
      }
      System.out.println();
    }
    
    
    
    
    for (int i = rows - 1; i >= 1; i--) {
      
      for (int j = 1; j <= rows - i; j++) {
          System.out.print(" ");
      }
      
      for (int j = 1; j <= i; j++) {
          System.out.print((char) ('A' + j - 1) + "");
      }
      
      for (int j = i - 1; j >= 1; j--) {
          System.out.print((char) ('A' + j - 1) + "");
      }
      System.out.println();
    }
  }
}

