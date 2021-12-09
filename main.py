from flask import Flask, request, jsonify

from custom_exceptions.duplicate_jersey_number_exception import DuplicateJerseyNumberException
from custom_exceptions.duplicate_team_name_exception import DuplicateTeamNameException
from data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from data_access_layer.implementation_classes.account_dao_imp import AccountDAOImp
from entities.customer import Customer
from entities.account import Account
from service_layer.implementation_service.customer_postgres_service import CustomerPostgresService
from service_layer.implementation_service.customer_service_imp import CustomerServiceImp
from service_layer.implementation_service.account_service_imp import AccountServiceImp
import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)

customer_dao = CustomerPostgresDAO()
customer_service = CustomerPostgresService(customer_dao)
account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)


# create player method
@app.post("/customer")
def create_customer_entry():
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["phoneNumber"],
            customer_data["customerId"]
        )
        customer_to_return = customer_service.service_create_customer(new_customer)
        customer_as_dictionary = customer_to_return.make_customer_dictionary()
        customer_as_json = jsonify(customer_as_dictionary)
        return customer_as_json
    except DuplicateJerseyNumberException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


# get customer information
@app.get("/customer/<customer_id>")
def get_customer_information(customer_id: str):
    result = customer_service.service_get_customer_by_id(int(customer_id))
    result_as_dictionary = result.make_customer_dictionary()
    result_as_json = jsonify(result_as_dictionary)
    return result_as_json


# get all customer information
@app.get("/customer")
def get_all_customers_information():
    customers_as_customers = customer_service.service_get_all_customers()
    customers_as_dictionary = []
    for customers in customers_as_customers:
        dictionary_customer = customers.make_customer_dictionary()
        customers_as_dictionary.append(dictionary_customer)
    return jsonify(customers_as_dictionary)


@app.patch("/customer/<customer_id>")
def update_customer_information(customer_id: str):
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["phoneNumber"],
            int(customer_id)
        )
        updated_customer = customer_service.service_update_customer(new_customer)
        return "Customer updated successfully, the customer info is now " + str(updated_customer)
    except DuplicateJerseyNumberException as e:
        return str(e)


# delete customer information
@app.delete("/customer/<customer_id>")
def delete_customer_information(customer_id: str):
    result = customer_service.service_delete_customer_by_id(int(customer_id))
    if result:
        return "Customer with id {} was deleted successfully".format(customer_id)
    else:
        return "Something went wrong: customer with id {} was not deleted".format(customer_id)


@app.post("/account")
def create_account():
    try:
        body = request.get_json()
        new_account = Account(
            body["accountId"],
            body["accountBalance"],
            body["customerId"]
        )
        created_account = account_service.service_create_account(new_account)
        created_account_as_dictionary = created_account.create_account_dictionary()
        return jsonify(created_account_as_dictionary), 201
    except DuplicateTeamNameException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


@app.get("/account/<account_id>")
def get_account_by_id(account_id: str):
    account = account_service.service_get_account_by_id(int(account_id))
    account_as_dictionary = account.create_account_dictionary()
    return jsonify(account_as_dictionary), 200


@app.get("/account")
def get_all_accounts():
    accounts = account_service.service_get_all_account()
    accounts_as_dictionaries = []
    for account in accounts:
        dictionary_account = account.create_account_dictionary()
        accounts_as_dictionaries.append(dictionary_account)
    return jsonify(accounts_as_dictionaries), 200


@app.patch("/account/<account_id>")
def update_account(account_id: str):
    try:
        body = request.get_json()
        update_info = Account(
            int(account_id),
            body["accountBalance"],
            body["customerId"]
        )
        updated_customer = account_service.service_update_account_information(update_info)
        updated_customer_as_dictionary = updated_customer.create_account_dictionary()
        return jsonify(updated_customer_as_dictionary), 200
    except DuplicateTeamNameException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message)


@app.delete("/account/<account_id>")
def delete_account(account_id: str):
    result = account_service.service_delete_account_information(int(account_id))
    if result:
        return "Account with id {} was deleted successfully".format(account_id)
    else:
        return "Something went wrong: account with id {} was not deleted".format(account_id)


@app.post("/deposit/<account_id>/<deposit_amount>")
def deposit_savings(account_id, deposit_amount):
    account_service.service_deposit(int(account_id), int(deposit_amount))
    return "Thanks for your deposit"


@app.post("/withdraw/<account_id>/<withdraw_amount>")
def withdraw_savings(account_id, withdraw_amount):
    account_service.service_withdraw(int(account_id), int(withdraw_amount))
    return "Thanks for your business"


app.run(host="0.0.0.0", port=5001)
