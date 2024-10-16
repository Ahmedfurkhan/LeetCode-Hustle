import heapq

class Item:
    def __init__(self, friend_id, start_time, end_time):
        self.friend_id = friend_id      # Unique identifier for each friend
        self.start_time = start_time    # Time the friend arrives
        self.end_time = end_time        # Time the friend leaves
        self.chair = -1                 # Initially, no chair assigned (-1)
    
    def set_chair(self, chair):
        self.chair = chair              # Method to assign a chair to the friend

    # This comparison is used to sort friends by their end time
    def __lt__(self, other):
        return self.end_time < other.end_time

class Solution:
    def smallestChair(self, times, target_friend):
        arrival = []      # List to store Item objects representing friends
        available = []    # Min-heap to track available chairs
        assigned = []     # Min-heap to track friends currently sitting, sorted by end_time

        # Create Item objects for each friend and push all chair numbers into available heap
        for i in range(len(times)):
            arrival.append(Item(i, times[i][0], times[i][1]))
            heapq.heappush(available, i)  # Chair numbers (0, 1, 2, ...) added to heap
        
        # Sort the friends based on their arrival time
        arrival.sort(key=lambda x: x.start_time)

        # Process each friend in order of their arrival time
        for item in arrival:
            # Free up chairs from friends who have already left by the time this friend arrives
            while assigned and assigned[0].end_time <= item.start_time:
                freed_item = heapq.heappop(assigned)      # Friend with the earliest end_time leaves
                heapq.heappush(available, freed_item.chair)  # Add their chair back to available chairs
            
            # Assign the smallest available chair to the current friend
            item.set_chair(heapq.heappop(available))
            heapq.heappush(assigned, item)  # Add current friend to assigned heap (sorted by end_time)

            # If the current friend is the target friend, return the assigned chair number
            if item.friend_id == target_friend:
                return item.chair

        return -1  # Return -1 if target_friend is not found (unlikely scenario)

