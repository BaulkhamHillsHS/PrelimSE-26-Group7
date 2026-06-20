import csv
cfile = csv.reader(open('subscribed_members.csv', "r"), delimiter=",")
next(cfile)
for row in cfile:
    user = row[0]
    subscription = row[3]
    file = open(f"Subscription_invoice\\{user}.txt", "w")
    file.write(f"Started as {subscription}")
    file.write("\n")
    file.close
print("Data is written")