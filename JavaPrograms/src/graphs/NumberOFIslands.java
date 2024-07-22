package graphs;

public class NumberOFIslands {
    static boolean[][] visited;

    public int numIslands(char[][] grid) {

        int g_row = grid.length;
        int g_col = grid[0].length;
        int count = 0;
        visited = new boolean[g_row][g_col];

        if (g_row == 0)
            return 0;

        for (int row = 0; row < g_row; row++) {
            for (int col = 0; col < g_col; col++) {
                if (grid[row][col] == 1 && !visited[row][col]) {
                    bfsMarkVisit(grid, row, col);
                    count++;
                }
            }
        }

        return count;
    }

    private void bfsMarkVisit(char[][] grid, int row, int col) {

        boolean isInScope = row >= 0 && col >= 0 && row < grid.length && col < grid[0].length;

        if (isInScope && grid[row][col] == 1) {
            grid[row][col] = 0;
            bfsMarkVisit(grid, row + 1, col);
            bfsMarkVisit(grid, row, col + 1);
            bfsMarkVisit(grid, row - 1, col);
            bfsMarkVisit(grid, row, col - 1);
        }

    }


    public static void main(String[] args) {
//        char[][] grid= {
//                {1, 1, 1, 1, 0},
//                {1, 1, 0, 1, 0},
//                {1, 1, 0, 0, 0},
//                {0, 0, 0, 0, 0}
//        };

        char[][] grid = {{1, 1, 0, 0, 0},
                {1, 1, 0, 0, 0},
                {0, 0, 1, 0, 0},
                {0, 0, 0, 1, 1}};


        System.out.println(new NumberOFIslands().numIslands(grid));

    }

}
