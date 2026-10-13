"""Bind literal reviewer-authored TSV indices; no score inference."""
from chat_lr_contract import RUN
import bind_chat_semantic_authored_scores as binder

binder.RUN = RUN

if __name__ == '__main__':
    binder.main()
