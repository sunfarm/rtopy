import pandas as pd
import fire

class CLI:
    def compare(self):
        output_r = pd.read_csv('output_r.csv')
        output_python = pd.read_csv('output_python.csv')

        if not output_r.equals(output_python):
            print("Differences found between R and Python outputs.")

            if output_r.shape != output_python.shape:
                print(f"R and Python outputs differ")
            else:
                # Compare each item
                for index, (row_r, row_python) in enumerate(zip(output_r.iterrows(), output_python.iterrows())):
                    if row_r[1].equals(row_python[1]):
                        continue
                    else:
                        print(f"Difference at index {index}:")
                        print("R output:", row_r[1])
                        print("Python output:", row_python[1])
        else:
            print("No differences found. Outputs match perfectly.")

if __name__ == "__main__":
    fire.Fire(CLI)
