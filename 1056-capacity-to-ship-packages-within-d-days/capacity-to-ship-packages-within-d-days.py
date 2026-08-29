class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lowrange = max(weights)
        highrange = sum(weights)

        def canfinish(weights, days, mid):
            load = 0
            req_days = 1
            for weight in weights:
                if load + weight <= mid:
                    load += weight
                else:
                    req_days += 1
                    load = weight
            return req_days <= days

        while lowrange <= highrange:
            mid = (lowrange + highrange) // 2
            if canfinish(weights, days, mid):
                highrange = mid - 1
            else:
                lowrange = mid + 1

        return lowrange