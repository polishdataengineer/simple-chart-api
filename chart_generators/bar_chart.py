from plotly import graph_objects as go


async def bar_chart_generation(data: dict) -> go.Figure:
  """Bar chart generation"""
  try:
    # We want to read x, y or labels, values from the JSON payload
    data["data"][0]["x"] = data["data"][0]["labels"]
    data["data"][0]["y"] = data["data"][0]["values"]
    [data["data"][0].pop(element, None) for element in ["values", "labels"]]
    fig = go.Figure(data=data["data"])
  except KeyError:
    fig = go.Figure(data=data["data"])
  return fig
