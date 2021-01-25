# Implement a function meetingPlanner that given the availability, slotsA and slotsB, 
# of two people and a meeting duration dur, returns the earliest time slot that works for both of them 
# and is of duration dur. If there is no common time slot that satisfies the duration requirement, return an empty array.

def meeting_planner(slotsA, slotsB, dur):
  for A in slotsA:
    if A[1] - A[0] >= dur:
      for B in slotsB:
        if B[1]-B[0] >= dur:
          left = max(A[0],B[0])
          right = min(A[1],B[1])
          if right - left >= dur:
            return [left, left+dur]
         
  return []