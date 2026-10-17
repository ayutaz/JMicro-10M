"""Reuse exact process/lock observation under separate resource-v2 contract."""
from run_answer_curriculum_resource_v2 import CONFIG,RUN,contract
import inspect_answer_curriculum as original
original.CONFIG=CONFIG;original.RUN=RUN;original.preflight=contract.preflight


if __name__=='__main__':original.main()
