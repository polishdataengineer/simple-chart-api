"""PIE chcart generation tests"""
import pytest
from plotly import graph_objects as go

from chart_generators.pie_chart import pie_chart_generation

pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_pie_chart_generation() -> None:
  """generation tests"""

  # Test case with valid data
  data = {
    "title": "My Chart",
    "data": [{
      "type": "pie",
      "labels": ["A", "B", "C"],
      "values": [1, 2, 3]
    }]
  }
  expected_fig = go.Figure(
    data=go.Pie(labels=["A", "B", "C"], values=[1, 2, 3]))
  assert isinstance(await pie_chart_generation(data), go.Figure)
  assert await pie_chart_generation(data) == expected_fig

  # Test case with invalid data
  second_data_possibility = {
    "title": "My Chart",
    "data": [{
      "type": "pie",
      "x": ["A", "B", "C"],
      "y": [1, 2, 3]
    }]
  }
  assert await pie_chart_generation(second_data_possibility) == expected_fig
