import torch
import pytest

from jmicro.export import llama_rope_rows


def test_llama_rope_row_conversion_preserves_each_head_pair():
    matrix = torch.arange(8 * 3).reshape(8, 3)
    expected = matrix[[0, 2, 1, 3, 4, 6, 5, 7]]
    assert torch.equal(llama_rope_rows(matrix, 2), expected)
    assert torch.equal(llama_rope_rows(matrix, 1), matrix[[0, 4, 1, 5, 2, 6, 3, 7]])
    with pytest.raises(ValueError, match="complete even"):
        llama_rope_rows(matrix, 3)
