import pandas as pd
import fire


class CLI:

    def inputs(self):
        data = pd.DataFrame({
            'Category': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'C'],
            'Values': [1, 1, 1, 2, 2, 3, 3, 3, 3]
        })
        data.to_csv('inputs.csv', index=False)

    def compare(self):
        output_r = pd.read_csv('output_r.csv')
        output_python = pd.read_csv('output_python.csv')

        comparison_result = output_r.equals(output_python)
        print("Do the outputs match? ", comparison_result)



if __name__ == "__main__":
    fire.Fire(CLI)
