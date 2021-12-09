class Customer:
    def __init__(self, first_name: str, last_name: str, phone_number: int, customer_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.customer_id = customer_id

    def make_customer_dictionary(self):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "phoneNumber": self.phone_number,
            "customerId": self.customer_id
        }

    def __str__(self):
        return "first name: {}, last name: {}, phone number: {}, customer_id: {}".format(self.first_name,
                                                                                         self.last_name,
                                                                                         self.phone_number,
                                                                                         self.customer_id)
