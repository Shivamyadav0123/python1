from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass
class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending email notification with message: {message}")
class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending SMS notification with message: {message}")
class PushNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending push notification with message: {message}")
def send_notification(notification: Notification, message: str) -> None:
    notification.send(message)
cc=EmailNotification()
sms=SMSNotification()
push=PushNotification()
send_notification(cc, "Hello, this is an email notification!")
send_notification(sms, "Hello, this is an SMS notification!")
send_notification(push, "Hello, this is a push notification!")