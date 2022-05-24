from datetime import datetime, timedelta

from celery import shared_task
from .models import Order
import time


@shared_task
def complete_order(oid):
    order = Order.objects.get(pk=oid)
    order.complete = True
    order.save()


@shared_task
def clear_old():
    old_orders = Order.objects.all().exclude(time_in__gt =
                        datetime.now() - timedelta(minutes = 1))
    old_orders.delete()
# Example
# @shared_task
# def hello():
#     time.sleep(10)
#     print("Hello, world!")
#
#
# @shared_task
# def printer(N):
#     for i in range(N):
#         time.sleep(1)
#         print(i+1)
# End of example
