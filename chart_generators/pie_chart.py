from plotly import graph_objects as go


async def pie_chart_generation(data: dict) -> go.Figure:
  """Pie chart generation"""
  try:
    # We want to read x, y or labels, values from the JSON payload
    data["data"][0]["labels"] = data["data"][0]["x"]
    data["data"][0]["values"] = data["data"][0]["y"]
    [data["data"][0].pop(element, None) for element in ["x", "y"]]
    fig = go.Figure(data=data["data"])

  except KeyError:
    fig = go.Figure(data=[
      go.Pie(
        labels=data["data"][0]["labels"],
        values=data["data"][0]["values"],
      )
    ])
  return fig
