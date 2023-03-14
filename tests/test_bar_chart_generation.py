"""BAR chcart generation tests"""
import pytest
from plotly import graph_objects as go

from chart_generators.bar_chart import bar_chart_generation

pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_bar_chart_generation() -> None:
  """generation tests"""

  # Test case with valid data
  data = {
    "title": "My Chart",
    "data": [{
      "type": "bar",
      "x": ["foo", "bar", "baz"],
      "y": [1, 2, 4]
    }]
  }
  expected_fig = go.Figure(data=go.Figure(data=data["data"]))

  assert isinstance(await bar_chart_generation(data), go.Figure)
  assert await bar_chart_generation(data) == expected_fig

  # Test case with invalid data
  second_data_possibility = {
    "title":
      "My Chart",
    "data": [{
      "type": "bar",
      "labels": ["foo", "bar", "baz"],
      "values": [1, 2, 4]
    }]
  }
  assert await bar_chart_generation(second_data_possibility) == expected_fig
