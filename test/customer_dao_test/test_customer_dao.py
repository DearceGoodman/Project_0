from data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customer import Customer

customer_dao_postgres = CustomerPostgresDAO()
customer_dao_imp = CustomerDAOImp()
customer = Customer("Test", "Player", 12, 1)
customer_for_postgres = Customer("Isassas", "Baker", 102, 0)


def test_create_customer_success():
    new_customer: Customer = customer_dao_postgres.create_customer_entry(customer_for_postgres)
    print(new_customer.customer_id)
    assert new_customer.customer_id != 0


def test_get_customer_success():
    returned_customer: Customer = customer_dao_postgres.get_customer_information(1)
    assert returned_customer.customer_id == 1


def test_get_all_customers_success():
    customer_list = customer_dao_postgres.get_all_customers_information()
    assert len(customer_list) >= 2


def test_update_customer_success():
    updated_info = Customer("changed by", "update customer method", 105, 1)
    updated_customer: Customer = customer_dao_postgres.update_customer_information(updated_info)
    assert updated_customer.phone_number == updated_info.phone_number


def test_delete_customer_success():
    confirm_customer_deleted = customer_dao_postgres.delete_customer_information(4)
    assert confirm_customer_deleted
