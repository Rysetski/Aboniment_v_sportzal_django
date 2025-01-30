from celery import shared_task
from .models import Notification
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from apps.subscriptions.models import Subscription
from django.conf import settings

@shared_task
def send_notification(user_id, message):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    user = User.objects.get(id=user_id)
    Notification.objects.create(user=user, message=message)
    return f"Notification sent to {user.username}"




@shared_task
def test_task():
    print("Celery is working!")
    return "Task executed successfully"


@shared_task
def send_email_about_subscription(user_id, subscription_id):
    """
    Отправляет email при покупке абонемента.
    """
    User = get_user_model()
    user = User.objects.get(pk=user_id)
    subscription = Subscription.objects.get(pk=subscription_id)

    subject = f"Оформлен абонемент в {subscription.gym.name}"
    message = (
        f"Здравствуйте, {user.username}!\n\n"
        f"Вы успешно оформили абонемент в {subscription.gym.name}.\n"
        f"Даты действия: {subscription.start_date} - {subscription.end_date}\n"
        f"Стоимость: {subscription.price}.\n\n"
        "Спасибо за вашу покупку!"
    )

    # Адрес 'from_email' можно указать непосредственно в send_mail 
    # или взять из settings.DEFAULT_FROM_EMAIL
    from_email = settings.DEFAULT_FROM_EMAIL  
    recipient_list = [user.email]

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False
    )
    return f"Email sent to {user.email}"