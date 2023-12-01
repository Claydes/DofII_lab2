import random
import model
import t2_mandani_inference
import t2_plot

class FuzzyController:
    def __init__(self):
        t2_mandani_inference.preprocessing(model.input_lvs, model.output_lv)

    @staticmethod
    def get_result(crisp):
        result = t2_mandani_inference.process(model.input_lvs, model.output_lv, model.rule_base, crisp)

        return (result[1], round(result[0], 1))


if __name__ == '__main__':
    t2_mandani_inference.preprocessing(model.input_lvs, model.output_lv)
    for i in range(4):
        t2_plot.draw_lv(model.input_lvs[i])
    t2_plot.draw_lv(model.output_lv)