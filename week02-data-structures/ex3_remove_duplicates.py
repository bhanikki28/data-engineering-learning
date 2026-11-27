emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
print(len(emails))
unique_emails = list(dict.fromkeys(emails))
print("Unique Emails Count : ", len(unique_emails))
unique_emails_set = set(emails)
print("Unique Emails Count : ", len(unique_emails_set))
