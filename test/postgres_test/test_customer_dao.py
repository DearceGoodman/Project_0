from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customer import Customer

customer_dao = CustomerPostgresDAO()
customer: Customer = Customer("first", "last", 23, 1)

random_names = {"Bob"}
random_names.add("Sally")
random_names.add("Bill")
random_names.add("Susie")

random_name = random_names.pop()

update_customer = Customer(random_name, "player", 200, 1)

customer_to_delete = Customer(random_names.pop(), random_names.pop(), 0, 1)


def test_create_customer_success():
    created_customer = customer_dao.create_customer_entry(customer)
    assert created_customer.customer_id != 0


def test_get_customer_success():
    brandon_roy = customer_dao.get_customer_information(1)
    assert brandon_roy.first_name == "Brandon" and brandon_roy.last_name == "Roy"


def test_get_all_customer_success():
    customers = customer_dao.get_all_customers_information()
    assert len(customers) > 2


def test_update_customer_success():
    updated_customer = customer_dao.update_customer_information(update_customer)
    assert updated_customer.first_name == random_name


def test_delete_player_success():
    customer_to_be_deleted = customer_dao.create_customer_entry(customer_to_delete)
    result = customer_dao.delete_customer_information(customer_to_be_deleted.customer_id)
    assert result
