our_routes = {"LAX", "JFK", "CDG", "DXB", "MDW"}
competitor_routes = {"JFK", "CDG","LHR", "BKK", "MDW"}
same_routes = our_routes.intersection(competitor_routes)
unique_routes = our_routes.difference(competitor_routes)
here_or_there = our_routes.symmetric_difference(competitor_routes)

print(f"Here are the routes we share:\n{same_routes}")
print(f"here are the routes that are only offered by our airline:\n{unique_routes}")
print(f"Here are the destinations that neither airline share:\n{here_or_there}")