# #each login event contains timestamp, username, ip_address, status
# timestamp = integer representing seconds
# username = account
# ip_address = source IP
# status is either success or failure
# suspicious user = threshold failed login attempts within any window_seconds period
# return all sus users in alpha order

#first split the list and save each attribute in a dictionary for counter, store only if the window seconds makes sense


def find_suspicious_users(events, threshold, window_seconds):

     failed_attempts = {}

     for i in events:
        timestap, username,ip, status = i.split()

        if status == "failure":
            failed_attempts[username] = 1
    
    
     # return suspicious_users

def main_input():
    n = int(input())

    events = []

    for _ in range(n):
        events.append(input())

    threshold = int(input())
    window_seconds = int(input())

    suspicious_users = find_suspicious_users(
        events,
        threshold,
        window_seconds
    )

    if suspicious_users:
        for username in suspicious_users:
            print(username)
    else:
        print("NONE")