class DatabaseConnection:
    message = "Database connection ..."

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def type_DatabaseConnect(self):
        self.connectiontype = "online database"
        print(DatabaseConnection.message)
        return f"Name: {self.hostname}, port: {self.port}, type: {self.connectiontype}"


# While loop for continuous user input
while True:
    hostname = input("Enter the hostname: ")
    if hostname == "":
        print("Hostname cannot be empty. Please try again.")
        continue

    try:
        port = int(input("Enter the port number: "))
    except ValueError:
        print("Invalid port number. Please enter a valid integer.")
        continue

    # Create a database connection object
    db_connection = DatabaseConnection(hostname, port)
    print(db_connection.type_DatabaseConnect())

    # Ask user if they want to continue
    choice = input("Do you want to create another connection? (yes/no): ")
    if choice.lower() != "yes":
        print("Exiting the program.")
        break
