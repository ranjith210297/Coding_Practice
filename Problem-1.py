/* Java program to find the sum of elements in each row and each column of the given matrix and print the greatest of the same */
import java.util.*;
public class Main
{
	public static void main(String[] args)
		{	
			Scanner sc = new Scanner(System.in);
			int m, n, row, col, sum = 0, row_ind = 0, col_ind = 0;
			m = sc.nextInt();
			n = sc.nextInt();
			int[] row_arr = new int[m];
			int i, j;
			int[][] mat = new int[m][n];
			for(i = 0; i < m; i++)
				{
					for(j = 0; j < n; j++)
						mat[i][j] = sc.nextInt();
				}

			int z = 0;

			System.out.print(“Sum of rows is “);
			for(row=0; row<m; row++)
				{
					sum = 0;
					for(col=0; col<n; col++)
						{
							sum += mat[row][col];
						}

					System.out.print(sum + ” “);

					row_arr[z++] = sum;
				}
			int temp_row = row_arr[0];
			for(i=1;i<m;i++)
				{
					if(temp_row < row_arr[i])
						{
							temp_row = row_arr[i];
							row_ind = i;
						}

				}
			System.out.print(“\nRow ” + ++row_ind + ” has maximum sum “);

			System.out.print(“\nSum of columns is “);
			sum = 0;
			int y = 0;
			int[] col_arr = new int[n];
			for (i = 0; i < n; ++i)
				{
					sum = 0;
					for (j = 0; j < m; ++j)
						{
							sum = sum + mat[j][i];
						}
					System.out.print(sum + ” “);
					
					col_arr[y++] = sum;
	
            }

	int temp_col = col_arr[0];
	for(i=1;i<n;i++)
		{
			if(temp_col < col_arr[i])
				{
					temp_col = col_arr[i];
					col_ind = i;
				}
		
		}
	System.out.print(“\nColumn ” + ++col_ind + ” has maximum sum “);
	}

}