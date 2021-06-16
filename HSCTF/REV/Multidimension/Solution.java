import java.util.Scanner;

public class Main {
	
	private char[][] arr = {{104,101,121,95,115,105},{110,99,101,95,119,104},{101,110,95,119,97,115},{95,116,105,109,101,95},{97,95,100,105,109,101},{110,115,105,111,110,63}};
	public void line() {
		char[][] newArr = new char[arr.length][arr[0].length];
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[0].length; j++) {
				int p = i - 1, q = j - 1, f = 0;
				boolean row = i % 2 == 0;
				boolean col = j % 2 == 0;
				if (row) {
					p = i + 1;
					f++;
				} else
					f--;
				if (col) {
					q = j + 1;
					f++;
				} else
					f--;
				newArr[p][q] = (char) (arr[i][j] + f);
			}
		}
		arr = newArr;
	}
	
	public void print() {
	    for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[0].length; j++) {
			    System.out.print(arr[i][j]);
			}
	    }
	    System.out.println();
	}
	
	public void plane() {
		int n = arr.length;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				arr[i][j] -= i + n - j;
			}	
		}
		for (int i = 0; i < n / 2; i++) {
			for (int j = 0; j < n / 2; j++) {
				char t = arr[i][j];
				arr[i][j] = arr[n - 1 - j][i];
				arr[n - 1 - j][i] = arr[n - 1 - i][n- 1 -j];
				arr[n - 1 - i][n- 1 -j] = arr[j][n - 1 - i];
				arr[j][n - 1 - i] = t;
			}
		}
	}
	
	public void space(int n) {
		arr[(35 - n) / 6][(35 - n) % 6] += (n / 6) + (n % 6);
		if (n != 0) {
			n--;
			space(n);
		}
	}
	
	public void time() {
		int[][] t = {{8, 65, -18, -21, -15, 55}, 
				{8, 48, 57, 63, -13, 5}, 
				{16, -5, -26, 54, -7, -2}, 
				{48, 49, 65, 57, 2, 10}, 
				{9, -2, -1, -9, -11, -10}, 
				{56, 53, 18, 42, -28, 5}};
		for (int j = 0; j < arr[0].length; j++)
			for (int i = 0; i < arr.length; i++)
				arr[i][j] -= t[j][i];
	}
	
	public static void main(String[] args) {
			Main f = new Main();
			f.time();
			f.print();
			f.space(35);
			f.print();
			f.plane();
			f.print();
			f.line();
			f.print();
		}

}
