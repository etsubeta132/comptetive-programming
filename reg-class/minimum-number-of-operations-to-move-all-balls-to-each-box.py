class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ball_box = [int(num_ball) for num_ball in boxes]
        ball = []

        for i in range(len(ball_box)):
            total = 0
            for j in range(len(ball_box)):
                total+=ball_box[j]*(abs(j-i))
            ball.append(total)
        
        return ball

