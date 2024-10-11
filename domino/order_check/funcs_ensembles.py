

from .domino_process_func_obj import ProcessFunc, ProcessFuncsList
from .funcs_process import get_order_marks_array, get_domino_order_marks_array
from .funcs_multy import ordered_balance
from .funcs_self import balanced_mark
from .simmetric_mark import simmetric_marc
from domino.entrope import get_secondary_growth_entrope, get_entrope

from functools import partial

complex_ensemble_funcs = ProcessFuncsList(
  ProcessFunc(get_secondary_growth_entrope, 'Изменение энтропии'),
  ProcessFunc(get_entrope, 'Энтропия', procces_volume_param='both'), 
  ProcessFunc(ordered_balance, 'Энтропия характеристик\nупорядоченности'), 
  ProcessFunc(simmetric_marc, 'Оценка симметричности'),
  ProcessFunc(balanced_mark, 'Сбалансированность', procces_volume_param='both'),   
)

mark_domino_to_classificate = partial(get_order_marks_array, complex_ensemble_funcs=complex_ensemble_funcs)
mark_both_domino_to_classificate = partial(get_domino_order_marks_array, complex_ensemble_funcs=complex_ensemble_funcs)