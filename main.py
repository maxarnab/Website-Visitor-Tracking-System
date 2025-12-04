import csv

def track_unique_visitors(visits):
    # Remove duplicate tuples
    unique_visits = list(set(visits))

    # Count unique users for each website
    website_users = {}

    for user, site in unique_visits:
        if site not in website_users:  #check whether we already have an entry for this website.
            website_users[site] = set() #when website key is missing, create it as an empty set to collectuser IDs.
        website_users[site].add(user)  # add the current user ID to the set for that site.

    # Returning list of tuples (website, unique_count)
    return [(site, len(users)) for site, users in website_users.items()]


def load_csv(filename):
    visits = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            visits.append((int(row["user_id"]), row["website"]))
    return visits


# Loading the CSV data
visits = load_csv("example.csv")

# Processing and print results
result = track_unique_visitors(visits)
print(result)
