"""Actual PID/boot/start observer, preserving the closed run's evidence."""
from chat_lr_contract import RUN
import observe_chat_semantic_jobs as observer

observer.RUN = RUN

if __name__ == '__main__':
    observer.main()
