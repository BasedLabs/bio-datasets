import pandas as pd

def create_markdown_from_csv(csv_file, md_file):
    df = pd.read_csv("bio_datasets.csv")
    df.index = range(1, len(df) + 1)

    with open("README.md", 'w') as md:
        md.write("#Bio Datasets \n")
        md.write("\nTo contribute, make changes to `bio_datasets.csv` and run `python create_readme.py` \n")

    with open("README.md", 'a') as md:
        df.to_markdown(buf=md)

# Calling the function with your filenames
create_markdown_from_csv("bio_datasets.csv", "README.md")
