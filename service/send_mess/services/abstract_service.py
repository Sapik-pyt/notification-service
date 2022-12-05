from abc import ABC, abstractmethod


class ServiceAbctract(ABC):
    @abstractmethod
    def validate_data_method_post(self, *args):
        pass

    @abstractmethod
    def validate_data_method_put(self, *args):
        pass

    @abstractmethod
    def create(self, *args):
        pass

    @abstractmethod
    def put(self, *args):
        pass

    @abstractmethod
    def delete(self, *args):
        pass

    @abstractmethod
    def method_get_of_list_is_validate(self, *args):
        pass

    @abstractmethod
    def method_get_client_info(self, *args):
        pass
