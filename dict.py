# Create a dictionary of baseball players and their home run counts
players = {
    "Player A": 25,
    "Player B": 30,
    "Player C": 15
}

# Access a value using get()
print("Player A's home runs:", players.get("Player A"))

# Add a new player using assignment
players["Player D"] = 20
print("\nAfter adding Player D:", players)

# Update a player's home runs using update()
players.update({"Player A": 28})
print("\nAfter updating Player A's home runs:", players)

# Remove a player using pop()
removed_home_runs = players.pop("Player C")
print("\nAfter removing Player C:", players)
print(f"Removed Player C's home runs: {removed_home_runs}")

# Check if a player is in the dictionary using in
print("\nIs Player B in the dictionary?", "Player B" in players)

# Iterate through keys, values, and items
print("\nPlayers and their home runs:")
for player, home_runs in players.items():
    print(f"{player}: {home_runs}")

# Clear all players
players.clear()
print("\nAfter clearing the dictionary:", players)
