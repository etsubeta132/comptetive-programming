class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)

        has_dp = [[False]*(N+1) for i in range(N+1)]
        dp = [[None]*(N+1) for i in range(N+1)]

        def Score(left,right):
            if left > right:
                return  0
            
            if has_dp[left][right]:
                return dp[left][right]
            
            
            score_left = nums[left] - Score(left+1, right)
            score_right = nums[right] - Score(left, right-1)
            
            
            has_dp[left][right] = True
            dp[left][right] = max(score_left,score_right)

            return dp[left][right]
        
          
        return Score(0,N-1)>=0

            


            
                





