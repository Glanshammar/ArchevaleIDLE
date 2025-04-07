def calculate_xp_requirements(max_level=150, base_xp=100, increase_rate=0.10):
    xp_requirements = {}
    
    # Set the XP requirement for level 1
    xp_requirements[1] = base_xp
    
    for level in range(2, max_level + 1):
        # Calculate XP requirement for the current level
        # Current level's XP is the previous level's total plus 10% of previous level's total
        xp_requirements[level] = xp_requirements[level - 1] + int(xp_requirements[level - 1] * increase_rate)
    
    return xp_requirements

def main():
    max_level = 150
    base_xp = 100
    increase_rate = 0.10  # 10% increase
    
    xp_requirements = calculate_xp_requirements(max_level, base_xp, increase_rate)
    
    cumulative_xp_values = []
    total_xp = 0
    
    for level in range(1, max_level + 1):
        total_xp += xp_requirements[level]
        cumulative_xp_values.append(total_xp)
    
    print(cumulative_xp_values)

if __name__ == "__main__":
    main()
