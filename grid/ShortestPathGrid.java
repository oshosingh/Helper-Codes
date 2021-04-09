import java.util.*;

public class ShortestPathGrid {
	
	static class QItem{
		int row;
		int col;
		int dist;
		public QItem(int row, int col, int dist){
			this.row = row;
			this.col = col;
			this.dist = dist;
		}
	}
	
	private static int minDistance(char[][] grid){
		QItem source = new QItem(0,0,0);
		
		//finding source
		for(int i=0; i<grid.length;i++){
			for(int j=0; j<grid[0].length;j++){
				if(grid[i][j]=='s'){
					source.row = i;
					source.col = j;
					break;
				}
			}
		}
		
		// Applying BFS on grid cells
		Queue<QItem> queue = new LinkedList<>();
		boolean visited[][] = new boolean[grid.length][grid[0].length];
		
		queue.add(new QItem(source.row, source.col, 0)); visited[source.row][source.col] = true;
		
		while(queue.isEmpty()==false){
			QItem p = queue.remove();
			
			// Destination Found
			if(grid[p.row][p.col]=='d'){
				return p.dist;
			}
			
			// Moving Up
			if(isValid(p.row-1, p.col, grid,visited)){
				queue.add(new QItem(p.row-1, p.col, p.dist+1));
				visited[p.row-1][p.col] = true;
			}
		
			// moving down
		      if (isValid(p.row + 1, p.col, grid, visited)) {
		        queue.add(new QItem(p.row + 1, p.col,
		                            p.dist + 1));
		        visited[p.row + 1][p.col] = true;
		      }
		 
		      // moving left
		      if (isValid(p.row, p.col - 1, grid, visited)) {
		        queue.add(new QItem(p.row, p.col - 1,
		                            p.dist + 1));
		        visited[p.row][p.col - 1] = true;
		      }
		 
		      // moving right
		      if (isValid(p.row - 1, p.col + 1, grid,
		                  visited)) {
		        queue.add(new QItem(p.row, p.col + 1,
		                            p.dist + 1));
		        visited[p.row][p.col + 1] = true;
		      }
		}
		return -1;
	}
	
	private static boolean isValid(int i, int j, char[][] grid, boolean[][] visited){
		if(i>=0 && j>=0 && i<grid.length && j<grid[0].length && grid[i][j]!='0' && visited[i][j]==false){
			return true;
		}
		return false;
	}

	public static void main(String[] args) {
		char[][] grid = { { '0', '*', '0', 's' },
                { '*', '0', '*', '*' },
                { '0', '*', '*', '*' },
                { 'd', '*', '*', '*' } };

		System.out.println(minDistance(grid));
	}

}

/**
	Given a matrix of N*M order. Find the shortest distance from a source cell to a destination cell, 
	traversing through limited cells only. Also you can move only up, down, left and right. 
	If found output the distance else -1. 
s represents ‘source’ 
d represents ‘destination’ 
* represents cell you can travel 
0 represents cell you can not travel 
This problem is meant for single source and destination.
*/