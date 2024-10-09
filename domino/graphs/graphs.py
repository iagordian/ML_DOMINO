
from abc import ABC
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import io

from .extract_data_funcs import get_random_forest_importants_pd, get_effectivity_pd

class MLGraph(ABC):

    '''
    Класс для создания графиков результатов тестирования
    '''

    extract_data_func = None

    def __init__(self, figsize=(18, 8), polar=False, labelsize=8, width_graph_coef=1.2, bottom=0.160):

        self.fig = plt.figure(figsize=figsize)
        self.ax = self.fig.add_subplot(polar=polar)
        self.ax.tick_params(axis='both', which='major', labelsize=labelsize)
        plt.grid(alpha=0.3, color='grey', linestyle='--', zorder=1)

        width = figsize[0] * width_graph_coef
        margin_left = 1 / width
        margin_right = 1 - margin_left

        margins = {
            "left": margin_left,
            "bottom": bottom,
            "right": margin_right,
            "top": 0.9
        }
        self.fig.subplots_adjust(**margins)

        self.data = self.__class__.extract_data_func()

    @property
    def bytes_string(self):
        img_container = io.BytesIO()
        self.fig.savefig(img_container, format='png')

        return base64.b64encode(img_container.getvalue()).decode('utf-8')
    
class FeatureImportansesGraph(MLGraph):
    extract_data_func = get_random_forest_importants_pd

    def __init__(self):

        super().__init__()
        
        plt.title('Важность признаков для принятия решения', y=1.04, fontweight="bold")        
        plt.xticks(rotation=20)
        sns.barplot(data=self.data, x='Признак', y='Важность признака', palette='rocket', zorder=2)
        plt.ylabel('Важность признака', fontweight="bold")
        plt.xlabel('Название признака', fontweight="bold")


class ModelEffectivityGraph(MLGraph):
    extract_data_func = get_effectivity_pd

    def __init__(self):

        super().__init__(labelsize=10, bottom=0.07)

        plt.title('Эффективность модели', y=1.04, fontweight="bold")        
        sns.lineplot(data=self.data, x='Длина ряда', y='Точность прогноза', marker='o', zorder=2, 
                     markerfacecolor='white', markersize=8, color='#8a2be2', markeredgecolor='#8a2be2')
        
        plt.xticks(list(range(6, 19)))
        plt.ylabel('Точность прогноза (Accuracy)', fontweight="bold")
        plt.xlabel('Длина ряда', fontweight="bold")
        for i, data in enumerate(zip(self.data['Точность прогноза'], self.data['Длина ряда']), start=1):
            
            accur, size = data
            accur = round(accur, 3)
            accur_next = self.data['Точность прогноза'][i] if i != self.data['Точность прогноза'].shape[0] else 0

            if all([
                i != self.data['Точность прогноза'].shape[0],
                accur > accur_next or accur_next - accur > 0.06
            ]):
                accur_pos = accur + 0.005
            else:
                accur_pos = accur - 0.006

            self.ax.annotate(accur, (size + 0.13, accur_pos), zorder=2, fontweight="bold")

            