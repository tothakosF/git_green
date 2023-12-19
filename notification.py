from win10toast import ToastNotifier


def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)


# Example
show_notification("Python Notification",
                  "This is a sample notification from Python.")
