"""Run the frozen comparison with the documented in-memory metadata alias."""
import compare_chat_semantic as frozen_comparison
from review_chat_semantic_observer import get_items

if __name__ == '__main__':
    frozen_comparison.get_items = get_items
    frozen_comparison.main()
