from customerDatabaseQueries.search_customer_query_handler import SearchCustomerHandler

''' Utility functions for the UI logic classes. '''


class UtilsForUI:
    @staticmethod
    def check_if_customer_exists(email: str) -> list:
        search_for_email_in_customers_table = SearchCustomerHandler.search_customer_by_email(email)

        if search_for_email_in_customers_table:
            return search_for_email_in_customers_table[0]
        return None
