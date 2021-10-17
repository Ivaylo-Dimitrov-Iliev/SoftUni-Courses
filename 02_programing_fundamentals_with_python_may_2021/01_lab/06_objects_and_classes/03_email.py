class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


command = input()

list_of_emails = []

while not command == "Stop":
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    list_of_emails.append(email)
    command = input()

indexes_of_send_emails = [int(el) for el in input().split(", ")]

for index in indexes_of_send_emails:
    list_of_emails[index].send()

for email in list_of_emails:
    print(email.get_info())
