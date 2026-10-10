class Solution {
public:
    int dfs(vector<vector<int>>& grid, int row, int col, vector<vector<int>>& hashset) {
        int ROW = grid.size();
        int COL = grid[0].size();

        // List the base cases that can cause a failure
        if(min(row, col) < 0 || row == ROW || col == COL || hashset[row][col]==1 || grid[row][col]==1) {
            return 0;
        }


        // List the case that causes a success

        if(row == ROW - 1 && col == COL - 1) {
            return 1;
        }
        // Add that this node has been visited
        hashset[row][col] = 1;
        // Move through the graph assuming that
        int count = 0;

        //! go up
        count += dfs(grid, row-1, col, hashset);

        //! go down
        count += dfs(grid, row+1, col, hashset);

        //! go left
        count += dfs(grid, row, col-1, hashset);

        //! go right
        count += dfs(grid, row, col+1, hashset);
        // Unmount the node
        hashset[row][col] = 0;
        // Return

        return count;
    }
    int countPaths(vector<vector<int>>& grid) {
        return dfs(grid, 0, 0, grid);
    }
};
