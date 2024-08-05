import plotly.express as px

from die import Die

class Die_Visual():
    # TODO Classe para retornar o resultado não importa quandos dados sejam usados 

    def __init__(self, rolls = 1000, dices=[]):
        self.rolls = rolls
        self.dices = dices
        self.created_dices = {}
        self.results = []

        self.create_dices()
        self.meke_rolls()

    def create_dices(self):
        # Create Dices.

        for index in range(len(self.dices)):
            key_name = f"dice_{index}"
            self.created_dices[key_name] = Die(self.dices[index])

    def meke_rolls(self):
        # Make some rolls, and store results in a list.

        result = 0
        for roll_num in range(self.rolls):
            for die in self.created_dices.values():
                result += die.roll()
            self.results.append(result)
            result = 0

    def die_max_result(self):
        # The max result of all dices.

        max_result = 0

        for die in self.created_dices.values():
            max_result += die.num_sides

        return max_result

    def analyze_result(self):
        # Analyze the results.

        frequencies = []
        max_result = self.die_max_result()
        poss_results = range(len(self.created_dices), max_result + 1)

        for value in poss_results:
            frequency = self.results.count(value)
            frequencies.append(frequency)

        return poss_results, frequencies
    
    def visualize_grafic(self):
        # Visualize the results.

        analyzed_result = self.analyze_result()

        title = f"Results of Rolling dice(s) {self.rolls} Times"
        labels = {"x": "Result", "y": "Frequency of Results"}
        fig = px.bar(x=analyzed_result[0], y=analyzed_result[1], title=title, labels=labels)

        # Further customize chart.
        fig.update_layout(xaxis_dtick=1)

        fig.show()


die_teste = Die_Visual(5000,dices=[6,6,6])

die_teste.visualize_grafic()