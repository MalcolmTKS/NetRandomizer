# Extract strings from file 


def parse_user_agents(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        user_agents = [line.strip() for line in f if line.strip()]
    return user_agents


if __name__ == "__main__":
    file_path = "/*/*/user-agents.txt"
    user_agents = parse_user_agents(file_path)

    # Print the first 15 user agents
    for ua in user_agents[:15]:
        print(ua)
