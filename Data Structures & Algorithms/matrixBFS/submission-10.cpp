class Solution {
public:
    int shortestPath(vector<vector<int>>& grid) {
        // Need to create the boundary constraints first, the rows and the columns
        int m = grid.size();
        int n = grid[0].size();

        // Create the visit set, use a 4x4 array, see if you can use the sizes based on the columns
        vector<vector<int>> visit(m, vector<int>(n));

        // Create the queue
        queue<pair<int,int>> queue;

        //! Insert the first value, ie the root
        queue.push(pair<int,int>(0,0));

        //! Make sure this is visited as well
        visit[0][0]=1;

        //! Start the main BFS protocol
        int length = 0;

        while(! queue.empty()) {
            //! Take the current length
            int len = queue.size();

            //! Run basic BFS
            for(int i = 0; i < len; i+=1) {
                // Record the node to search from
                pair<int,int> curr = queue.front();

                //Pop it to make sure no issues
                queue.pop();

                //! Extract the values
                int r = curr.first;
                int c = curr.second;

                //! Check the victory clause
                if(r == m-1 && c == n-1) {
                    return length;
                }

                //! populate the movement matrix
                int neighbours[4][2] = {{r,c+1}, {r,c-1}, {r+1, c}, {r-1,c}};
                for(int j = 0; j < 4; j+=1) {
                    // Get the values of rows and columns

                    int newR = neighbours[j][0];
                    int newC = neighbours[j][1];
                    if(min(newR, newC) < 0 || newR == m || newC == n || visit[newR][newC]==1 || grid[newR][newC]==1) {
                        continue;
                    }

                    //Push into the queue to get processed down the line
                    queue.push(pair<int, int>(newR, newC));

                    // Make sure this is visited
                    visit[newR][newC] = 1;
                }

            }

            length += 1;
        }
        return -1;

    }
};
