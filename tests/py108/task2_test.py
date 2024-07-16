from src.py108 import task2
from tests.helper.ClassSignature import ClassSignature
from tests.helper.custom_assertions import (
    assert_almost_equals,
    assert_class_signature,
    assert_equals,
)
from tests.helper.FunctionSignature import FunctionSignature


class TestTask2:
    def test_a_deposit_increases_the_balance(self):
        self.__assert_class_signature()

        module = task2
        class_name = "Account"
        initial_balance = 1000
        deposit_amount = 300
        sut = getattr(module, class_name)(initial_balance)

        sut.deposit(deposit_amount)

        assert_equals(
            message=f"> Initial balance= {initial_balance}\n> Amount to deposit= {deposit_amount}",
            expected=1300.00,
            actual=sut.balance,
        )

    def test_withdrawing_an_amount_less_than_current_balance_reduces_the_balance(self):
        self.__assert_class_signature()

        module = task2
        class_name = "Account"
        initial_balance = 1000
        withdrawal_amount = 500.0
        sut = getattr(module, class_name)(initial_balance)

        sut.withdrawal(withdrawal_amount)

        assert_equals(
            message=f"> Withdrawal {withdrawal_amount} from the balance of the account with a balance of {initial_balance}",
            expected=500.00,
            actual=sut.balance,
        )

    def test_withdrawing_an_amount_greater_than_current_balance(self):
        self.__assert_class_signature()

        module = task2
        class_name = "Account"
        initial_balance = 1000
        withdrawal_amount = 5000
        sut = getattr(module, class_name)(initial_balance)

        sut.withdrawal(withdrawal_amount)

        assert_equals(
            message=f"> Withdrawal {withdrawal_amount} from the balance of the account with a balance of {initial_balance}",
            expected=1000.00,
            actual=sut.balance,
        )

    def test_returns_the_new_balance_after_the_bank_fee(self):
        self.__assert_class_signature()

        module = task2
        class_name = "Account"
        initial_balance = 1000
        sut = getattr(module, class_name)(initial_balance)

        sut.fee()

        assert_almost_equals(
            message=f"Calculate the fee for an account with balance of {initial_balance}",
            expected=950.0,
            actual=sut.balance,
        )

    def __assert_class_signature(self):
        module = task2
        class_name = "Account"

        assert_class_signature(
            module=module,
            class_signature=ClassSignature(
                class_name=class_name,
                properties=["balance"],
                methods=[
                    FunctionSignature(function_name="deposit", number_of_parameters=2),
                    FunctionSignature(
                        function_name="withdrawal", number_of_parameters=2
                    ),
                    FunctionSignature(function_name="fee", number_of_parameters=1),
                ],
            ),
        )
