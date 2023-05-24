from .models import Recipe
from io import BytesIO
import base64
import matplotlib.pyplot as plt


def get_recipename_from_id(val):
    recipename = Recipe.objects.get(id=val)
    return recipename


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()

    return graph


def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')

    fig = plt.figure(figsize=(7, 4))

    if chart_type == '#1':
        names = data['name']
        difficulties = data['difficulty']

        # Define the mapping of difficulty levels to values
        difficulty_values = {
            'Easy': 2,
            'Medium': 4,
            'Hard': 6
        }

        values = [difficulty_values.get(diff, 0) for diff in difficulties]

        indices = list(range(len(names)))

        bar_height = 0.3

        recipe_positions = indices

        plt.barh(recipe_positions, values, color='gray', height=bar_height)

        plt.yticks(indices, names)

        plt.xlim(0, 6)

        # Customize the tick positions and labels on the x-axis
        difficulty_levels = ['Easy', 'Medium', 'Hard']
        difficulty_values = [2, 4, 6]
        plt.xticks(difficulty_values, difficulty_levels)

    elif chart_type == '#2':
        labels = kwargs.get('labels')
        plt.pie(data['difficulty'], labels=labels)

    elif chart_type == '#3':
        plt.plot(data['name'], data['difficulty'])
    else:
        print('unknown chart type')

    plt.tight_layout()

    chart = get_graph()
    return chart
