from typing import Sequence

from ..general import AttributeAbstract

class AttributeStandartizedU(AttributeAbstract):
    def get_sigma_lcl_ucl(self) -> tuple[list[float], list[float]]:
        lcl = [self.config.limits_constant[0] for i in range(len(self.data.table))]
        ucl = [self.config.limits_constant[1] for i in range(len(self.data.table))]
        return (lcl, ucl)
    
    def get_grand_average(self) -> float:
        u = self.get_values()
        return sum([n['parameter']*n['size'] for n in u])/sum([n['size'] for n in u])
    
    def get_sample_average(self) -> float:
        u = self.get_values()
        return sum([n['parameter'] for n in u])/len(u)
    
    def get_calculate_sigma(self, item: int) -> float:
        return 1
        
    def get_cl(self) -> float:
        return 0
    
    def get_values(self) -> Sequence[dict]:
        return [{
            'parameter': n[self.config.selected_parameter]/n['size'],
            'size': n['size']
        } for n in self.data.table]
        
    def values_for_plot(self) -> Sequence[float]:
        avg = self.get_average()
        u = self.get_values()
        return [(item['parameter'] - avg)/(avg/item['size'])**0.5 for item in u]