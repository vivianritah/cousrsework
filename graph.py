def find_mutual_friends(graph, user1, user2):
    friends_user1 = set(graph[user1])
    friends_user2 = set(graph[user2])
    mutual_friends = friends_user1.intersection(friends_user2)
    return list(mutual_friends)


def suggest_friends(graph, user):
    suggestions = set()
    user_friends = set(graph[user])
    
    for friend in user_friends:
        for potential_friend in graph[friend]:
            if potential_friend != user and potential_friend not in user_friends:
                suggestions.add(potential_friend)
                
    return list(suggestions)


from collections import deque

def shortest_path(graph, start_user, end_user):
    queue = deque([(start_user, [start_user])])
    visited = set()
    
    while queue:
        current_user, path = queue.popleft()
        if current_user == end_user:
            return path
        
        if current_user not in visited:
            visited.add(current_user)
            for neighbor in graph[current_user]:
                queue.append((neighbor, path + [neighbor]))
    
    return None  # Return None if there is no path


# Example graph structure
graph = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Alice", "David"],
    "Charlie": ["Alice", "David"],
    "David": ["Bob", "Charlie", "Eve"],
    "Eve": ["David"]
}

# 1. Finding mutual friends between "Bob" and "Charlie"
print("Mutual Friends:", find_mutual_friends(graph, "Bob", "Charlie"))

# 2. Suggesting friends for "Alice"
print("Friend Suggestions for Alice:", suggest_friends(graph, "Alice"))

# 3. Calculating the shortest path between "Alice" and "Eve"
print("Shortest Path from Alice to Eve:", shortest_path(graph, "Alice", "Eve"))
