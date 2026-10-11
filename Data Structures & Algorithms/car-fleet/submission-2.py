class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0
        cars=sorted([[p,s] for p,s in zip(position,speed)],reverse=True)
        prev_time=0
        carfleets=0
        for p,s in cars:
            current_time=(target-p)/s
            if current_time>prev_time:
                carfleets+=1
                prev_time=current_time
        return carfleets
