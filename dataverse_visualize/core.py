"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['CoreClient']

# %% ../nbs/00_core.ipynb 3
import matplotlib.pyplot as plt
import requests

# %% ../nbs/00_core.ipynb 4
class CoreClient:

    def __init__(self, url):
        self.url = url

    def visualize_data(self, threshold=10):

        url = f"{self.url}/api/search?q=*&type=dataset&show_facets=true"

        response = requests.get(url)

        facets = response.json().get("data", {}).get("facets", [])

        facet_data = {}

        for item in facets:
            for key in item.keys():
                facet = item[key]
                name = facet.get("friendly")
                labels = facet.get("labels", [])
                facet_data[name] = {list(label.keys())[0]: list(label.values())[0] for label in labels}

        # Visualize each facet
        for facet_name, values in facet_data.items():
            labels = list(values.keys())
            counts = list(values.values())

            if len(labels) > threshold:
                labels = labels[:threshold]
                counts = counts[:threshold]
            
            # Create a bar chart
            plt.figure(figsize=(10, 6))
            plt.barh(labels, counts)
            plt.title(f"Facet: {facet_name}")
            plt.xlabel("Count")
            plt.ylabel("Values")
            plt.tight_layout()
            plt.show()
