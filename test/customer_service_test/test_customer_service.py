from custom_exceptions.duplicate_jersey_number_exception import DuplicateJerseyNumberException
from data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from entities.customer import Customer
from service_layer.implementation_service.customer_service_imp import CustomerServiceImp

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)
customer = Customer("service", "testing", 100, 1)
customer_update = Customer("update", "test", 100, 2)


def test_validate_create_customer_method():
    try:
        for existing_customer in customer_service.customer_dao.customer_list:
            print(existing_customer)
        unexpected_customer = customer_service.service_create_customer(customer)
        print()
        for existing_customer in customer_service.customer_dao.customer_list:
            print(existing_customer)
            print()
        print(unexpected_customer.customer_id)
        assert False
    except DuplicateJerseyNumberException as e:
        assert str(e) == "Customer Id is already taken!"


def test_validate_update_customer_method():
    try:
        customer_service.service_update_customer(customer_update)
        assert False
    except DuplicateJerseyNumberException as e:
        assert str(e) == "Phone number already taken!"
