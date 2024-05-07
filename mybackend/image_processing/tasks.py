from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    for i in 100:
        print("Hello")
    return "Done"
    
