from typing import Sequence

from ..general import AttributeAbstract

class AttributeMovingAverageC(AttributeAbstract):
    def get_sigma_lcl_ucl(self) -> tuple[list[float], list[float]]:
        avg = self.get_average()
        lcl = [avg + self.config.limits_constant[0]*self.get_sigma(i) for i in range(len(self.data.table))]
        ucl = [avg + self.config.limits_constant[1]*self.get_sigma(i) for i in range(len(self.data.table))]
        return (lcl, ucl)
    
    def get_grand_average(self) -> float:
        return self.get_sample_average()
    
    def get_sample_average(self) -> float:
        return sum([n[self.config.selected_parameter] for n in self.data.table])/len(self.data.table)
    
    def get_calculate_sigma(self, item: int) -> float:
        sigmas = [self.get_average()**0.5 for i in range(len(self.data.table))]
        sigmas_total = sum(sigmas[i]*self.data.table[i]['size'] for i in range(len(sigmas)))/sum([item['size'] for item in self.data.table])
        return sigmas_total/(self.get_ma_span(item))**0.5
    
    def get_cl(self) -> float:
        return self.get_average()
    
    def get_ma_span(self, index: int) -> int:
        return self.config.ma_span if index + 1 > self.config.ma_span else index + 1
    
    def values_for_plot(self) -> Sequence[float]:
        p_values = [item[self.config.selected_parameter] for item in self.data.table]
        result = []
        for i in range(1, len(p_values)+1):
            current_slice = p_values[max(0, i-self.config.ma_span):i]
            if len(current_slice) == self.config.ma_span:
                result.append(sum(current_slice)/self.config.ma_span)
            else:
                result.append(sum(current_slice)/len(current_slice))
                
        return result