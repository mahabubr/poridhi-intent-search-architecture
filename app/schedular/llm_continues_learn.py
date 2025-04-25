from apscheduler.schedulers.background import BackgroundScheduler


def llm_learn():
    print("LLM learn is running...")


scheduler = BackgroundScheduler()

scheduler.add_job(llm_learn, "interval", minutes=1)


def start_model_continues_learn():
    scheduler.start()


def shutdown_model_continues_learn():
    scheduler.shutdown()
