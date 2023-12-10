import pytest
from src.task_1 import DataTable


@pytest.mark.parametrize(
    'threshold',
    [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9]
)
def test_data_table(threshold: int):
    assertions = []
    for row in DataTable().table:
        if row[1] <= threshold:
            assertions.append((f'{row[0]} (Frontend:{row[2]}|Backend:{row[3]}) has {row[1]} unique visitors per '
                               f'month. (Expected more than {threshold})'))
    assert not len(assertions), '\n'.join(assertions)


# @pytest.mark.parametrize(
#     'threshold, row',
#     [
#         (thr, row)
#         for thr in [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9]
#         for row in DataTable().table
#     ]
# )
# def test_data_table(threshold: int, row: list):
#     assert row[1] > threshold, (f'{row[0]} (Frontend:{row[2]}|Backend:{row[3]}) has {row[1]} unique visitors per '
#                                 f'month. (Expected more than {threshold})')
