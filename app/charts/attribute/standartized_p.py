from typing import Sequence

from ..general import AttributeAbstract

class AttributeStandartizedP(AttributeAbstract):
    def get_sigma_lcl_ucl(self) -> tuple[list[float], list[float]]:
        lcl = [self.config.limits_constant[0] for i in range(len(self.data.table))]
        ucl = [self.config.limits_constant[1] for i in range(len(self.data.table))]
        return (lcl, ucl)
    
    def get_grand_average(self) -> float:
        return sum([n[self.config.selected_parameter] for n in self.data.table])/sum([n['size'] for n in self.data.table])
    
    def get_sample_average(self) -> float:
        return sum([n[self.config.selected_parameter]/n['size'] for n in self.data.table])/len(self.data.table)
    
    def get_calculate_sigma(self, item: int) -> float:
        return 1
        
    def get_cl(self) -> float:
        return 0
    
    def values_for_plot(self) -> Sequence[float]:
        avg = self.get_average()
        return [(item[self.config.selected_parameter]/item['size'] - avg)/(avg*(1-avg)/item['size'])**0.5 for item in self.data.table]