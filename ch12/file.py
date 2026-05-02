
path = r"ch12\계좌1.txt"
mode = "w"

f = open(path, mode, encoding="utf-8")

accounts = {
    "김삿갓": "597-89-000089",
    "이수근": "343-64-000064",
    "박혁거세": "136-97-000097"
}

for name, account in accounts.items():
    f.write(f"{name} {account}\n")

f.close()





# path = r"ch12\계좌1.txt"


# accounts = {
#     "김삿갓": "597-89-000089",
#     "이수근": "343-64-000064",
#     "박혁거세": "136-97-000097"}

# with open(path, "w", encoding="utf-8") as f:
#     for name, account in accounts.items():
#         f.write(f"{name} {account}\n")


