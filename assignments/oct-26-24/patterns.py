rowA = 6
print("Pattern A")
    
for rowA in range(1, rowA+1):
    for colA in range(1, rowA+1):
        print("*", end="")
    print()
print()



System.out.println("pattern B");
	
	for rowB range(1, rowB+!2) {
		for (int colB = 6; colB >= rowB; colB--) {
			System.out.print("*");
		}
		System.out.println();
	}
	
	System.out.println("pattern C");
	for (int rowC = 6; rowC >= 1; rowC--) {
		for (int space = 1; space <= 6 - rowC; space++) {
			System.out.print(" ");
  }
        
	for (int colC = 1; colC <= rowC; colC++) {
 			 System.out.print("*");
	 }
		System.out.println();
	}
		System.out.println();
		
	System.out.println("pattern D");
	for (int rowD = 1; rowD <= 6; rowD++) {
		for (int spaceD = 1; spaceD <= 6 - rowD; spaceD++) {
			System.out.print(" ");
  }
		for (int colD = 1; colD <= rowD; colD++) {
			System.out.print("*");
		}
		System.out.println();
	}
	System.out.println();

